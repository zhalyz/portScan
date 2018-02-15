import socket
import sys
ports = [22, 80, 443, 445,  515, 8080, 10000, 20000]
host = '192.168.1.1/32'
sub=int(host.split('/')[1])
host=host.split('/')[0]
host=[int(x) for x in host.split('.')]
pos=int(sub/8)
ips=2**(32-sub)
for i in range(pos,4):
    host[i]=0
for i in range(0,ips):
    temp='.'.join([str(x) for x in host])
    for port in mas:
        s=socket.socket()
        s.settimeout(1)
        try:
            s.connect((temp,port))
        except socket.error:
            print(temp+' '+str(port)+' CLOSE')
        else:
            s.close()
            if port==80 or port==443:
                print("check")
            print(temp+' '+str(port)+' OPEN')
    host[3]+=1
    if host[3]==256:
        if host[2]==256:
            if host[1]==256:
                host[0]+=1
                host[1]=0
            host[1]+=1
            host[2]=0
        host[2]+=1
        host[3]=0
