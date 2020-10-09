import json
import difflib
from difflib import get_close_matches
from tkinter import *


data = json.load(open("data.json"))
#word = input("enter a word:-")


def translator():

    word = w.get()
    word = word.lower()
    if word in data:
        return data[word]

    elif len(get_close_matches(word,data.keys())) > 0:
        x = get_close_matches(word,data.keys(),cutoff=0.7)[0]
        Output2.delete('1.0',END)
        Output2.insert(END,x)
        print("Did you mean:-",x)
        print(get_close_matches(word,data.keys(),cutoff=0.7))





    else:
        x = "get_close_matches(word,data.keys(),cutoff=0.7)[0]"

        Output.delete('1.0',END)
        Output.insert(END,x)

def y():
    word = w.get()
    word = word.lower()
    x = get_close_matches(word,data.keys(),cutoff=0.7)[0]
    return data[x]
def yes():
    out=y()
    if type(out) == list:
        for element in out:
            Output.delete('1.0',END)
            Output.insert(END,element)

    else:
        Output.delete("1.0",END)
def no():
    Output.delete('1.0',END)
    Output.insert(END,"There  is no such word in dictionary")

def final():

    out = translator()

    if type(out) == list:
        for element in out:
            Output.delete('1.0',END)
            Output.insert(END,element)
            Output2.delete('1.0',END)
    else:
        Output.delete("1.0",END)
        Output.insert(END,out)


def clear():
    e1.delete(0,END)
    Output.delete('1.0',END)
    Output2.delete('1.0',END)

window = Tk()

title = Label(window,text = "Dictionary")
title.grid(row=0,column=0,columnspan=3)


l1 = Label(window, text = "Enter a word :-")
l1.grid(row = 3,column = 0)
l2 = Label(window,text = "Did you mean :- ")
l2.grid(row=4,column =0)
w = StringVar()
e1 = Entry(window,textvariable=w)
e1.grid(row = 3,column = 2)

button = Button(window,text="Search",width = 8,command = final)
button.grid(row = 3 , column = 5)

button1 = Button(window,text="Clear",width = 8,command = clear)
button1.grid(row = 3 , column = 6)

button2 = Button(window,text="Yes",width = 8,command = yes)
button2.grid(row = 4 , column = 5)

button3 = Button(window,text="NO",width = 8,command = no)
button3.grid(row = 4 , column = 6)


Output = Text(window, height = 5, width = 25, bg = "light cyan")
Output.grid(row = 6 , column= 2)

Output2 = Text(window, height = 1, width = 15, bg = "pink")
Output2.grid(row = 4 , column= 2)

window.mainloop()
