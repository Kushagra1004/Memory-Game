import tkinter as tk
import tkinter.messagebox
import time
import random
from random import randint


main_window=tk.Tk()
main_window.geometry("400x400")
main_window.configure(background="#393640")
level_label=tk.Label(main_window,text="Level : Easy     ",bg='bisque2').place(x=280,y=12)

def help():
    tkinter.messagebox.showinfo("Help","Set Level from the Menu and Press Start to play.\n\nMemories as many words as you can to score.")

def credit():
    tkinter.messagebox.showinfo("Credits","Made by : Kushagra")

main_list=['Cricket','Football','Rugby','Hockey','Basketball','Baseball','Volleyball','Lawn Tennis','Badminton','Table Tennis']
color_list=['red','blue','green','yellow','cyan']
time1=5

def update(t,l):
    global time1
    time1=t
    level_label=tk.Label(main_window,text="Level : "+l,bg='bisque2').place(x=280,y=12)



menubar=tk.Menu(main_window)
main_window.config(menu=menubar)
lmenu=tk.Menu(menubar,tearoff=False)
menubar.add_cascade(label="Levels",menu=lmenu)
lmenu.add_command(label="Easy",command=lambda:update(5,"Easy     "))
lmenu.add_command(label="Medium",command=lambda:update(3,"Medium"))
lmenu.add_command(label="Hard",command=lambda:update(2,"Hard     "))

menubar.add_command(label="Credits",command=credit)
menubar.add_command(label="Help",command=help)

frame=tk.Frame(main_window,height="320",width="400",bg="#0E484F")
frame.place(x=0,y=40)



def timer(t):
    if(t==0):
        enter_answer()
    else:
        t=t-1
        main_window.after(1000,timer,t)



def enter_answer():
    global frame
    frame.destroy()
    frame1=tk.Frame(main_window,height="320",width="400",bg="#0E484F")
    frame1.place(x=0,y=40)
    answer_heading_label=tk.Label(frame1,text="Enter your answers below")
    answer_heading_label.place(x=140,y=40)
    store_ans1= tk.StringVar()
    store_ans2= tk.StringVar()
    store_ans3= tk.StringVar()
    store_ans4= tk.StringVar()
    entry1=tk.Entry(frame1,textvariable=store_ans1)
    entry1.place(x = 150 ,y = 62 )
    entry2=tk.Entry(frame1,textvariable=store_ans1)
    entry2.place(x = 150 ,y = 82 )
    entry3=tk.Entry(frame1,textvariable=store_ans1)
    entry3.place(x = 150 ,y = 102 )
    entry4=tk.Entry(frame1,textvariable=store_ans1)
    entry4.place(x = 150 ,y = 122 )



def click_start(self):
    global time1,frame
    start_button.config(state = "disabled")
    frame=tk.Frame(main_window,height="320",width="400",bg="#0E484F")
    frame.place(x=0,y=40)

    list_of_random_items = random.sample(main_list, 4)
    first_random_item = list_of_random_items[0]
    second_random_item = list_of_random_items[1]
    third_random_item = list_of_random_items[2]
    fourth_random_item = list_of_random_items[3]

    label1=tk.Label(frame,text=first_random_item).place(x=randint(20,350),y=randint(40,300))
    label2=tk.Label(frame,text=second_random_item).place(x=randint(20,350),y=randint(40,300))
    label3=tk.Label(frame,text=third_random_item).place(x=randint(20,350),y=randint(40,300))
    label4=tk.Label(frame,text=fourth_random_item).place(x=randint(20,350),y=randint(40,300))
    timer(time1)


start_button=tk.Button(main_window,text="Start",bg="royal blue", command = lambda: click_start(0), relief= "raised" )
start_button.bind('<Return>', click_start)
start_button.place(x=180,y=370)


main_window.mainloop()
