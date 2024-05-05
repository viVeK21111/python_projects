import datetime
import time
import winsound
from datetime import date
from datetime import time
from datetime import datetime


print("""                    
                           ***** Alarm clock  ****            """)
print()
n=datetime.now()
ala=input("Enter yes/no to set an alarm today: ")
ct=0
def today():
    h=int(input('Enter hours (24 hour fomrat): '))
    m=int(input("Enter minute: "))
    print()
    flag=0
    if(h>23 or m>59 or m<0 or h<0):
        print("you've eneterd wrong input")
        print()
        flag=1
    def funct(h,m):
        if(h==n.hour and m==n.minute):
            print("Alarm is ringing....")
            print("But i didn't imported the sound yet 🤣")
            flag=3
        if(h>n.hour and m>n.minute):
            print("Alamr will ring in {} hours {} minutes".format(h-n.hour,m-n.minute))
            flag=3
        #if(h-n.hour==1 and m<n.minute):
          #  print('your alarm will ring in 0 hours and {} minutes'.format(60-(n.minute-m)))
        if(h>n.hour and m<n.minute):
            print("your alarm will ring in {} hours and {} minutes".format((h-1)-n.hour,60-(n.minute-m)))
            flag=3
        if(h==n.hour and m<n.minute):
            print("you can't set an alarm at this time for today")
            flag=3
        if(h==n.hour and m>n.minute):
            print('Alarm will ring in {} minutes'.format(m-n.minute)) 
            flag=3
        if(h>n.hour and m==n.minute):
            print('Alarm will ring in {} hours and 0 minutes'.format(h-n.hour))
            flag=3
        if(h<n.hour):
            print("you can't set an alarm at this time for today")  
            flag=3
    if(flag==0):
        funct(h,m)
    if(flag==1):
        today()
        #funct(h,m)
    if(flag==3):
        ct=1

if(ct==0):
    if ala=='yes':
        today()
     
if ala=='no':
    wd=n.isoweekday()  
    day=input('Enter the day, example: monday  : ')
    while(1):
        if(day=='monday' or day=='Monday'):
            dayn=1
            break
        if(day=='tuesday' or day=='Tuesday'):
            dayn=2
            break
        if(day=='wednesday' or day=='Wednesday'):
            dayn=3
            break
        if(day=='thursday' or day=='Thursday'):
            dayn=4
            break
        if(day=='friday' or day=='Friday'):
            dayn=5
            break
        if(day=='sataurday' or day=='Sataurday'):
            dayn=6
            break
        if(day=='sunday' or day=='Sunday'):
            dayn=7
            break
    def func(dayn,wd,n,days):
        time=list(map(int,input('Enter time in 24 hour format %H %M (H-hour,M-minute): ').split()))
        if(time[0]>n.hour and time[1]>=n.minute):
            hours=time[0]-n.hour
            minutes=time[1]-n.minute
        if(time[0]<n.hour and time[1]>=n.minute):
            days+=-1
            hours=24-(n.hour-time[0])
            minutes=time[1]-n.minute
        if(time[0]<n.hour and time[1]<n.minute):
            days+=-1
            hours=(24-(n.hour-time[0]))-1
            minutes=60-(n.minute-time[1])
        if(time[0]>n.hour and time[1]<n.minute):
            hours=(time[0]-n.hour)-1
            minutes=60-(n.minute-time[1]) 
        if(time[0]==n.hour and time[1]==n.minute):
            hours=0
            minutes=0
        if(time[0]==n.hour and time[1]<n.minute):
            days+=-1
            hours=23
            minutes=60-(n.minute-time[1])
        if(time[0]==n.hour and time[1]>n.minute):
            hours=0
            minutes=time[1]-n.minute
            
        print()
        print('Alarm set for {} days {} hours and {} minutes from now'.format(days,hours,minutes)) 
    if(dayn>wd):
        days=(dayn-wd)
        func(dayn,wd,n,days)
    if(dayn<wd):
        days=7-(wd-dayn)
        func(dayn,wd,n,days)
    if(dayn==wd):
        today()
input()
    









    
