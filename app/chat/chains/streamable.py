from queue import Queue
from threading import Thread
from app.chat.callbacks.stream import StreamingHandler
from flask import current_app


class StreamableChain:
    ##Overriding the stream function 
    def stream(self, input):

        queue= Queue()
        handler =  StreamingHandler(queue)

        # self(input)  This executes the chian but waits for all tokens to be assembled before executing next line, which defeats our purpuse of streaming from 
        #Can solve this by running it in a separate thread

        def task(app_context):
            app_context.push()
            self(input, callbacks=[handler]) #We are defining our handler and passing into the chain at call time. i.e whenevr we call Chain, we pass handler and it gets used by all objects inside the chain

        #Sadly this thread wont have access to application context i.e Flask error
        #Hence we pass context as args when we call a new thread. i.e task()
        Thread(target=task, args=[current_app.app_context()]).start()

        while True:
            token = queue.get()
            if token is None:
                break
            yield token