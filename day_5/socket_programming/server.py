# server code

import socket

def main():
    host = "192.168.1.100"
    port = 5000
    
    #create a socket object
    s = socket.socket()

    #bind that socket object to a port
    s.bind((host, port))

    #tell server to start listening for communication
    s.listen(1) # -> it will only listen 1 connection at a time

    # accept a communication
    c, addr = s.accept() # c -> connection, addr -> address

    print("Connection from: " + str(addr))

    while True:
        data = c.recv(1024)     # going to receive some bytes
        if not data:
            break
        print("form connected user:" + str(data))
        print("Sending: " + str(data))
        c.send(data)
    
    c.close()

main()
    