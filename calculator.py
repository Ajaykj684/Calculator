from tkinter import *
from tkinter import font


base = Tk()
base.title("Calculator")
base.geometry('400x500+30+40')
base.resizable(0,0)
base.configure(background='black')

label = Label(base,height=3, width=47,anchor= 'se')
label.place(x=30,y=75)
mfd_name = Label(base,text='Casio',fg='black',height='1',width='6')
mfd_name.place(x=30,y=20)


number = ''

def display(num):
    global number
    number = number+str(num)
    label['text'] = number


def equals():

    try:
        global number
        result=eval(number)
        label['text'] = result
    except:
        label['text'] = 'Error'

def clear():
    global number
    number = ''
    label['text']=number


def backspace():
    global number
    number = number[:-1]
    label['text']=number

times15 = font.Font(family='times', size=15, weight='bold')
button1 =  Button(text=1, height=2, width=7,command=lambda: display(1))
button2 =  Button(text=2, height=2,width=7,command=lambda: display(2))
button3 =  Button(text=3, height=2,width=7,command=lambda: display(3))
button4 =  Button(text=4, height=2,width=7,command=lambda: display(4))
button5 =  Button(text=5, height=2,width=7,command=lambda: display(5))
button6 =  Button(text=6, height=2,width=7,command=lambda: display(6))
button7 =  Button(text=7, height=2,width=7,command=lambda: display(7))
button8 =  Button(text=8, height=2,width=7,command=lambda: display(8))
button9 =  Button(text=9, height=2,width=7,command=lambda: display(9))
button0 =  Button(text=0, height=2,width=7,command=lambda: display(0))



button_dot =  Button(text='.', height=2,width=7,command=lambda: display('.'))
button_equal =  Button(text='=', height=2,width=7,command=equals)
button_clear =  Button(text='Clear', height=2,width=10,command=clear)

button_add =  Button(text='+', height=2,width=7,command=lambda: display('+'))
button_sub =  Button(text='-', height=2,width=7,command=lambda: display('-'))
button_div =  Button(text='/', height=2,width=7,command=lambda: display('/'))
button_mul =  Button(text='*', height=2,width=7,command=lambda: display('*'))
button_back =  Button(text='C', height=2,width=7,command=backspace)

button1.place(x=30,y=358)
button2.place(x=115,y=358)
button3.place(x=200,y=358)
button4.place(x=30,y=296)
button5.place(x=115,y=296)
button6.place(x=200,y=296)
button7.place(x=30,y=234)
button8.place(x=115,y=234)
button9.place(x=200,y=234)
button0.place(x=30,y=420)
button_dot.place(x=115,y=420)
button_equal.place(x=200,y=420)
button_clear.place(x=200,y=172)
button_back.place(x=285,y=172)
button_div.place(x=285,y=358)
button_mul.place(x=285,y=296)
button_sub.place(x=285,y=234)
button_add.place(x=285,y=420)

base.mainloop()

