import threading
import time

from sqlalchemy import Column, String, Integer, BigInteger
from AsunaRobot.modules.sql import BASE, SESSION

class AFK(BASE):
    __tablename__ = "afk_users"
    user_id = Column(BigInteger, primary_key=True)
    reason = Column(String)
    time = Column(Integer)

    def __init__(self, user_id, reason, time):
        self.user_id = user_id
        self.reason = reason
        self.time = time

AFK.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()

def is_afk(user_id):
    try:
        return SESSION.query(AFK).get(user_id)
    finally:
        SESSION.close()

def set_afk(user_id, reason, afk_time):
    with INSERTION_LOCK:
        afk = SESSION.query(AFK).get(user_id)
        if afk:
            afk.reason = reason
            afk.time = afk_time
        else:
            afk = AFK(user_id, reason, afk_time)
            SESSION.add(afk)
        SESSION.commit()

def remove_afk(user_id):
    with INSERTION_LOCK:
        afk = SESSION.query(AFK).get(user_id)
        if afk:
            SESSION.delete(afk)
            SESSION.commit()
            return True
        return False

def get_afk_reason(user_id):
    afk = SESSION.query(AFK).get(user_id)
    return afk.reason if afk else None

def get_afk_time(user_id):
    afk = SESSION.query(AFK).get(user_id)
    return afk.time if afk else None

def clear_afk(user_id):
    with INSERTION_LOCK:
        afk = SESSION.query(AFK).get(user_id)
        if afk:
            
