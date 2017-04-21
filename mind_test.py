import tkinter as tk
import tkinter.messagebox
import time
import random
from random import randint


main_window=tk.Tk()
main_window.geometry("500x500")
main_window.configure(background="#393640")
count=0
level_label=tk.Label(main_window,text=" Level :  Easy     ",bg='bisque2').place(x=380,y=12)

def help():
    tkinter.messagebox.showinfo("Help","Set Level from the Menu and Press Start to play.\n\nMemories as many words as you can to score.")

def credit():
    tkinter.messagebox.showinfo("Credits","Made by : Kushagra")

main_list=['Cricket','Football','Rugby','Hockey','Basketball','Baseball','Volleyball','Lawn Tennis','Badminton','Table Tennis','KitKat','Lolipop','Froyo','Nougat','JellyBeans','IceCream Sandwich','GingerBread','Honeycomb','Eclair','Donut','Red','Orange','Blue','Green','Black','Grey','Pink','Brown','White','Purple','United States','India','Russia','China','Brazil','Canada','London','Switzerland','Spain','Australia']
color_list=['powder blue','wheat1','plum1','ivory2','coral','PeachPuff2','SlateBlue1']
time1=4

def update(t,l):
    global time1
    time1=t
    level_label=tk.Label(main_window,text=" Level : "+l,bg='bisque2').place(x=380,y=12)



menubar=tk.Menu(main_window)
main_window.config(menu=menubar)
lmenu=tk.Menu(menubar,tearoff=False)
menubar.add_cascade(label="Levels",menu=lmenu)
lmenu.add_command(label="Easy",command=lambda:update(4,"  Easy     "))
lmenu.add_command(label="Medium",command=lambda:update(3,"Medium"))
lmenu.add_command(label="Hard",command=lambda:update(2,"  Hard     "))

menubar.add_command(label="Credits",command=credit)
menubar.add_command(label="Help",command=help)

frame=tk.Frame(main_window,height="420",width="500",bg="#0E484F")
frame.place(x=0,y=40)



def timer(t):
    if(t==0):
        enter_answer()
    else:
        t=t-1
        main_window.after(1000,timer,t)




def match_answer(a,b,c,d,e,f,g,h,i,j):
    global count,first_random_item,second_random_item,third_random_item,fourth_random_item,fifth_random_item,sixth_random_item,seventh_random_item,eighth_random_item,ninth_random_item,tenth_random_item
    if (a.lower()==first_random_item.lower() or a.lower()==second_random_item.lower() or a.lower()==third_random_item.lower() or a.lower()==fourth_random_item.lower() or a.lower()==fifth_random_item.lower() or a.lower()==sixth_random_item.lower() or a.lower()==seventh_random_item.lower() or a.lower()==eighth_random_item.lower() or a.lower()==ninth_random_item.lower() or a.lower()==tenth_random_item.lower() ):
        count=count+1
    if (b.lower()==first_random_item.lower() or b.lower()==second_random_item.lower() or b.lower()==third_random_item.lower() or b.lower()==fourth_random_item.lower() or b.lower()==fifth_random_item.lower() or b.lower()==sixth_random_item.lower() or b.lower()==seventh_random_item.lower() or b.lower()==eighth_random_item.lower() or b.lower()==ninth_random_item.lower() or b.lower()==tenth_random_item.lower() and b != a):
        count=count+1
    if (c.lower()==first_random_item.lower() or c.lower()==second_random_item.lower() or c.lower()==third_random_item.lower() or c.lower()==fourth_random_item.lower() or c.lower()==fifth_random_item.lower() or c.lower()==sixth_random_item.lower() or c.lower()==seventh_random_item.lower() or c.lower()==eighth_random_item.lower() or c.lower()==ninth_random_item.lower() or c.lower()==tenth_random_item.lower() and c != a and c != b):
        count=count+1
    if (d.lower()==first_random_item.lower() or d.lower()==second_random_item.lower() or d.lower()==third_random_item.lower() or d.lower()==fourth_random_item.lower() or d.lower()==fifth_random_item.lower() or d.lower()==sixth_random_item.lower() or d.lower()==seventh_random_item.lower() or d.lower()==eighth_random_item.lower() or d.lower()==ninth_random_item.lower() or d.lower()==tenth_random_item.lower() and d != a and d != b and d != c):
        count=count+1
    if (e.lower()==first_random_item.lower() or e.lower()==second_random_item.lower() or a.lower()==third_random_item.lower() or e.lower()==fourth_random_item.lower() or e.lower()==fifth_random_item.lower() or e.lower()==sixth_random_item.lower() or e.lower()==seventh_random_item.lower() or e.lower()==eighth_random_item.lower() or e.lower()==ninth_random_item.lower() or e.lower()==tenth_random_item.lower() and e != a and e != b and e != c and e != d):
        count=count+1
    if (f.lower()==first_random_item.lower() or f.lower()==second_random_item.lower() or f.lower()==third_random_item.lower() or f.lower()==fourth_random_item.lower() or f.lower()==fifth_random_item.lower() or f.lower()==sixth_random_item.lower() or f.lower()==seventh_random_item.lower() or f.lower()==eighth_random_item.lower() or f.lower()==ninth_random_item.lower() or f.lower()==tenth_random_item.lower() and f != a and f != b and f != c and f != d and f != e):
        count=count+1
    if (g.lower()==first_random_item.lower() or g.lower()==second_random_item.lower() or g.lower()==third_random_item.lower() or g.lower()==fourth_random_item.lower() or g.lower()==fifth_random_item.lower() or g.lower()==sixth_random_item.lower() or g.lower()==seventh_random_item.lower() or g.lower()==eighth_random_item.lower() or g.lower()==ninth_random_item.lower() or g.lower()==tenth_random_item.lower() and g != a and g != b and g != c and g != d and g != e and g != f):
        count=count+1
    if (h.lower()==first_random_item.lower() or h.lower()==second_random_item.lower() or h.lower()==third_random_item.lower() or h.lower()==fourth_random_item.lower() or h.lower()==fifth_random_item.lower() or h.lower()==sixth_random_item.lower() or h.lower()==seventh_random_item.lower() or h.lower()==eighth_random_item.lower() or h.lower()==ninth_random_item.lower() or h.lower()==tenth_random_item.lower() and h != a and h != b and h != c and h != d and h != e and h != f and h != g):
        count=count+1
    if (i.lower()==first_random_item.lower() or i.lower()==second_random_item.lower() or i.lower()==third_random_item.lower() or i.lower()==fourth_random_item.lower() or i.lower()==fifth_random_item.lower() or i.lower()==sixth_random_item.lower() or i.lower()==seventh_random_item.lower() or i.lower()==eighth_random_item.lower() or i.lower()==ninth_random_item.lower() or i.lower()==tenth_random_item.lower() and i != a and i != b and i != c and i != d and i != e and i != f and i != g and i != h):
        count=count+1
    if (j.lower()==first_random_item.lower() or j.lower()==second_random_item.lower() or j.lower()==third_random_item.lower() or j.lower()==fourth_random_item.lower() or j.lower()==fifth_random_item.lower() or j.lower()==sixth_random_item.lower() or j.lower()==seventh_random_item.lower() or j.lower()==eighth_random_item.lower() or j.lower()==ninth_random_item.lower() or j.lower()==tenth_random_item.lower() and j != a and j != b and j != c and j != d and j != e and j != f and j != g and j != h and j != i):
        count=count+1

    score=str(count)
    tkinter.messagebox.showinfo("Score","Your score is : "+score)
    start_button.config(state = "normal")
    count =0







def enter_answer():
    global frame
    frame.destroy()
    frame1=tk.Frame(main_window,height="420",width="500",bg="#0E484F")
    frame1.place(x=0,y=40)
    answer_heading_label=tk.Label(frame1,text="Enter your answers below")
    answer_heading_label.place(x=190,y=40)
    store_ans1= tk.StringVar()
    store_ans2= tk.StringVar()
    store_ans3= tk.StringVar()
    store_ans4= tk.StringVar()
    store_ans5= tk.StringVar()
    store_ans6= tk.StringVar()
    store_ans7= tk.StringVar()
    store_ans8= tk.StringVar()
    store_ans9= tk.StringVar()
    store_ans10= tk.StringVar()
    entry1=tk.Entry(frame1,textvariable=store_ans1)
    entry1.place(x = 200 ,y = 62 )
    entry2=tk.Entry(frame1,textvariable=store_ans2)
    entry2.place(x = 200 ,y = 84 )
    entry3=tk.Entry(frame1,textvariable=store_ans3)
    entry3.place(x = 200 ,y = 106 )
    entry4=tk.Entry(frame1,textvariable=store_ans4)
    entry4.place(x = 200 ,y = 128 )
    entry5=tk.Entry(frame1,textvariable=store_ans5)
    entry5.place(x = 200 ,y = 150 )
    entry6=tk.Entry(frame1,textvariable=store_ans6)
    entry6.place(x = 200 ,y = 172 )
    entry7=tk.Entry(frame1,textvariable=store_ans7)
    entry7.place(x = 200 ,y = 194 )
    entry8=tk.Entry(frame1,textvariable=store_ans8)
    entry8.place(x = 200 ,y = 216 )
    entry9=tk.Entry(frame1,textvariable=store_ans9)
    entry9.place(x = 200 ,y = 238 )
    entry10=tk.Entry(frame1,textvariable=store_ans10)
    entry10.place(x = 200 ,y = 260 )
    check_answer_button=tk.Button(frame1,text="Check Answer",command=lambda: match_answer(store_ans1.get(),store_ans2.get(),store_ans3.get(),store_ans4.get(),store_ans5.get(),store_ans6.get(),store_ans7.get(),store_ans8.get(),store_ans9.get(),store_ans10.get()))
    check_answer_button.place(x=220,y=284)



def click_start(self):
    global time1,frame,first_random_item,second_random_item,third_random_item,fourth_random_item,fifth_random_item,sixth_random_item,seventh_random_item,eighth_random_item,ninth_random_item,tenth_random_item
    start_button.config(state = "disabled")
    frame=tk.Frame(main_window,height="420",width="500",bg="#0E484F")
    frame.place(x=0,y=40)

    list_of_random_items = random.sample(main_list, 10)
    first_random_item = list_of_random_items[0]
    second_random_item = list_of_random_items[1]
    third_random_item = list_of_random_items[2]
    fourth_random_item = list_of_random_items[3]
    fifth_random_item = list_of_random_items[4]
    sixth_random_item = list_of_random_items[5]
    seventh_random_item = list_of_random_items[6]
    eighth_random_item = list_of_random_items[7]
    ninth_random_item = list_of_random_items[8]
    tenth_random_item = list_of_random_items[9]

    label1=tk.Label(frame,text=first_random_item,bg=random.choice(color_list)).place(x=randint(10,150),y=randint(40,120))
    label2=tk.Label(frame,text=second_random_item,bg=random.choice(color_list)).place(x=randint(150,300),y=randint(40,120))
    label3=tk.Label(frame,text=third_random_item,bg=random.choice(color_list)).place(x=randint(300,450),y=randint(40,120))
    label4=tk.Label(frame,text=fourth_random_item,bg=random.choice(color_list)).place(x=randint(10,150),y=randint(120,240))
    label5=tk.Label(frame,text=fifth_random_item,bg=random.choice(color_list)).place(x=randint(150,300),y=randint(120,240))
    label6=tk.Label(frame,text=sixth_random_item,bg=random.choice(color_list)).place(x=randint(300,450),y=randint(120,240))
    label7=tk.Label(frame,text=seventh_random_item,bg=random.choice(color_list)).place(x=randint(10,150),y=randint(240,400))
    label8=tk.Label(frame,text=eighth_random_item,bg=random.choice(color_list)).place(x=randint(150,300),y=randint(240,400))
    label9=tk.Label(frame,text=ninth_random_item,bg=random.choice(color_list)).place(x=randint(300,450),y=randint(240,400))
    label10=tk.Label(frame,text=tenth_random_item,bg=random.choice(color_list)).place(x=randint(20,450),y=randint(40,400))

    timer(time1)


start_button=tk.Button(main_window,text="    Start    ",bg="royal blue", command = lambda: click_start(0), relief= "raised" )
start_button.bind('<Return>', click_start)
start_button.place(x=230,y=470)


main_window.mainloop()
