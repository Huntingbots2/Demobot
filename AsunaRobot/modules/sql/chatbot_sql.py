import threading

from sqlalchemy import Column, String

from AsunaRobot.modules.sql import BASE, SESSION


class  AsunaChats(BASE):
    __tablename__ = "mukesh_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


 AsunaChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_mukesh(chat_id):
    try:
        chat = SESSION.query( AsunaChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_mukesh(chat_id):
    with INSERTION_LOCK:
        mukeshchat = SESSION.query( AsunaChats).get(str(chat_id))
        if not mukeshchat:
            mukeshchat =  AsunaChats(str(chat_id))
        SESSION.add(mukeshchat)
        SESSION.commit()


def rem_mukesh(chat_id):
    with INSERTION_LOCK:
        mukeshchat = SESSION.query( AsunaChats).get(str(chat_id))
        if mukeshchat:
            SESSION.delete(mukeshchat)
        SESSION.commit()
