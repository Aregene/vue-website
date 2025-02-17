'''
Date: 2025-02-16 13:26:01
LastEditors: Aregene
LastEditTime: 2025-02-16 13:26:41
'''
from sqlalchemy import  Column, Integer
from sqlalchemy.ext.declarative import declarative_base
# 创建数据的基类:
Base = declarative_base()
# 定义Data模型
class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    a = Column(Integer)
    b = Column(Integer)
    c=Column(Integer)
    d=Column(Integer)
    e=Column(Integer)
    f=Column(Integer)
    g=Column(Integer)
    h=Column(Integer)
    i=Column(Integer)
    j=Column(Integer)
    k=Column(Integer)