from datetime import datetime
from sqlalchemy import Column,Integer,String,DateTime
from .db import Base

class User(Base):

    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),unique=True,nullable=False)
    password = Column(String(50),nullable=False)
    last_login = Column(DateTime,default=datetime.now)

    def __repr__(self):
        return '<User #{}:{}>'.format(self.id,self.name)