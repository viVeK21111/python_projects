from tkinter import *
import tkinter as tk
import time
from tkinter import messagebox
from datetime import datetime
import winsound
nww=Tk()
nww.geometry('600x600')
nww.config(bg='floral white')
l=Label(nww,text='ALARM CLOCK',height=2,width=15,bg='#0059b3',font='bold')
l.pack()
iw=Canvas(nww,height=60,width=700)
iw.pack()
iw.create_text(180,50,text='Click on yes/no to set an alarm today: ',fill='black',font='bold')

def yesbut():
    y1=190
    iw2=Canvas(nww,height=100,width=700)
    iw2.pack()
    iw2.create_text(150,80,text='Enter time in Hours and minutes: ',fill='black',font='bold')
    global h
    global m
    h=StringVar()
    m=StringVar()
    h.set('00')
    m.set('00')
    hentry=Entry(nww,width=5,textvariable=h)
    hentry.place(x=320,y=190)
    mentry=Entry(nww,width=5,textvariable=m)
    mentry.place(x=360,y=190) 
    yesb=Button(nww,text='Submit',bg='grey',height=2,width=10,activebackground='indigo',command=submit)
    yesb.place(x=70,y=250)
    y1+=60
def submit():
    global ho
    global minu
    n=datetime.now()
    ho=int(h.get())
    minu=int(m.get())
    global flag
    flag=0
    if(ho>23 or minu>59 or minu<0 or ho<0):
        flag=1
    def funct(ho,minu):
        global flag1
        flag1=0
        global p
        if(ho==n.hour and minu==n.minute):
            p="Alarm is ringing...."
            flag1=3
        if(ho>n.hour and minu>n.minute):
            p="Alamr will ring in {} hours {} minutes".format(ho-(n.hour),minu-(n.minute))
            flag1=3
        if(ho>n.hour and minu<n.minute):
            p="Alarm will ring in {} hours and {} minutes".format((ho-1)-n.hour,60-(n.minute-minu))
            flag1=3
        if(ho==n.hour and minu<n.minute):
            p="Can't set an alarm at this time for today"
            flag1=3
        if(ho==n.hour and minu>n.minute):
            p='Alarm will ring in {} minutes'.format(minu-(n.minute))
            flag1=3
        if(ho>n.hour and minu==n.minute):
            p='Alarm will ring in {} hours and 0 minutes'.format(ho-(n.hour))
            flag1=3
        if(ho<n.hour):
            p="Can't set an alarm at this time for today"
            flag1=3
    if(flag==0):
        funct(ho,minu)
        nw0=Tk()
        nw0.geometry('400x400')
        iw4=Canvas(nw0,height=50,width=730)
        iw4.create_text(180,30,text=p,fill='black',font='bold') 
        iw4.pack()
        iw4.place(x=20,y=100) 
        def cb():
            nw0.destroy()
        cb=Button(nw0,height=3,width=30,bg='grey',text='please close this window',command=cb) 
        cb.pack()
        cb.place(x=20,y=200) 
        nww.destroy()
        nw0.mainloop()
        # iw5=Canvas(nw0,height=50,width=700)
        # iw5.create_text(160,30,text='Alarm is ringing',fill='black',font='bold') 
        # iw5.pack()
        # iw5.place(x=0,y=100)
        while(1):
            n=datetime.now()
            if(n.hour==ho and n.minute==minu):
                for i in range(1):
                    winsound.Beep(800,200) 
                break
    
    if(flag==1):
        nw9=Tk()
        iw3=Canvas(nw9,height=50,width=700)
        iw3.create_text(160,300,text="Can't set an alarm at this time for today",fill='black',font='bold') 
        iw3.pack()
        iw3.place(x=20,y=150)  
    
def nobut():
    def cb1():
         nw3.destroy() 
         nw8=Tk()
         nw8.geometry('400x400')
         iw6=Canvas(nw8,height=100,width=700)
         iw6.pack()
         iw6.create_text(150,80,text='Enter time in Hours and minutes: ',fill='black',font='bold')
         global h1
         global m1
         h1=StringVar()
         m1=StringVar()
         h1.set('00')
         m1.set('00')
         hentry=Entry(nw8,width=5,textvariable=h1)
         hentry.place(x=30,y=100)
         mentry=Entry(nw8,width=5,textvariable=m1)
         mentry.place(x=60,y=100)
         def cb2():
             global ho1
             global minu1
             ho1=int(h1.get())
             minu1=int(m1.get())
             nw8.destroy()
         cb8=Button(nw8,height=2,width=30,bg='grey',text='Submit',command=cb2)
         cb8.pack()
         cb8.place(x=30,y=250)
         nw8.mainloop()
    nww.destroy()
    nw3=Tk()
    nw3.geometry('500x500') 
      
    cm=BooleanVar()
    b1=Checkbutton(nw3,text='{}'.format('monday'), var=cm). grid(row=0,column=0)

    ct=BooleanVar()
    b2=Checkbutton(nw3,text='Tuesday',  var=ct). grid(row=1,column=0) 

    cw=BooleanVar()
    b3=Checkbutton(nw3,text='Wednesday', var=cw). grid(row=2,column=0)

    cth=BooleanVar()
    b4=Checkbutton(nw3,text='Thursday ', var=cth).grid(row=3,column=0)
    
    cf=BooleanVar()
    b5=Checkbutton(nw3,text='Friday ', var=cf). grid(row=4,column=0)

    csa=BooleanVar()
    b6=Checkbutton(nw3,text='Sataurday',var=csa).grid(row=5,column=0)
    
    cs=BooleanVar()
    b7=Checkbutton(nw3,text='Sunday   ',var=cs). grid(row=6,column=0)
    
    cb3=Button(nw3,height=2,width=30,bg='grey',text='Submit',command=cb1) 
    cb3.grid(row=7,column=1) 
    
    
    nw3.mainloop()           
    
    if(cm.get()==True):
        dayn=1
    if(ct.get()==True):
        dayn=2
    if(cw.get()==True):
        dayn=3
    if(cth.get()==True):
        dayn=4
    if(cf.get()==True):
        dayn=5
    if(csa.get()==True):
        dayn=6
    if(cs.get()==True):
        dayn=7
    n1=datetime.now()  
    wd=n1.isoweekday()
    if(dayn>wd):
        days=(dayn-wd)
    if(dayn<wd):
        days=7-(wd-dayn)
    if(dayn==wd):
        days=7 
    if(ho1>n1.hour and minu1>=n1.minute):
        hours=ho-n.hour
        minutes=minu-n.minute
    if(ho1<n1.hour and minu1>=n1.minute):
        days+=-1
        hours=24-(n1.hour-ho1)
        minutes=minu1-n1.minute
    if(ho1<n1.hour and minu1<n1.minute): 
        days+=-1
        hours=(24-(n1.hour-ho1))-1
        minutes=60-(n1.minute-minu1)
    if(ho1>n1.hour and minu1<n1.minute):
        hours=(ho1-n1.hour)-1
        minutes=60-(n1.minute-minu1) 
    if(ho1==n1.hour and minu1==n1.minute):
        hours=0
        minutes=0
    if(ho1==n1.hour and minu1<n1.minute):
        days+=-1
        hours=23
        minutes=60-(n1.minute-minu1)
    if(ho1==n1.hour and minu1>n1.minute):
        hours=0
        minutes=minu1-n1.minute 
    t="Alarm set for {} days {} hours and {} minutes from now".format(days,hours,minutes)
    nw5=Tk()
    nw5.geometry('500x400')
    iw5=Canvas(nw5,height=100,width=740,bg='#0059b3') 
    iw5.create_text(240,50,text=t,fill='black',font='bold')  
    iw5.pack() 
    iw5.place(x=0,y=100) 
    nw5.mainloop() 
    ad=days+n1.day
    while(1):
        n1=datetime.now()
        if(n1.day==ad and ho==n.hour and minu==n.minute):
            for i in range(1):
                winsound.Beep(800,200) 
            break
        
        
    

yesb=Button(nww,text='Yes',bg='grey',height=2,width=5,command=yesbut) 
yesb.place(x=360,y=80)
nob=Button(nww,text='No',bg='grey',height=2,width=5,command=nobut)
nob.place(x=400,y=80)  
nww.mainloop()


  