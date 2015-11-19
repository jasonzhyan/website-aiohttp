#!/usr/bin/env python3
# _*_codeding:ctf-8 
#models.py
import orm
from models import User, Blog, Comment
import asyncio

def test():
    loop=asyncio.get_event_loop()
    yield from orm.create_pool(loop,user='www-data',password='www-data',database='firsttime')
    
    u=User(name='test',email='test@test.com',passwd='11111',image='nothing')
    
    yield from u.save()

    
for x in test():
    print('x=',x)
    
#loop=asyncio.get_event_loop()
#yield from orm.create_pool(loop,user='www-data',password='www-data',database='firsttime')