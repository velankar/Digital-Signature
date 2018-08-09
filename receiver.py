import os, sys, math,hashlib
from random import randint
from Tkinter import *
import tkMessageBox
import socket
root=Tk()
root.wm_title("Receiver")
TCP_IP = 'localhost'
TCP_PORT = 9001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
def recc(event):
	global data,s1
	pubkey=''
	s1=""
	q=13
	data = s.recv(100)
	l1=data.split('$')
	msg = Message(root, text = l1[0],aspect=500)
	
	msg.config(bg='lightgreen', font=('times', 12, 'italic'))
	msg.grid(row=7)
	h1 = hashlib.sha1()
	h1.update(l1[0])
	hashkey=h1.hexdigest()
	hashkey=int(hashkey,16)
	##########################

	r=l1[1]
	r=int(r)
	s1=l1[2]
	s1=int(s1)
	
	
	print l1[3]
	for i in range (1,len(l1[3])-1):
		pubkey=pubkey+l1[3][i]
	print pubkey
	publickey=pubkey.split(',')
	p=int(publickey[0])
	q=int(publickey[1])
	g=int(publickey[2])
	y=int(publickey[3])
	s1=int(s1)
	w=1
	while((s1*w)%q!=1):
		w=w+1
	print w
	u1=(hashkey*w)%q
	u2=(r*w)%q
	v=((pow(g,u1)*pow(y,u2))%p)%q
	print "v is ",v
	
	if(v==r):
		print "digital signature is valid"
		tkMessageBox.showinfo("Title", " Digital signature is verified!!! ")
	button_1= Button(root,text="VERIFY")
button_1= Button(root,text=" Verify Digital Signatue")
button_1.grid(row=1)
button_1.bind("<Button-1>",recc)
root.mainloop()
