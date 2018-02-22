import socket
from logging import LogSocket
from compressor import GzipSocket

def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, 'utf8'))
    client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',2401))
server.listen(1)
log_send = True
compress_hosts = ['127.0.0.1','localhost']

try:
    while True:
        client, addr = server.accept()

        # We only have to change one line in our original code to use this decorator. Instead
        # of calling respond with the socket, we call it with a decorated socket:
        if log_send:
            client = LogSocket(client)
        if client.socket.getpeername()[0] in compress_hosts:
           client = GzipSocket(client)
        respond(client)
        # respond(client)
finally:
    server.close()
