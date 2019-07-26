import os

iplist = open("list.txt","r")
lines = iplist.readlines()
iplist.close()
f=open("online.txt", "a+")
g=open("offline.txt", "a+")
for line in lines:
    if os.system("ping -n 1 " + line) == 0: #FOR LINUX CHANGE "ping -n 1 " TO "ping -c 1 "
        f.write(line)
    else:
        g.write(line)
f.close()
