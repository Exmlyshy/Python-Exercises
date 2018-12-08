#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-25 19:29:16
import random

from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Jihuoma(Base):
	__tablename__='Jihuoma'

	jihuoma=Column(String(20),primary_key=True)

engine=create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
DBSession=sessionmaker(bind=engine)

session=DBSession()


def rndChar():
    if random.random() > 0.5:
        return chr(random.randint(65, 90))
    return chr(random.randint(97, 122))


for i in range(200):
    CodeStr = ''
    for j in range(10):
        CodeStr += rndChar()
    new=Jihuoma(jihuoma=CodeStr)
    session.add(new)

# new_1=Jihuoma(jihuoma='test1')
# new_2=Jihuoma(jihuoma='test2')
# session.add(new_1)
# session.add(new_2)
session.commit()
session.close()