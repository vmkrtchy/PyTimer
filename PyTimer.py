import time
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as tk

t_timer = Tk()
t_timer.geometry("500x500")
t_timer.title("Countdown Timer")
t_timer.configure(background='orange')
t_timer.resizable(False,False)

Label(t_timer, text="Correct Time",bg="orange", font=("Arial", 25)).place(x = 95, y=105)
def clock():
	clock_time = time.strftime('%H: %M: %S %p')
	corrent_time.config(text=clock_time)
	corrent_time.after(1000,clock)

corrent_time = Label(t_timer,text="", bg="orange",font=("Arial", 25))
corrent_time.place(x=270,y=105)
clock()


h_String = StringVar()
m_String = StringVar()
s_String = StringVar()


h_String.set("00")
m_String.set("00")
s_String.set("00")


h_box = Entry(t_timer, width=3, font=("Calibri", 20, ""), textvariable=h_String)
m_box = Entry(t_timer, width=3, font=("Calibri", 20, ""), textvariable=m_String)
s_box = Entry(t_timer, width=3, font=("Calibri", 20, ""), textvariable=s_String)


h_box.place(x=170, y=180)
m_box.place(x=220, y=180)
s_box.place(x=270, y=180)

def Start():
    try:
        clockTime = int(h_String.get()) * 3600 + int(m_String.get()) * 60 + int(s_String.get())
    except:
        print("Incorrect values")

    while (clockTime > -1):

        totalMinutes, totalSeconds = divmod(clockTime, 60)

        totalHours = 0
        if (totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)

        h_String.set("{0:2d}".format(totalHours))
        m_String.set("{0:2d}".format(totalMinutes))
        s_String.set("{0:2d}".format(totalSeconds))

        t_timer.update()
        time.sleep(1)

        if (clockTime == 0):
            messagebox.showinfo("", "Finished")

        clockTime -= 1



image = PhotoImage(file='start.png')
button = Button(t_timer,image=image,command=Start,border=0,bg='#FFA500',activebackground='#FFA500')
button.place(relx=0.5, rely=0.5, anchor=CENTER)
t_timer.mainloop()
