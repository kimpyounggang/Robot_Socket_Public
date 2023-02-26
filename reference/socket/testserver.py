import socket
from sqlite3 import connect

#소켓생성
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#소켓 포트에 연결
server_adress = ('localhost',8080)
print(*server_adress)
sock.bind(server_adress)

#소켓대기
sock.listen()

while True:
    print("연결을 대기")

    connection,client_address = sock.accept()

    try:
        print('connection from',client_address)

        #작은 데이터 받고 다시 전송

        while True:
            data = connection.recv(16)
            print(data)
            if data != None:
                connection.sendall(data)
            else:
                print('no data',client_address)
                break
    finally:
        print("close")
        connection.close()

