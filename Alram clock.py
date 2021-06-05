# Import all the needed library.

from tkinter import *
import datetime
import time


def alram(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H , %M , %S")
        date = current_time.strftime("%d , %m , %y")
        print("The set date is:",date)
        print(now)
        if now == set_timer_now:
            print("Time to wake up bro")
        break

def actual_time():
    set_alarm_timer = f"{Hour.get()}:{Min.get()}:{Sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title(" #Randomchirag Alarm clock ")
clock.geometry("400x200")
time_format=Label(clock, text = " Enter Time In 24 Hours Format !",fg="red" , bg="black" , font="Arial").place(x=70,y=150)
addTime = Label(clock,text = " Hour        Min        Sec" , font=60).place(x=110)
set_your_alarm = Label(clock,text = " Enter Time  " , fg="black",relief="solid" , font=("Helventica",20,"bold")).place(x=0 , y=29)

# The veriable use to set the alram clock .
Hour = StringVar()
Min = StringVar()
Sec = StringVar()

# time required to set the alaram clock .
hourtime = Entry(clock,textvariable =  Hour , bg="pink",width =15).place(x= 100 , y= 30)
mintime  =  Entry(clock,textvariable = Min , bg="pink",width =15).place(x= 130 , y= 30)
sectime  =  Entry(clock,textvariable = Sec , bg="pink",width =15).place(x= 160, y= 30)

# To take the time input from user .
submit = Button(clock,text='Set Alarm' , fg="red" , width = 10 ,command = actual_time).place(x=110 , y =70)
clock.mainloop()
