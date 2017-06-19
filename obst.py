#!/bin/python

import os,sys,socket,time,commands

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.122.96 ",3333))

#data will recvice drive name
data=s.recvfrom(20)
d_name=data[0]

if os.path.isdir(d_name) :
	print "TRUE"

	#data1 will receive drive size 
	data1=s.recvfrom(10)
	d_size=data1[0]

	#cliaddr will receive client ip
	cliadd= data1[1][0]
	 
	#creating LVM by the name of the drive
	os.system('lvcreate  --name  '+d_name+'  --size  '+d_size+'M   drive1')

	#now formating the storage drive
	os.system('mkfs.ext4  /dev/drive1/'+d_name)

	#creating a directory for drive 
	os.system('mkdir /mnt/'+d_name)

	#now mount the storage drive
	os.system('mount /dev/drive1/'+d_name+'  /mnt/'+d_name)

	#now NFS server configuration
	os.system('yum install nfs-utils -y')

	#making in entery in nfs export file
	entry="/mnt/"+d_name+" "+cliadd+"(rw,no_root_squash)"

	#appending entry var to /etc/exports file
	f=open('/etc/exports','a')
	f.write(entry)
	f.write("\n")
	f.close()

	#starting nfs service
	service=os.system('exportfs -r')
	if service == 0 :
		print "done"
		s.sendto("done",data1[1])
	else :
		print "check your code"
else :
	print "this name drive already exit"
