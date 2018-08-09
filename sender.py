import os, sys, math,hashlib
from random import randint
from Tkinter import *
import tkMessageBox
import socket
TCP_IP = 'localhost'
TCP_PORT = 9001
hashkey=""
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
tcpsock.listen(5)
q= 13 
p=0
s=0
def prime(num):
	flag=0
	for i in range(2,num/2):
		if(num%i==0):
			flag=1
		
	if(flag==0):
		return 1
	else:
		return 0

k=1
while(prime(k*q+1)!=1):
	k=k+1
p=k*q+1
print p
g=randint(1,p)
h=2
while(pow(g,q,p)!=1 and pow(h,(p-1)/q,p)!=g):
	g=randint(1,p)
print g

x=randint(0,q)
y=pow(g,x,p)
publickey=[p,q,g,y]
privatekey=[p,q,g,x]
root=Tk()
root.wm_title("Sender")
label_1=Label(root,text="Enter Plain Text")
label_1.grid(row=0,sticky=E)
entry_1=Entry(root)
entry_1.grid(row=0,column=1)
#hashkey=9
k=randint(0,q)
r=pow(g,k,p)%q
while(r==0):
	k=randint(0,q)
	r=pow(g,k,p)
print "r is ",r
i=1
while(k*i%q!=1):
	i=i+1
print "i is ",i
def acceptconn(event):
	global conn,r,s,hashkey,g
	conn,addr=tcpsock.accept()
button_5= Button(root,text="Connect")
button_5.grid(row=6,column=1)
button_5.bind("<Button-1>",acceptconn)
def send(event):
	global hashkey,r,s,conn
	
	message=entry_1.get()
	h1 = hashlib.sha1()
	h1.update(message)
	hashkey=h1.hexdigest()
	hashkey=int(hashkey,16)
	s=i*(hashkey+r*x)%q
	
	str4=message+"$"+str(r)+"$"+str(s)+'$'+str(publickey)+'$'+'#'
	#conn,addr=tcpsock.accept()
	conn.send(str4)	
	#conn.send(str1)
button_4= Button(root,text="SEND")
button_4.grid(row=5,column=1)
button_4.bind("<Button-1>",send)



##########################
'''
w=1
while((s*w)%q!=1):
	w=w+1
print w
u1=(hashkey*w)%q
u2=(r*w)%q
v=((pow(g,u1)*pow(y,u2))%p)%q
print "v is ",v
def((v,r,event):
	if(v==r):
		print "digital signature is valid"
		tkMessageBox.showinfo("Title", " Digital signature is verified!!! ")
button_1= Button(root,text="VERIFY")'''
root.mainloop()
