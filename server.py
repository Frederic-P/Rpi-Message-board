from socket import *
import datetime

host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print "Listening..."
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    now = datetime.datetime.now().time()
    hh = str(now.hour)
    mm = str(now.minute)
    ss = str(now.second)
    time = "%s:%s:%s " %(hh, mm, ss)
    print "Received message at : " + time + data
UDPSock.close()

