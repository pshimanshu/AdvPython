# client code

import socket

def main():
    host = "192.168.1.100"
    port = 5000
    
    #create a socket object
    s = socket.socket()
    
    #connect to port
    s.connect((host, port))

    msg = input("<<-->>")

    while msg!="q":
        s.send(msg.encode("ascii"))
        data = s.recv(1024)
        print("Received from server: " + str(data))
        msg = input("<<-->>")
    
    s.close()


main()
