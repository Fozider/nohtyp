import socket
import threading

def server_rev(*args):
    conn = args[0] 
    while True:
        try:
            data=conn.recv(1024) 
            dt=data.decode('utf-8')                                 #接收一个1024字节的数据 
            print('收到：',dt)
        except:
            print('interrupt')
            conn.close()
            
#注册服务器
def regsiter_server(ip,port,num):
    #创建tcp 流式服务器
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind((ip,port))
    s_socket.listen(num)
    print("注册服务器成功···")
    while True:
        conn,addr= s_socket.accept()
        print(addr)
        ctt = threading.Thread(target=server_rev,args=(conn,))
        ctt.daemon = True
        ctt.start()
        while True:
            aa=input('服务器发出：') 
            if aa=='quit':
                conn.close()        #关闭来自客户端的连接
                s_socket.close()              #关闭服务器端连接
            else:
                conn.send(aa.encode('utf-8'))
            
def regsiter_client(ip,port):
    #创建tcp 客户端
    c_socket = socket.socket()
    try:
        print("wait connect···")
        c_socket.connect((ip,port))                                #建立连接
        ctt = threading.Thread(target=server_rev,args=(c_socket,))
        ctt.daemon = True
        ctt.start()
        while True:

            ab=input('客户端发出：')
            if ab=='quit':
                c_socket.close()                                               #关闭客户端连接
            else:
                c_socket.send(ab.encode('utf-8'))                               #发送数据
    except:
            print("no connect···")
            
link_mode = input("是否创建服务器？y/n \r\n")
link_port = int(input('port?'))
link_maxnum = 12

#服务器列表
link_slist = []
#客户端列表
link_clist = []

#获取本机ip
local_ip = socket.gethostbyname(socket.gethostname())
print("本机ip:"+local_ip)

if (link_mode == "y"):
    print("正在注册服务器···")
    regsiter_server(local_ip,link_port,link_maxnum)
elif(link_mode == "n"):
    print("正在连接服务器···")
    regsiter_client(local_ip,link_port)
else:
    print("input ERR···")
