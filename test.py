#!/usr/bin/env python3
# _*_codeding:ctf-8 
#models.py
import orm
from models import User, Blog, Comment
import asyncio

@asyncio.coroutine
def test(loop):
    
    yield from orm.create_pool(loop=loop,user='root',password='password',db='first')
    u=User(name='test3',email='test4@test.com',passwd='test',image='about:blank')
    yield from u.save()
    

loop = asyncio.get_event_loop()
   
loop.run_until_complete(test(loop))
loop.close()

#for x in test(loop):
#    print('x=',x)
'''
def test(loop):
    
    yield from orm.create_pool(loop,user='www-data',password='www-data',db='first')
    
    #u=User(name='test',email='test@test.com',passwd='11111',image='nothing')
    
    #yield from u.save()

loop=asyncio.get_event_loop()    
loop.run_until_complete(test(loop))
loop.close()

#for x in test(loop):
#    print('x=',x)
    
#loop=asyncio.get_event_loop()
#yield from orm.create_pool(loop,user='www-data',password='www-data',database='firsttime')
'''
