#!/usr/bin/env python3
# _*_codeding:ctf-8 

import aiomysql
import asyncio
#import log

@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool=yield from aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('aotocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )
    
@asyncio.coroutine
def select(sql,args,size=None): 
    log(sql,args)
    global __pool
    with (yield from __pool) as conn:
        cursor=yield from conn.cursor(aiomysql.DictCursor)
        yield from cursor.execute(sql.replace('?','%s'),args or ())
        if size:
            rs=yield from cursor.fetchmany(size)
        else:
            rs=yield from cursor.fetchall()
        yield from cursor.close()
        logging.info('rows returned: %s' % len(rs))     
        return rs
        
@asyncio.coroutine
def execute(sql,args):
    log(sql)
    with (yield from __pool) as conn:
        try:
            cursor=yield from conn.cursor()
            yield from cursor.execute(sql.replace('?','%s'),args)
            affected = cursor.rowcount
            yield from cursor.close()
        except BaseException as e:
            raise
        return affected
        
from orm import Model,StringField,IntegerField

class user(Model):
    __table__='users'
    
    id=IntegerField(primary_key=True)
    name=StringField()
    