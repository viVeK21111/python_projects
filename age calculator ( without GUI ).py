print("""
                     **** AGE CALCULATOR ****             """)
print()
print()
g=input("Enter your gender (m/f): ")
print()
n=input("Enter your name: ")
print()
from datetime import date
import calendar as cal
today=date.today()
pd=(today.day)
pm=(today.month)
py=(today.year)
yy=int(input("Enter your birht year: "))
mm=int(input("Enter your birth month: "))
dd=int(input("Enter your birth date: "))
print()
if(mm>12 or dd>31):
    print('you have entered wrong input')
else:
    if(py-yy<=-1):
        print("You are not born yet, please contact your representatives for that")
    if(py-yy==0 and pm-mm==0 and pd>dd):
        print("you are an infant, age is just {} days".format(pd-dd))
    if(py-yy==0 and pm-mm==0 and pd<dd):
        print("You are not born yet, please contact your representatives for that")
    if(py-yy==0 and pm-mm==1 and pd<dd):
        print('your age is just {}'.format(30-(dd-pd)))
    if(py-yy==0 and pm-mm==1 and pd>dd):
        print("your age is just {} month and {} days".format(1,pd-dd))
    if(py-yy==0 and pm-mm>1 and pd<dd):
        print('your age is just {} months and {} days'.format((pm-mm)-1,30-(dd-pd)))
    if(py-yy==0 and pm-mm>1 and pd>dd):
        print('your age is just {} months and {} days'.format(pm-mm,pd-dd))
    if(py-yy==0 and pm-mm==0 and pd==dd):
        print("you just born today!")
    if(pd==dd and pm-mm==0 and py-yy>1):
        print(""" 
                    **** Cheers! It's your birthday  *** """)
        gift=input("you want any gift? Enter yes/no: ")
        if(gift=='yes'):
            print("sorry, i've no gifts for you but i'll calculate your exact age: ")
        if(gift=='no'):
            print("it's ok, check out your age here: ")
        
    if(py-yy>=1):
        i=input("Enter 'f' to get full age    OR     Enter 's' to get age in years,months and days:  ")
        print()
        ydiff=py-yy
        if(pm>mm and py-yy==1):
            ydiff=1
        ly=cal.leapdays(2003, 2022)
        ddiff=(365*ydiff)+ly
        mdiff=12*ydiff
        if(i=='s'):
            if(pm==mm and pd==dd):
                days=0
            if(pm==mm and pd<dd):
                ydiff+=-1
                days=30-(dd-pd)
                mdiff+=-1
                ddiff-=dd-pd
            if(pm==mm and pd>dd):
                days=pd-dd
                ddiff+=pd-dd
            if(pm-mm==1 and pd<dd):
                days=30-(dd-pd)
                ddiff+=(30-(dd-pd))+(pm-mm-1)*30
                mdiff+=0
            if(pm-mm>1 and pd<dd):
                days=30-(dd-pd)
                mdiff+=(pm-mm-1)
                ddiff+=((pm-mm-1)*30)+(30-(dd-pd))
            if(pm>mm and pd>dd):
                days=pd-dd
                mdiff+=(pm-mm)
                ddiff+=(pd-dd)*30
            if(pm>mm and pd==dd):
                days=0
                mdiff+=(pm-mm)
                ddiff+=(pm-mm)*30
            if(pm<mm and pd==dd):
                days=0
                mdiff-=(mm-pm)
                ddiff-+(mm-pm)*30
                ydiff+=-1
            if(pm<mm and pd>dd):
                days=30-(pd-dd)
                mdiff-=(mm-pm-1)
                ddiff-=(mm-pm-1)*30+(pd-dd)
                ydiff+=-1
            if(mm-pm==1 and pd>dd):
                days=pd-dd
                mdiff+=-1
                ddiff=(ddiff-30)+(pd-dd)
            if(pm<mm and pd<dd):
                days=30-(dd-pd)
                ydiff+=-1
                mdiff-=(mm-pm-1)
                ddiff-=(((mm-pm)*30)+(dd-pd))
            if(g=='m'):
                print(""" Mr.{} your age is {} years or {} months,{} days  or {} days""".format(n,ydiff,mdiff,days,ddiff))
            if(g=='f'):
                print(""" Ms.{} your age is {} years or {} months,{} days  or {} days""".format(n,ydiff,mdiff,days,ddiff))
            
        if(i=='f'):
            if(pm==mm and pd==dd):
                mdiff1=0
                ddiff1=0
            if(pm==mm and pd<dd):
                ydiff+=-1
                mdiff1=11
                ddiff1=30-(dd-pd)
            if(pm==mm and pd>dd):
                mdiff1=0
                ddiff1=pd-dd
            if(pm>mm and pm-mm==1 and pd<dd):
                mdiff1=0
                ddiff1=30-(dd-pd)
            if(pm>mm and pm-mm==1 and pd==dd):
                mdiff1=1
                ddiff1=0
            if(pm>mm and pm-mm==1 and pd>dd):
                mdiff1=1
                ddiff1=pd-dd
            if(pm>mm and pm-mm>1 and pd<dd):
                mdiff1=pm-mm-1
                ddiff1=30-(dd-pd)
            if(pm>mm and pm-mm>1 and pd>dd):
                mdiff1=pm-mm
                ddiff1=pd-dd
            if(pm<mm and pd>dd):
                mdiff1=12-(mm-pm)
                ddiff1=30-(pd-dd)
                ydiff+=-1
            if(pm<mm and pd<dd):
                mdiff1=11-(mm-pm)
                ddiff1=30-(dd-pd)
                ydiff+=-1
            if(g=='m'):
                print("Congrats! Mr.{} you have completed {} years {} months and {} days of your life".format(n,ydiff,mdiff1,ddiff1))
            if(g=='f'):
                print("Bravo! Ms.{} you have completed {} years {} months and {} days of your life".format(n,ydiff,mdiff1,ddiff1))
            print()
            if(ydiff>=100):
                print("And i wonder how you're still alive")


print()
print()
print()
print()
print()
print()
print()
print()
print()
int(input('Press Enter key to exit Age calculator '))   

        
    
    

    
    
    
    

