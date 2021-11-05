import tkinter
from tkinter import *
import random
import time
from time import *
wn=tkinter.Tk()
wn.title("Quiz For Topper")
wn.geometry("800x600")
wn.resizable(0,0)
wn.config(background="white")
img=PhotoImage(file="Img.png")
imglabel=Label(wn,image=img,background="white" )
imglabel.grid(padx=(250,0),pady=(0,30))
imglabel.pack(pady=(0,30))
Questions=["Q.1 What is a correct syntax to output (Hello World) in Python?",
           "Q.2 Which one is NOT a legal variable name?",
           "Q.3 What is the correct syntax to output the type of a variable or object in Python?",
           "Q.4 What is the correct way to create a function in Python?",
           "Q.5 Which method can be used to remove any whitespace from both the beginning and the end of a string?",
           "Q.6 Which method can be used to return a string in upper case letters",
           "Q.7 Which collection is ordered, changeable, and allows duplicate members?",
           "Q.8 What is called when a function is defined inside a class?",
           "Q.9 What is the output of the expression : 3*1**3",
           "Q.10 Suppose list1 is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after list1.pop(1)?"]
Options=[["echo(Hello World)","p(Hello World)","echo(Hello World)","print(Hello World)"],
         ["_myvar","Myvar","my-var","my_var"],
         ["print(typeOf(x))","print(type(x))","print(typeof(x))","print(typeof x)"],
         ["create myFunction():","function myfunction():","def myFunction():","class myFunction():"],
         ["ptrim()","trim()","len()","strip()"],
         ["upperCase()","toUpperCase()","upper()","uppercase()"],
         ["SET","LIST","DICTIONARY","TUPLE"],
         ["Module","Class","Another Function","Method"],
         ["27","9","3","1"],
         ["[3,4,5,20,5,25,1,3]","[1,3,3,4,5,5,20,25]","[3,5,20,5,25,1,3]","[1,3,4,5,20,2,25]"]]
Answers=[3,2,2,2,1,2,1,3,2,2]
def Show_Result(score):
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    Questions_label.destroy()
     
   
    labelimage=Label(wn,background="white")
    labelimage.pack(pady=(30,90))
    labelresulttext=Label(wn,font=("Times",20,"bold"),background="white",fg="black",justify="center")
    labelresulttext.pack(pady=(0,20))
    labelresulttext1=Label(wn,font=("Consolas",15),background="white",fg="black",justify="center")
    labelresulttext1.pack()
    if score>=8:
        img=PhotoImage(file="good.png")
        labelimage.config(image=img)
        labelimage.image=img
        labelresulttext1.config(text=f"Your Score is {score} ")
        labelresulttext.config(text="YOU ARE EXECELLENT !!")
    elif score>=4 and score<8:
        img=PhotoImage(file="better.png")
        labelimage.config(image=img)
        labelimage.image=img
        labelresulttext1.config(text=f"Your Score is {score} ")
        labelresulttext.config(text="YOU ARE GOOD !!")
    elif score<4:
        img=PhotoImage(file="sad.png")
        labelimage.config(image=img)
        labelimage.image=img
        labelresulttext1.config(text=f"Your Score is {score} ")
        labelresulttext.config(text="BETTER LUCK NEXT TIME !!")
def calc():
    global Indexes,user_answer,Answers
    z=0
    score=0
    for y in Indexes:
        if Answers[y] == user_answer[z]:
            score=score+1
        z+=1 
    Show_Result(score)
i=1
user_answer=[]
def Option_selected():
    global radiovar,user_answer
    global Questions_label,r1,r2,r3,r4
    global i
    x=radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if i<10:
        Questions_label.config(text=Questions[Indexes[i]])
        r1['text']=Options[Indexes[i]][0]
        r2['text']=Options[Indexes[i]][1]
        r3['text']=Options[Indexes[i]][2]
        r4['text']=Options[Indexes[i]][3]
        i+=1
    else:
        calc()
Indexes=[]
def gen():
    global Indexes
    while(len(Indexes)<10):
        x=random.randint(0,9)
        if x in Indexes:
            continue
        else:
            Indexes.append(x)
def Start_Quiz():
    global Questions_label,r1,r2,r3,r4
    Questions_label=Label(wn,text=Questions[Indexes[0]],font=("Comic sans MS",20),background="white",fg="black",width="100",wraplength="600",justify="center")
    Questions_label.pack(pady=(50,50))
    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)
    r1=Radiobutton(wn,text=Options[Indexes[0]][0],font=("Times",20),background="white",fg="black",value=0,variable=radiovar,command=Option_selected,cursor="hand2")
    r1.pack()
    r2=Radiobutton(wn,text=Options[Indexes[0]][1],font=("Times",20),background="white",fg="black",value=1,variable=radiovar,command=Option_selected,cursor="hand2")
    r2.pack()
    r3=Radiobutton(wn,text=Options[Indexes[0]][2],font=("Times",20),background="white",fg="black",value=2,variable=radiovar,command=Option_selected,cursor="hand2")
    r3.pack()
    r4=Radiobutton(wn,text=Options[Indexes[0]][3],font=("Times",20),background="white",fg="black",value=3,variable=radiovar,command=Option_selected,cursor="hand2")
    r4.pack()
    
 
def StartButtonIsPressed():
    label.destroy()
    label1.destroy()
    labelRules.destroy()
    button.destroy()
    imglabel.destroy()
    #sleep(1)
    gen()
    Start_Quiz()
     

label=Label(wn,text="Quiz For Topper",font=("Comic sans MS",20,"bold"),background="white",fg="black")
label.pack(pady=(0,25))
button=Button(wn,text="START",font=("Comic sans MS",15),background="#ff99dd",fg="#008ae6",relief=FLAT,border=0.,padx="5",cursor="hand2",command=StartButtonIsPressed)
button.pack(pady=(0,35))
label1=Label(wn,text="Read The Rules\nClick Start Once You Are Ready",background="white",font=("Consolas",15))
label1.pack(pady=(0,20))
labelRules=Label(wn,text="This Quiz Contains 5 Questions\nYou Will Get 20 Minutes For Solve A Quiz\nOnce You Select Option That Will Be The Final Choice\nHence,Think Before You Select.",
                 width="100",font=("Times",20),background="black",fg="white",justify="center")
labelRules.pack()
wn.mainloop()
