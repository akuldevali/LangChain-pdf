import random
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from app.chat.models import ChatArgs
from app.chat.vector_stores import retriever_map
from app.chat.llms import llm_map
from app.chat.memories import memory_map
from app.chat.chains.retrieval import StreamingConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI
from app.web.api import ( set_conversation_components, get_conversation_components)
from app.chat.score import random_component_by_score

def select_component(component_type, component_map, chat_args):
    components = get_conversation_components(chat_args.conversation_id)

    previous_component = components[component_type]

    if previous_component:
        builder = component_map[previous_component]
        return previous_component, builder(chat_args)
    else:
        # random_name = random.choice(list(component_map.keys()))
        random_name= random_component_by_score(component_type, component_map)
        builder = component_map[random_name]
        return random_name, builder(chat_args)
    
def build_chat(chat_args: ChatArgs):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming flag.

    :return: A chain

    Example Usage:

        chain = build_chat(chat_args)
    """

    retriever_name , retriever = select_component(
        "retriever",
        retriever_map,
        chat_args
    )

    llm_name, llm = select_component(
        "llm",
        llm_map,
        chat_args
    )

    memory_name, memory = select_component(
        "memory",
        memory_map,
        chat_args
    )
    print( f"Running chain with\n Memory:{memory_name},\n LLM : {llm_name},\n Retriever : {retriever_name} \n")
    set_conversation_components(chat_args.conversation_id, llm=llm_name,retriever=retriever_name, memory=memory_name)

    # retriever = build_retriever(chat_args)
    # llm = build_llm(chat_args)
    condense_question_llm = ChatOpenAI(streaming=False) #Specifically used by condense_ques_chain
    # memory = build_memory(chat_args)

    #modified the from_llm src code to accomodate 2 different chat_models
    return StreamingConversationalRetrievalChain.from_llm(
        llm=llm,
        condense_question_llm=condense_question_llm,
        memory=memory,
        retriever=retriever
    )
