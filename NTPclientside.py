from socket import AF_INET, SOCK_DGRAM
import socket, struct, time, sys, NTPserver

HOSTNAME = socket.gethostname()
HOST = socket.gethostbyname(HOSTNAME)
PORT = 12345
BUFFER = 1024
ADDRESS = (HOST, PORT)
s = socket.socket(AF_INET, SOCK_DGRAM)
while True:
    message = input()
    if message == "x":
        break
    else:
        message = str(NTPserver.NTPtime()) + "|" + message
        print(message.encode())
        s.sendto(message.encode(), ADDRESS)

