#!/usr/bin/env python3
# _*_codeding:ctf-8 

import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')
    
@asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)                                           #创建web应用
    app.router.add_route('GET','/',index)                                   #新增路由，监听‘GET’'/'
    srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)   #新建服务器由执行者（分出来的协程？）监听’127.0.0.1‘9000端口
    logging.info('server started at http://127.0.0.1:9000...')
    return srv
    
loop=asyncio.get_event_loop()        #创建事件循环
loop.run_until_complete(init(loop))  #开始事件循环
loop.run_forever()                   #一直循环