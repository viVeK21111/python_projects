from tkinter import *
from tkinter import ttk
nws=Tk()
nws.geometry('500x500')

l1=Label(nws,text='CURRENCY CONVERTER',font='bold',bg='sky blue',fg='black')
l2=Label(nws,text=' ',font='bold')
l3=Label(nws,text='select your currency: ',font='bold')
cb=ttk.Combobox(nws,values=['USD','EUR','Rupee (₹)','AUD (Australian dollar)',
                            'CAD (canadian dollar)','SGD (Singapore dollar)',
                            'MXN (mexican peso)','THB (Thai bhat)'])
cb1=ttk.Combobox(nws,values=['USD','EUR','Rupee (₹)','AUD (Australian dollar)',
                            'CAD (canadian dollar)','SGD (Singapore dollar)',
                            'MXN (mexican peso)','THB (Thai bhat)'])
cb.current(0)
cb1.current(0)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
cb.grid(row=3,column=0) 

l5=Label(nws,text='Select foreign currency: ',font='bold')
l4=Label(nws,text=' ',font='bold')
l4.grid(row=4,column=0)
l5.grid(row=5,column=0)
cb1.grid(row=6,column=0)

def b():
    mc=cb.get()
    fc=cb1.get()
    amo=h.get()
    print(mc,fc)
    print(amo,end='   ')
    if(mc==fc):
        t1=amo
    flag=0
    if(mc!=fc):
        if((fc=='USD' and mc=='Rupee (₹)') or (fc=='Rupee (₹)' and mc=='USD')): 
            if(fc=='Rupee (₹)' and mc=='USD'):
                t1=float(amo)*79.47
            else:
                t1=float(amo)/79.47
        if((fc=='USD' and mc=='EUR') or (fc=='EUR' and mc=='USD')): 
            if(fc=='EUR' and mc=='USD'):
                t1=float(amo)*0.99
            else:
                t1=float(amo)/0.99
        if((fc=='USD' and mc=='AUD (Australian dollar)') or (fc=='AUD (Australian dollar)' and mc=='USD')):
            if(mc=='USD' and fc=='AUD (Australian dollar)'):
                t1=float(amo)*1.48
            else:
                t1=float(amo)/1.48
        if((fc=='USD' and mc=='CAD (canadian dollar)') or (fc=='CAD (canadian dollar)' and mc=='USD')):
            if(mc=='USD' and fc=='CAD (canadian dollar)'):
                t1=float(amo)*1.30
            else:
                t1=float(amo)/1.30
        if((fc=='USD' and mc=='SGD (Singapore dollar)') or (fc=='SGD (Singapore dollar)' and mc=='USD')):
            if(mc=='USD' and fc=='SGD (Singapore dollar)'):
                t1=float(amo)*1.40
            else:
                t1=float(amo)/1.40
        if((mc=='USD' and fc=='MXN (mexican peso)') or (fc=='MXN (mexican peso)' and mc=='USD')):
            if(mc=='USD' and fc=='MXN (mexican peso)'):
                t1=float(amo)*20.70
            else:
                t1=float(amo)/20.70
        if((fc=='USD' and mc=='THB (Thai bhat)') or (fc=='THB (Thai bhat)' and mc=='USD')):
            if(mc=='USD' and fc=='THB (Thai bhat)'):
                t1=float(amo)*36.24
            else:
                t1=float(amo)/36.24
        if((fc=='AUD (Australian dollar)' and mc== 'EUR') or (fc=='EUR' and mc=='AUD (Australian dollar)')): 
            if(fc=='AUD (Australian dollar)' and mc=='EUR'):
                t1=float(amo)*1.49
            else:
                t1=float(amo)/1.49
        if((fc=='Rupee (₹)' and mc== 'EUR') or (fc=='EUR' and mc=='Rupee (₹)')): 
            if(fc=='Rupee (₹)' and mc=='EUR'):
                t1=float(amo)*79.98
            else:
                t1=float(amo)/79.98
        if((fc=='CAD (canadian dollar)' and mc== 'EUR') or (fc=='EUR' and mc=='CAD (canadian dollar)')): 
            if(fc=='CAD (canadian dollar)' and mc=='EUR'):
                t1=float(amo)*1.31
            else:
                t1=float(amo)/1.31
        if((fc=='SGD (Singapore dollar)' and mc== 'EUR') or (fc=='EUR' and mc=='SGD (Singapore dollar)')): 
            if(fc=='SGD (Singapore dollar)' and mc=='EUR'):
                t1=float(amo)*1.42
            else:
                t1=float(amo)/1.42
        if((fc=='MXN (mexican peso)' and mc== 'EUR') or (fc=='EUR' and mc=='MXN (mexican peso)')): 
            if(fc=='MXN (mexican peso)' and mc=='EUR'):
                t1=float(amo)*20.89
            else:
                t1=float(amo)/20.89
        if((fc=='THB (Thai bhat)' and mc== 'EUR') or (fc=='EUR' and mc=='THB (Thai bhat)')): 
            if(fc=='THB (Thai bhat)'and mc=='EUR'):
                t1=float(amo)*36.44
            else:
                t1=float(amo)/36.44
        if((fc=='AUD (Australian dollar)'and mc=='Rupee (₹)') or (fc=='Rupee (₹)' and mc=='AUD (Australian dollar)')): 
            if(fc=='AUD (Australian dollar)' and mc=='Rupee (₹)'):
                t1=float(amo)*0.02
            else:
                t1=float(amo)/0.02
        if((fc=='CAD (canadian dollar)'and mc=='Rupee (₹)') or (fc=='Rupee (₹)' and mc=='CAD (canadian dollar)')): 
            if(fc=='CAD (canadian dollar)' and mc=='Rupee (₹)'):
                t1=float(amo)*0.02
            else:
                t1=float(amo)/0.02
        if((fc=='SGD (Singapore dollar)'and mc=='Rupee (₹)') or (fc=='Rupee (₹)' and mc=='SGD (Singapore dollar)')): 
            if(fc=='SGD (Singapore dollar)' and mc=='Rupee (₹)'):
                t1=float(amo)*0.02
            else:
                t1=float(amo)/0.02
        if((fc=='MXN (mexican peso)'and mc=='Rupee (₹)') or (fc=='Rupee (₹)' and mc=='MXN (mexican peso)')): 
            if(fc=='MXN (mexican peso)' and mc=='Rupee (₹)'):
                t1=float(amo)*0.26
            else:
                t1=float(amo)/0.26
        if((fc=='THB (Thai bhat)'and mc=='Rupee (₹)') or (fc=='Rupee (₹)' and mc=='THB (Thai bhat)')): 
            if(fc=='THB (Thai bhat)' and mc=='Rupee (₹)'):
                t1=float(amo)*0.46
            else:
                t1=float(amo)/0.46
        if((fc=='CAD (canadian dollar)'and mc=='AUD (Australian dollar)') or (fc=='AUD (Australian dollar)' and mc=='CAD (canadian dollar)')): 
            if(fc=='CAD (canadian dollar)' and mc=='AUD (Australian dollar)'):
                t1=float(amo)*0.88
            else:
                t1=float(amo)/0.88
        if((fc=='SGD (Singapore dollar)'and mc=='AUD (Australian dollar)') or (fc=='AUD (Australian dollar)' and mc=='SGD (Singapore dollar)')): 
            if(fc=='SGD (Singapore dollar)' and mc=='AUD (Australian dollar)'):
                t1=float(amo)*0.95
            else:
                t1=float(amo)/0.95
        if((fc=='MXN (mexican peso)'and mc=='AUD (Australian dollar)') or (fc=='AUD (Australian dollar)' and mc=='MXN (mexican peso)')): 
            if(fc=='MXN (mexican peso)' and mc=='AUD (Australian dollar)'):
                t1=float(amo)*14.05
            else:
                t1=float(amo)/14.05
        if((fc=='THB (Thai bhat)'and mc=='AUD (Australian dollar)') or (fc=='AUD (Australian dollar)' and mc=='THB (Thai bhat)')): 
            if(fc=='THB (Thai bhat)' and mc=='AUD (Australian dollar)'):
                t1=float(amo)*24.51
            else:
                t1=float(amo)/24.51
        if((fc=='SGD (Singapore dollar)'and mc=='CAD (canadian dollar)') or (fc=='CAD (canadian dollar)' and mc=='SGD (Singapore dollar)')): 
            if(fc=='SGD (Singapore dollar)'and mc=='CAD (canadian dollar)'):
                t1=float(amo)*1.08
            else:
                t1=float(amo)/1.08
        if((fc=='MXN (mexican peso)'and mc=='CAD (canadian dollar)') or (fc=='CAD (canadian dollar)' and mc=='MXN (mexican peso)')): 
            if(fc=='MXN (mexican peso)'and mc=='CAD (canadian dollar)'):
                t1=float(amo)*15.96
            else:
                t1=float(amo)/15.96
        if((fc=='THB (Thai bhat)'and mc=='CAD (canadian dollar)') or (fc=='CAD (canadian dollar)' and mc=='THB (Thai bhat)')): 
            if(fc=='THB (Thai bhat)'and mc=='CAD (canadian dollar)'):
                t1=float(amo)*27.83
            else:
                t1=float(amo)/27.83
        if((fc=='MXN (mexican peso)'and mc=='SGD (Singapore dollar)') or (fc=='SGD (Singapore dollar)' and mc=='MXN (mexican peso)')): 
            if(fc=='MXN (mexican peso)'and mc=='SGD (Singapore dollar)'):
                t1=float(amo)*14.76
            else:
                t1=float(amo)/14.76
        if((fc=='THB (Thai bhat)'and mc=='SGD (Singapore dollar)') or (fc=='SGD (Singapore dollar)' and mc=='THB (Thai bhat)')): 
            if(fc=='THB (Thai bhat)'and mc=='SGD (Singapore dollar)'):
                t1=float(amo)*25.74
            else:
                t1=float(amo)/25.74
        if((fc=='THB (Thai bhat)'and mc=='MXN (mexican peso)') or (fc=='MXN (mexican peso)' and mc=='THB (Thai bhat)')): 
            if(fc=='THB (Thai bhat)'and mc=='MXN (mexican peso)'):
                t1=float(amo)*1.74
            else:
                t1=float(amo)/1.74
        
    print(t1)   
    nwr=Tk()
    nwr.geometry('400x400')
    l=Label(nwr,text='After converting, the amount is {}'.format(t1),font='bold',bg='grey')
    l.place(x=5,y=5)
    def bc():
        nwr.destroy()
    icb=Button(nwr,text='Close',height=1,width=8,command=bc,bg='grey')
    icb.place(x=10,y=80)
    sl=Label(nwr,text='Note :',fg='red')
    sl.place(x=3,y=150)
    sl=Label(nwr,text='The converted amount is being displayed in foreign currency.',fg='black')
    sl.place(x=37,y=150)
    
    nwr.mainloop() 
    

la=Label(text='Enter amount in your currency: ',font='bold')
a=int()
h=Entry(nws,width=30,textvariable=a) 
l6=Label(nws,text=' ',font='bold')
l6.grid(row=7,column=0)
la.grid(row=8,column=0)
h.grid(row=8,column=1)

sb=Button(nws,height=2,width=9,text='Submit',command=b,bg='grey',activebackground='navy blue') 
l7=Label(nws,text=' ',font='bold')
l7.grid(row=9,column=0)
sb.grid(row=10,column=0)

def bc():
    nws.destroy()
icb=Button(nws,text='Close this window',height=2,width=15,command=bc,bg='grey',activebackground='indigo')
sl=Label(nws,text=' ')
sl.grid(row=11,column=0)
# sl=Label(nws,text=' ',font='bold')
# sl.grid(row=12,column=0)
sl=Label(nws,text=' ')
sl.grid(row=12,column=0)
icb.grid(row=13,column=1)
sl=Label(nws,text=' ')
sl.grid(row=14,column=0)
sl=Label(nws,text="""Note : The above-listed currencies are 
                the only major trading currencies.""",fg='navy blue')
s2=Label(nws,text='Currency values taken on date: 14-07-2022',fg='Black')
sl.grid(row=15,column=0)
s2.grid(row=16,column=0)
nws.mainloop()  


