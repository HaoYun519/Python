# Exercise 3: Use urllib to replicate the previous exercise of 
# (1) retrieving the document from a URL,
# (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document.
#  Don’t worry about the headers for this exercise,
#  simply show the first 3000 characters of the document contents.
#http://data.pr4e.org/romeo.txt

import urllib.request

url = input('Enter URL: ')
content = urllib.request.urlopen(url).read()
content = content.decode()    

print(content[:3000])
print(len(content))
    


























 
# import socket

# try:
#     mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     mysock.connect(('data.pr4e.org', 80))
#     cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#     mysock.send(cmd)

#     received = b""
#     while True:
#         data = mysock.recv(512)
#         if (len(data) < 1):
#             break
#         received += data
        
#     received = received.decode()    
#     print(received[:3000])
#     print(len(received))
    
#     mysock.close()
# except:
#     print('The URL is improperly formatted or non-existent!')
    

    

    
# try:
# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
