from app.chat.memories.histories.sql_history import SqlMessageHistory
from langchain.memory import ConversationBufferWindowMemory

def window_buffer_memory_builder(chat_args):
    return ConversationBufferWindowMemory(
        chat_memory=SqlMessageHistory(convo_id=chat_args.conversation_id),
        return_messages=True,
        memory_key="chat_history",
        output_key="answer",
        k=2
    )