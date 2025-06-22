from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv
from langchain.callbacks.base import BaseCallbackHandler
from queue import Queue
from threading import Thread

load_dotenv()
queue = Queue()

#This class will stream tokens as it receives it from the OpenAI servers
#gotta figure out a way to push the tokens from here to the StreamingChain generator
class StreamingHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token, **kwargs):
        queue.put(token)

    def on_llm_end(self, response, **kwargs):
        queue.put(None)

    def on_llm_error(self, error, **kwargs):
        queue.put(None)

chat = ChatOpenAI(streaming=True, callbacks=[StreamingHandler()])

prompt = ChatPromptTemplate.from_messages(
    [("human", "{content}")]
)

# chain = LLMChain( llm=chat, prompt=prompt)

# # messages = prompt.format_messages(content= "tell me a 5 jokes")

# #when we call an object like a function (i.e chat), python automatically calls __call__
# # output = chat.stream(messages)

# #chat.stream will override the streaming flag in ChatOpenAI class, return a generator obj
# #chain.stream is different from chat.stream
# for output in chain.stream(input={"content": "tell me a 2 jokes"}):
#     print(output)

class StreamingChain(LLMChain):
    ##Overriding the stream function 
    def stream(self, input):
        # self(input)  This executes the chian but waits for all tokens to be assembled before executing next line, which defeats our purpuse of streaming from 
        #Can solve this by running it in a separate thread

        def task():
            self(input)

        Thread(target=task).start()

        while True:
            token = queue.get()
            if token is None:
                break
            yield token

chain = StreamingChain(llm=chat, prompt=prompt)

input = {"content": "Tell me a joke"}

for output in chain.stream(input=input):
    print(output)