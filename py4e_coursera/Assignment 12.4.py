# Exercise 4: Change the urllinks.py program to extract
# and count paragraph (p) tags from the retrieved HTML document 
# and display the count of the paragraphs as the output of your program. 
# Do not display the paragraph text, only count them. 
# Test your program on several small web pages as well as some larger web pages.
#http://data.pr4e.org/romeo.txt
#http://www.dr-chuck.com/dr-chuck/resume/bio.htm



from urllib.request import urlopen  #Get links from a web page
from bs4 import BeautifulSoup       #import BeautifulSoup library
import ssl                       

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#Retrieve all of the paragraph tags
tags = soup('p')
print(len(tags))






















 
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
