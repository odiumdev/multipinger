import os

iplist = open("list.txt","r")
lines = iplist.readlines()
iplist.close()
f=open("online.txt", "a+")
g=open("offline.txt", "a+")
for line in lines:
    if os.system("ping -l 50 -n 1 " + line) == 0:
        f.write(line)
    else:
        g.write(line)
f.close()
