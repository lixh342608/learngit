#coding=utf-8
'''
Created on 2016年9月13日

@author: pc
'''
import socket,time,threading

def tcplink(so, addr):
    print('Accept new connection from %s:%s...' % addr)
    so.send(b'Welcome!')
    while True:
        data = so.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        so.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    so.close()
    print('Connection from %s:%s closed.' % addr)

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(("127.0.0.1",9999))

sock.listen(5)
print('Waiting for connection...')

while True:
    # 接受一个新连接:
    so,addr = sock.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(so, addr))
    t.start()
"""def tcplink(so, addr):
    print('Accept new connection from %s:%s...' % addr)
    so.send(b'Welcome!')
    while True:
        data = so.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        so.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    so.close()
    print('Connection from %s:%s closed.' % addr)"""