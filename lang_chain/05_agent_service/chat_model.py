from pydantic import BaseModel


class ChatModel(BaseModel): # pydynamic 의 BaseModel 상속받아야 정상 작동함
    q:str