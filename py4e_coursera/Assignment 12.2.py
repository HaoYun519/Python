# Exercise 2: Change your socket program so that it counts the number
#  of characters it has received and stops displaying any text
#  after it has shown 3000 characters. The program should retrieve 
#  the entire document and count the total number of characters 
#  and display the count of the number of characters at the end 
#  of the document.
# Test with http://www.dr-chuck.com/dr-chuck/resume/bio.htm
 
import socket

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    received = b""
    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        received += data
        
    received = received.decode()    
    print(received[:3000])
    print(len(received))
    
    mysock.close()
except:
    print('The URL is improperly formatted or non-existent!')


#http://data.pr4e.org/romeo.txt 