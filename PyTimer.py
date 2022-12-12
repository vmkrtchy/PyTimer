import time
from tkinter import *
from tkinter import messagebox

t_timer = Tk()
t_timer.geometry("500x500")
t_timer.title("Countdown Timer")
t_timer.configure(background='orange')

h_String = StringVar()
m_String = StringVar()
s_String = StringVar()

### Set strings to default value
h_String.set("00")
m_String.set("00")
s_String.set("00")

### Get user input
h_box = Entry(t_timer, width=3, font=("Calibri", 20, ""), textvariable=h_String)
m_box = Entry(t_timer, width=3, font=("Calibri", 20, ""), textvariable=m_String)
s_box = Entry(t_timer, width=3, font=("Calibri", 20, ""), textvariable=s_String)

### Center textboxes
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

        ### Update the interface
        t_timer.update()
        time.sleep(1)

        ### Let the user know if the timer has expired
        if (clockTime == 0):
            messagebox.showinfo("", "Finished")

        clockTime -= 1


T_Button = Button(t_timer, text='Set Time', bd='5', command=Start)
T_Button.place(relx=0.5, rely=0.5, anchor=CENTER)

### Keep looping
t_timer.mainloop()