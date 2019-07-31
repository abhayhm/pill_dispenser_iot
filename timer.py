#iporting necessary modules

import RPi.GPIO as GPIO
import datetime
import time
from tkinter import *
from _thread import start_new_thread

#function to exit the program
def getfun():
	exit()

#function to compare current time and quantity with user input time and quantity
def compar():
	z=0
	while True:
		ct=datetime.datetime.now()
		hour=str(ct.hour)
		minute=str(ct.minute)
		qt=0
		print(z)
		if hour==morningt1h and minute==morningt1m:
			while qt<int(morningq1):
				p1.ChangeDutyCycle(2.5)
				time.sleep(0.5)
				p1.ChangeDutyCycle(12.5)
				time.sleep(0.5)
				p1.ChangeDutyCycle(0)
				qt+=1
				print("a")
				time.sleep(1)	
		qt=0
		print(z)
		if hour==afternoont1h and minute==afternoont1m:
			while qt<int(afternoonq1):
				p1.ChangeDutyCycle(2.5)
				time.sleep(0.5)
				p1.ChangeDutyCycle(12.5)
				time.sleep(0.5)
				p1.ChangeDutyCycle(0)
				qt+=1
				print("b")	
				time.sleep(1)
		qt=0
		print(z)
		if hour==nightt1h and minute==nightt1m:
			while qt<int(nightq1):
				p1.ChangeDutyCycle(2.5)
				time.sleep(0.5)
				p1.ChangeDutyCycle(12.5)
				time.sleep(0.5)
				p1.ChangeDutyCycle(0)
				qt+=1	
				print("c")
				time.sleep(1)
		qt=0
		print(z)
		if hour==morningt2h and minute==morningt2m:
			while qt<int(morningq2):
				p2.ChangeDutyCycle(2.5)
				time.sleep(0.5)
				p2.ChangeDutyCycle(12.5)
				time.sleep(0.5)
				p2.ChangeDutyCycle(0)
				qt+=1
				print("d")
				time.sleep(1)	
		qt=0
		print(z)
		if hour==afternoont2h and minute==afternoont2m:
			while qt<int(afternoonq2):
				p2.ChangeDutyCycle(2.5)
				time.sleep(0.5)
				p2.ChangeDutyCycle(12.5)
				time.sleep(0.5)
				p2.ChangeDutyCycle(0)
				qt+=1
				print("e")
				time.sleep(1)
		qt=0
		print(z)
		if hour==nightt2h and minute==nightt2m:
			while qt<int(nightq2):
				p2.ChangeDutyCycle(2.5)
				time.sleep(0.5)
				p2.ChangeDutyCycle(12.5)
				time.sleep(0.5)
				p2.ChangeDutyCycle(0)
				qt+=1
				print("f")
				time.sleep(1)
		time.sleep(60)
		z+=1

#creating gui
tk=Tk()
tk.title("MEDIBOX")
tk.geometry("475x350")

servo1=20
servo2=21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(servo1, GPIO.OUT)
GPIO.setup(servo2, GPIO.OUT)

p1=GPIO.PWM(servo1, 50)
p2=GPIO.PWM(servo2, 50)

p1.start(12.5)
p2.start(12.5)

#reading user input data from the text file 
with open("data.txt","r") as file:
	lst=file.readlines()

morningt1h=lst[0][2:4]
morningt1m=lst[0][5:7]
morningq1=lst[0][0]

morningt2h=lst[1][2:4]
morningt2m=lst[1][5:7]
morningq2=lst[1][0]

afternoont1h=lst[2][2:4]
afternoont1m=lst[2][5:7]
afternoonq1=lst[2][0]

afternoont2h=lst[3][2:4]
afternoont2m=lst[3][5:7]
afternoonq2=lst[3][0]

nightt1h=lst[4][2:4]
nightt1m=lst[4][5:7]
nightq1=lst[4][0]

nightt2h=lst[5][2:4]
nightt2m=lst[5][5:7]
nightq2=lst[5][0]

#developing gui for displlaying the user input data read from text file
mes=StringVar()
mes.set("PILL DETAILS OF THE PATIENT PILL,QUANTITY AND TIME")
l1=Label(tk,textvariable = mes)
l1.grid(row=0,column=0,columnspan=2)


pill1=StringVar()
pill1.set("Q/T")
lem=Label(tk,textvariable=pill1)
lem.grid(row=1,column=1)

pill1=StringVar()
pill1.set("PILL 1")
lem=Label(tk,textvariable=pill1)
lem.grid(row=2,column=0)

tb=StringVar()
tb.set(lst[0])
lem=Label(tk,textvariable=tb)
lem.grid(row=2,column=1,columnspan=2)

pill1=StringVar()
pill1.set("PILL 2")
lem=Label(tk,textvariable=pill1)
lem.grid(row=3,column=0)

tb=StringVar()
tb.set(lst[1])
lem=Label(tk,textvariable=tb)
lem.grid(row=3,column=1,columnspan=2)

pill1=StringVar()
pill1.set("PILL 1")
lem=Label(tk,textvariable=pill1)
lem.grid(row=4,column=0)

tb=StringVar()
tb.set(lst[2])
lem=Label(tk,textvariable=tb)
lem.grid(row=4,column=1,columnspan=2)

pill1=StringVar()
pill1.set("PILL 2")
lem=Label(tk,textvariable=pill1)
lem.grid(row=5,column=0)

tb=StringVar()
tb.set(lst[3])
lem=Label(tk,textvariable=tb)
lem.grid(row=5,column=1,columnspan=2)

pill1=StringVar()
pill1.set("PILL 1")
lem=Label(tk,textvariable=pill1)
lem.grid(row=6,column=0)

tb=StringVar()
tb.set(lst[4])
lem=Label(tk,textvariable=tb)
lem.grid(row=6,column=1,columnspan=2)

pill1=StringVar()
pill1.set("PILL 2")
lem=Label(tk,textvariable=pill1)
lem.grid(row=7,column=0)

tb=StringVar()
tb.set(lst[5])
lem=Label(tk,textvariable=tb)
lem.grid(row=7,column=1,columnspan=2)

b=Button(tk,text="UPDATE",command=getfun)
b.grid(row=8,column=0,columnspan=2)

#creating two threads one for tkinter and other for dispensing
start_new_thread(compar,())
tk.mainloop()

