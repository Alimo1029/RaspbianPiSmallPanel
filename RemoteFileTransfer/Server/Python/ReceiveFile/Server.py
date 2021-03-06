#创建日期：2019年12月17日18:26:13
#简介：基于Python的文件传输服务
#编写人：limo1029
#软件：vim
#附注：Server端
#版权声明(C)limo1029


#引用模块
from socket import * as sk
import threading
from hashlib import sha256

#获取本机IP
local_name = sk.getfqdn(sk.gethostname())
local_ip = sk.gethostbyname(local_name)

#声明依赖函数组

#传输凭证验证（访问令牌）
def checking(username, password, root_password):
    sha256_input_root_password = sha256(root_password).hexdigest()
    print(sha256_input_root_password)

#新客户连接调用此函数
def new_connect(client_executor, address):
    print('来自%s%s的连接' %address)


#主执行函数

#构建socket实例
listener = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
listener.bind((local_ip, 39254))
listener.listen(5)
print('等待连接......')

#声明主函数
def run():
    new_connect()
    checking(1,1,1)
#死循环等待，若有客户连接，分配线程处理客户请求，继续等待，如此循环
while True:
    client_executor, address = listener.accept()
    tg = threading.Thread(target = run, args = (client_executor, address))
    tg.start()
