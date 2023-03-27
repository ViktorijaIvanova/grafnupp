from math import*
from msvcrt import kbhit
from re import A
from secrets import choice
from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks
from tkinter import*  

def valik():
    num=var.get() 
    lbox.insert(END,num)
    
def lipp():
    var.get()
    if "bahama":
        print(1)
    if "estonia":
        print(2)
    if "austria":
        print(3)
    lbox.insert(END,"bahama")
    lbox.insert(END,"estonia")
    lbox.insert(END,"austria")



aken=Tk()
#LIPUD
raam = Tk()
raam.title("Tahvel")
lbox=Listbox(raam,height=9,width=30)
var=IntVar() #StringVar()

r1=Radiobutton(raam,text="bahama",variable=var,value=1,command=valik)
r2=Radiobutton(raam,text="estonia",variable=var,value=2,command=valik)
r3=Radiobutton(raam,text="avstria",variable=var,value=3,command=valik) 


r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)
tahvel = Canvas(raam, width=600, height=600, background="white")
tahvel.grid()
tahvel.create_rectangle(5,5,  180,45,fill="#4599a1")
tahvel.create_rectangle(5,45,  180,90,fill="yellow")
tahvel.create_rectangle(5,130,  180,90,fill="#4599a1")
tahvel.create_polygon(5,5,  100,60,  5,130,  5,4, width=5,fill="black")

tahvel.create_rectangle(360,5,  180,45,fill="blue")
tahvel.create_rectangle(360,45,  180,90,fill="black")
tahvel.create_rectangle(360,130,  180,90,fill="white") 

tahvel.create_rectangle(900,5,  350,45,fill="red")
tahvel.create_rectangle(900,45,  350,90,fill="white")
tahvel.create_rectangle(900,130,  350,90,fill="red")



#tahvel.create_rectangle(600,5,  180,45,fill="red")
#tahvel.create_rectangle(600,45,  180,90,fill="blue")
#tahvel.create_rectangle(600,130,  180,90,fill="yellow")

#muster

x0=400
y0=400
x1=600
y1=600
a=100
r=(a**2+a**2)**(1/2)
p=(a-r)

for i in range(12):
    x0+=p
    y0+=p
    x1-=p
    y1-=p
    tahvel.create_rectangle(x0,y0,x1,y1,width=1,outline="blue",fill="red")
    tahvel.create_oval(x0,y0,x1,y1,width=1,outline="blue",fill="yellow")
    p=r-a 
    r=r-p 
    a=((r)*sqrt(2))/2
    tahvel.grid()
    
colors=["black",
        "cyan",
        "magenta",
        "red",
        "blue",
        "gray",
        "yellow",
        "green",
        "lightblue",
        "pink",
        "gold"]
raam2=Tk()
raam2.title("ringid")
tahvel2=Canvas(raam2,width=600,height=600,background="white")
x0=0
y0=0
x1=600
y1=600
p=5
for i in range(55):
    x0+=p 
    y0+=p 
    x1-=p 
    y1-=p 
    tahvel2.create_oval(x0,y0,x1,y1,fill=choice(colors))
    tahvel2.grid()
    
"""tahvel.create_rectangle(600,295,  430,145,fill="white")

tahvel.create_rectangle(250,295,  400,145,fill="white")"""



#VALGUSFOOR
#suur_font = font.Font(family='Helvetica', size=32, weight='bold')
#tahvel.create_text(30, 500, text="valgusfoor!", font=suur_font, anchor=NW)

tahvel.create_rectangle(30,750,  200,300,fill="grey")
tahvel.create_rectangle(100,410,  135,375,fill="red")
tahvel.create_rectangle(100,415,  135,450,fill="yellow")
tahvel.create_rectangle(100,455,  135,490,fill="green")
tahvel.create_rectangle(115,650,  120,500,fill="black")
tahvel.create_rectangle(50,600,   180,600,width=4 )

raam.mainloop()

