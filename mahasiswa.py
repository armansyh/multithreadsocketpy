import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.1", 7777))

while True:
    data = sock.recv(100)
    data = data.decode("ascii")
    print(data)