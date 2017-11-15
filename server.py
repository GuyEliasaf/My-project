import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
host = 'guyeliasaf'
port = int(input("Enter port over 1024"))
address = (host, port)
s.bind(address)
message = raw_input("Enter text")
s.listen(5)
while True:
    c, addr = s.accept()
    print ("Got connection from", addr)
    c.send(message)
    c.close()
