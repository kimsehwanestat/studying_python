from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 1234))

print('연결 확인되었습니다')
clientSock.send('I am a client'.encode('utf-8'))

print('메시지를 전송했습니다.')


while True:
    data = clientSock.recv(1024)
    print('받은 데이터:', data.decode('utf-8'))

    sendData = input('>>>')
    clientSock.send(sendData.encode('utf-8'))
    
