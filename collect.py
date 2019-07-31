#importing necessary modules
from tkinter import *
import time

#creating gui outlines
tk=Tk()
tk.title("MEDIBOX")
tk.geometry("475x350")


#function to store user input data in text format
def getfun():
        if(ev1.get()=="choose" or ev2.get()=="choose" or ev3.get()=="choose" or ev4.get()=="choose" or ev5.get()=="choose" or ev6.get()=="choose" or ev7.get()=="choose" or ev8.get()=="choose" or ev9.get()=="choose" or ev10.get()=="choose" or ev11.get()=="choose" or ev12.get()=="choose"):
                err=StringVar()
                err.set("Please choose all the options!")
                lb=Label(tk,textvariable=err)
                lb.grid(row=9,column=0,columnspan=3)
        else:
                with open("data.txt",'w') as file:
                        file.write(ev1.get()+" "+ev3.get()+"\n")
                        file.write(ev2.get()+" "+ev4.get()+"\n")

                        file.write(ev5.get()+" "+ev7.get()+"\n")
                        file.write(ev6.get()+" "+ev8.get()+"\n")

                        file.write(ev9.get()+" "+ev11.get()+"\n")
                        file.write(ev10.get()+" "+ev12.get())
                
                exit()

#creating gui for user input
mes=StringVar()
mes.set("PLEASE ENTER PILL DETAILS")
l1=Label(tk,textvariable = mes)
l1.grid(row=0,column=0,columnspan=2)

pill1=StringVar()
pill1.set("PILL 1")
lem=Label(tk,textvariable=pill1)
lem.grid(row=1,column=1)

pill2=StringVar()
pill2.set("PILL 2")
lem=Label(tk,textvariable=pill2)
lem.grid(row=1,column=2)


#morning

quantity=StringVar()
quantity.set("QUANTITY:")
l2=Label(tk,textvariable= quantity)
l2.grid(row=2,column=0)

ev1=StringVar()
ev1.set("choose")
e1=OptionMenu(tk,ev1,"0","1","2","3","4","5")
e1.grid(row=2,column=1)

ev2=StringVar()
ev2.set("choose")
e2=OptionMenu(tk,ev2,"0","1","2","3","4","5")
e2.grid(row=2,column=2)

disp=StringVar()
disp.set("Morning")
l2=Label(tk,textvariable= disp)
l2.grid(row=2,column=3)

tim=StringVar()
tim.set("TIME:")
l3=Label(tk,textvariable= tim)
l3.grid(row=3,column=0)

ev3=StringVar()
ev3.set("choose")
e3=OptionMenu(tk,ev3,"07:00","08:00","09:00","10:00","11:00")
e3.grid(row=3,column=1)

ev4=StringVar()
ev4.set("choose")
e4=OptionMenu(tk,ev4,"07:00","08:00","09:00","10:00","11:00")
e4.grid(row=3,column=2)

#afternoon

quantity=StringVar()
quantity.set("QUANTITY:")
l2=Label(tk,textvariable= quantity)
l2.grid(row=4,column=0)

ev5=StringVar()
ev5.set("choose")
e5=OptionMenu(tk,ev5,"0","1","2","3","4","5")
e5.grid(row=4,column=1)

ev6=StringVar()
ev6.set("choose")
e6=OptionMenu(tk,ev6,"0","1","2","3","4","5")
e6.grid(row=4,column=2)

disp=StringVar()
disp.set("Afternoon")
l2=Label(tk,textvariable= disp)
l2.grid(row=4,column=3)

tim=StringVar()
tim.set("TIME:")
l3=Label(tk,textvariable= tim)
l3.grid(row=5,column=0)

ev7=StringVar()
ev7.set("choose")
e7=OptionMenu(tk,ev7,"12:00","13:00","14:00","15:00")
e7.grid(row=5,column=1)

ev8=StringVar()
ev8.set("choose")
e8=OptionMenu(tk,ev8,"12:00","13:00","14:00","15:00")
e8.grid(row=5,column=2)

#night

quantity=StringVar()
quantity.set("QUANTITY:")
l2=Label(tk,textvariable= quantity)
l2.grid(row=6,column=0)

ev9=StringVar()
ev9.set("choose")
e9=OptionMenu(tk,ev9,"0","1","2","3","4","5")
e9.grid(row=6,column=1)

ev10=StringVar()
ev10.set("choose")
e10=OptionMenu(tk,ev10,"0","1","2","3","4","5")
e10.grid(row=6,column=2)

disp=StringVar()
disp.set("Night")
l2=Label(tk,textvariable= disp)
l2.grid(row=6,column=3)

tim=StringVar()
tim.set("TIME:")
l3=Label(tk,textvariable= tim)
l3.grid(row=7,column=0)

ev11=StringVar()
ev11.set("choose")
e11=OptionMenu(tk,ev11,"17:00","18:00","19:00","20:00","21:00","22:00")
e11.grid(row=7,column=1)

ev12=StringVar()
ev12.set("choose")
e12=OptionMenu(tk,ev12,"17:00","18:00","19:00","20:00","21:00","22:00")
e12.grid(row=7,column=2)

b=Button(tk,text="UPDATE",command=getfun)
b.grid(row=8,column=1)
tk.mainloop()
