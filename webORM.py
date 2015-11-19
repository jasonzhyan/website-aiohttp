#!/usr/bin/env python3
# _*_codeding:ctf-8 

import aiomysql
import asyncio
import logging;logging.basicConfig(level=logging.INFO)
from orm import Model
from orm import StringField,IntegerField

@asyncio.coroutine
def create_pool(loop,**kw):  					#create a connection pool
    logging.info('create database connection pool...')
    global __pool								# global variable means there's only one __pool and all the functions can use the same pool
    __pool=yield from aiomysql.create_pool(     # create pool (give a value to a global variable "__pool" which is a instance)
                                                # and I think it is equals mysql.connector.connec(user=.....)   
        host=kw.get('host','localhost'),  		# 为pool的参数赋值,kw为可视为（组装为）dict的关键字参数，这说明函数create_pool可接受关键字参数，或者命名关键字参数
        port=kw.get('port',3306),				# it means kw have a function".get" 3306是'port'不存在时的默认值
        user=kw['user'],
        password=kw['password'],          		 # it means kw is a dictionary
        db=kw['db'],
        charset=kw.get('charset','utf8'),		#除了数据库名，用户名，密码，其他都有默认值
        autocommit=kw.get('aotocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )
    
@asyncio.coroutine
def select(sql,args,size=None):           #create a "select" function with whom we can do select words
    log(sql,args)  #what is log？
    global __pool							#声明全局变量？
    with (yield from __pool) as conn:    #create a connection with connction pool "__pool"
        cursor=yield from conn.cursor(aiomysql.DictCursor)
        yield from cursor.execute(sql.replace('?','%s'),args or ()) #'?' is a SQL words and replace sth
		                                               # But args is for what?
        if size:
            rs=yield from cursor.fetchmany(size)             #use different words recieve word from mysql base on if there is a value of "size"
        else:
            rs=yield from cursor.fetchall()					#返回值是一组dict？
        yield from cursor.close()
        logging.info('rows returned: %s' % len(rs))          #calculate the elements in rs,and this is the row's number
        return rs          # Return a list in which there is the execute result
        
@asyncio.coroutine
def execute(sql,args):   #this function is used for the words"delete","update","modify","insert"
    log(sql)
	global __pool #is there any affection with this row? and can I add this?
    with (yield from __pool) as conn:
        try:						#为什么这里有try而select没有。这里容易出错。
            cursor=yield from conn.cursor()
            yield from cursor.execute(sql.replace('?','%s'),args)
            affected = cursor.rowcount
            yield from cursor.close()
        except BaseException as e:  #基础错误？框架异常基类
            raise
        return affected
        


class User(Model):
    __table__='users'
    
    id=IntegerField(primary_key=True)    #当不按照顺序使用默认参数时，需要写上参数名，这就是一个例子
    name=StringField()
    
	