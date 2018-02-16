import socket
import sys
import requests
import re

def hosts(host):
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
    return host

def request(host):
    response=requests.get('http://'+host)
    if response.headers['Server']=='':
        print("Поле \"Server\" в зоголовке отсутствует")
    else:
        print("Server: "+response.headers['Server'])

def putin_ip():
    print("Введите ip адрес (формат x.x.x.x/y): ")
    host = input()
    if check_ip_format(host)==False:
        host=putin_ip()
    return host

def error():
    print("Неверный формат входных данных")

def check_ip_format(host):
    if re.match(r'\d+[.]+\d+[.]+\d+[.]+\d+[/]+\d+$',host)==None:
        error()
        return False
    sub=int(host.split('/')[1])
    if sub >32:
        error()
        return False
    host=[int(x) for x in host.split('/')[0].split('.')]
    for i in host:
        if i>255:
            error()
            return False
    return True

def check_ports_format(mas):
    if re.match(r'\d+([,]\d+)*$',mas)==None:
        error()
        return False
    return True

def putin_ports():
    print("Введите номера портов (через запятую): ")
    ports = input().replace(' ','')
    if check_ports_format(ports)==False:
        ports=putin_ports()
    return ports

host=putin_ip()
sub=int(host.split('/')[1])
mas=putin_ports()
mas=[int(x) for x in mas.split(',')]
pos=int(sub/8)
ips=2**(32-sub)
host=[int(x) for x in host.split('/')[0].split('.')]
for i in range(pos,4):
    host[i]=0
for i in range(0,ips):
    flag=False
    temp='.'.join([str(x) for x in host])
    for port in mas:
        s=socket.socket()
        s.settimeout(1)
        try:
            s.connect((temp,port))
        except socket.error:
            pass
        else:
            s.close()
            print(temp+' '+str(port)+' OPEN')
            if (port==80 or port==443) and flag==False:
                request(temp)
                flag=True
    host=hosts(host)
