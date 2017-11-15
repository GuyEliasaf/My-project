import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

host = 'guyeliasaf'
port = int(input("Enter port over 1024"))
address = (host, port)
s.connect(address)
print(s.recv(1024))
s.close()