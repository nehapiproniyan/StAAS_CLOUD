#!/bin/python

import os,commands,sys,time,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.122.96"
s_port=3333

drive_name=raw_input("enter storage drive name:")
drive_size=raw_input("enter storage drive of size in M:")

s.sendto(drive_name,(s_ip,s_port))
s.sendto(drive_size,(s_ip,s_port))

msg=s.recvfrom(10)


if msg[0] == "done" :
	os.system('mkdir  /media/'+drive_name)
        os.system('mount  '+s_ip+':mnt/'+drive_name+'  /media/'+drive_name)
	print "done"
else :
	print "no response" 

