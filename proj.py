from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import tkinter as tk
import time
import psutil
import matplotlib.pyplot as plt



def shtdwdn():
    msgbox=messagebox.askquestion('SHUTDOWN','Are you sure you want to turnoff system',icon = 'warning')
    if msgbox=='yes':
        print('shutting down')
        os.system("shutdown /s /t 1 ");
    else:
         messagebox.showinfo('Return','You will now return to the application screen')
     
       
def restart():
    msgbox=messagebox.askquestion('Restart','Are you sure you want to restart system',icon = 'warning')
    if msgbox=='yes':
        print('restarting')
        os.system("shutdown /r /t 1 ");
    else:
         messagebox.showinfo('Return','You will now return to the application screen')
     
       
def tasklist():
    p=os.popen('tasklist')
    l=p.read()
    s=tk.Scrollbar(root)
        
    T=tk.Text(root,width=80,height=60)
    T.place(x=5,y=60)
    s.pack(side=tk.RIGHT, fill=tk.Y)
    s.config(command=T.yview)
    T.config(yscrollcommand=s.set)
    T.insert(tk.END,l)


def sysinfo():
    q=os.popen('systeminfo')
    s=q.read()
    print(q.read())

    messagebox.showinfo("system",s)
    

def sysinfi():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*"),("text files","*.txt")))
    print (root.filename)
    os.system(root.filename)                    



def util():
    plt.rcParams['animation.html'] = 'jshtml'
    plt.title('CPU UTILIZATION')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.show()
    plt.ylabel('CPU')
    plt.xlabel('time')
    i = 0
    x, y = [], []

    while True:
        x.append(i)
        y.append(psutil.cpu_percent())
        ax.plot(x, y, color='b')
        fig.canvas.draw()
        ax.set_xlim(left=max(0, i-50), right=i+50)
        time.sleep(0.1)
        i += 1

    plt.close()



root=Tk()
root.geometry("750x1000")
root.title("Task Manager")
root.configure(bg="lavender")


btnsht = Button(root,text="Turnoff",command=shtdwdn,relief=RAISED)
btnsht.place(x=10,y=5)

btnrestart = Button(root,text="Restart",command=restart)
btnrestart.place(x=70,y=5)

btntasklist = Button(root,text="Task",command=tasklist)
btntasklist.place(x=130,y=5)

btntsysinfo = Button(root,text="system",command=sysinfo).place(x=220,y=5)
btnutil = Button(root,text="utilization",command=util).place(x=280,y=5)

btntsysinfi = Button(root,text="App",command=sysinfi).place(x=180,y=5)    
    
root.mainloop()
