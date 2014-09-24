import socket
import re
import time
import math

def caesar(plainText, shift): 
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  return cipherText

HOST = '54.209.5.48'    # The remote host
PORT = 12345              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = s.recv(1024)
print data
data = s.recv(1024)
print data
a = re.compile("psifer text: (.*)")
cs = a.findall(data)[0]

for key in range(26):
    text = caesar(cs, key)
    if 'theanswertothisstageis' in text:
        cs_answer = text[len('theanswertothisstageis'):]
        break

s.send(cs_answer + "\n")

time.sleep(1)
data = s.recv(1024)
print data

a = re.compile("psifer text: (.*)")

def code(n, msg):
    m = len(msg)
    l = math.floor(m / n)

    decoded = []
    for i in range(n):
        for j in range(int(l)):
            decoded.append(msg[i+j*n])

    return "".join(decoded)

m = a.findall(data)[0]
for i in range(1,50):
    res1 = code(i, m)
    if "winning" in res1:
        s.send("winning for the win\n")
        break
    if "easiest" in res1:
        s.send("easiest answer\n")
        break
    if "easy" in res1:
        s.send("easy answer\n")
        break
    if "more" in res1:
        s.send("more answers here\n")
        break
    if "goes" in res1:
        s.send("this is where the answer goes\n")
        break


data = s.recv(1024)
print data

data = s.recv(1024)
print data

s.send('MAGICWAND\n')

time.sleep(1)
data = s.recv(1024)
print data
time.sleep(1)
data = s.recv(1024)
print data
s.close()