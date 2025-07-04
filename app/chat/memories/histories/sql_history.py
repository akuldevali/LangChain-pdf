from pydantic import BaseModel
from langchain.schema import BaseChatMessageHistory
from app.web.api import (
    get_messages_by_conversation_id,
    add_message_to_conversation
)

#A custom class to persist messages in db
class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
    convo_id : str

    @property
    def messages(self):
        return get_messages_by_conversation_id(self.convo_id)
    
    def add_message(self, message):
        return add_message_to_conversation(
            conversation_id=self.convo_id,
            role=message.type,
            content=message.content
        )
    
    def clear(self):
        pass