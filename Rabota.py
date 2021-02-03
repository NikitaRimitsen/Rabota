from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import fileinput
from tkinter.messagebox import *
import webbrowser
import re
import tkinter as tk
from tkinter import PhotoImage


def funktion(a):
	tabs.select(a)

def print_hello():
    webbrowser.open_new_tab('https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D1%81%D0%BA%D0%BE%D0%BF')

def print_hello2():
    webbrowser.open_new_tab('https://horo.mail.ru/prediction/aries/today/')

def print_hello3():
    webbrowser.open_new_tab('https://horo.mail.ru/prediction/taurus/today/')

def print_hello4():
    webbrowser.open_new_tab('https://horo.mail.ru/prediction/gemini/today/')

def print_hello5():
    webbrowser.open_new_tab('https://horo.mail.ru/prediction/cancer/today/')

def print_hello6():
    webbrowser.open_new_tab('https://horo.mail.ru/prediction/leo/today/')

def print_hello7():
    webbrowser.open_new_tab('https://horo.mail.ru/prediction/virgo/today/')

def print_hello8():
    webbrowser.open_new_tab('https://horo.mail.ru/prediction/libra/today/')

def print_hello9():
    webbrowser.open_new_tab('https://horo.mail.ru/prediction/scorpio/today/')

def print_hello10():
    webbrowser.open_new_tab('https://horo.mail.ru/prediction/sagittarius/today/')

def print_hello11():
    webbrowser.open_new_tab('https://horo.mail.ru/prediction/capricorn/today/')

def print_hello12():
    webbrowser.open_new_tab('https://horo.mail.ru/prediction/aquarius/today/')

def print_hello13():
    webbrowser.open_new_tab('https://horo.mail.ru/prediction/pisces/today/')

root=Tk()
root.geometry("700x500")
root.title("Гороскоп")

tabs=ttk.Notebook(root)
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tab5=Frame(tabs)
tab6=Frame(tabs)
tab7=Frame(tabs)
tab8=Frame(tabs)
tab9=Frame(tabs)
tab10=Frame(tabs)
tab11=Frame(tabs)
tab12=Frame(tabs)
tab13=Frame(tabs)
tabs.add(tab1,text="Главная")
tabs.add(tab2,text="Овен")
tabs.add(tab3,text="Телец")
tabs.add(tab4,text="Близнецы")
tabs.add(tab5,text="Рак")
tabs.add(tab6,text="Лев")
tabs.add(tab7,text="Дева")
tabs.add(tab8,text="Весы")
tabs.add(tab9,text="Скорпион")
tabs.add(tab10,text="Стрелец")
tabs.add(tab11,text="Козерог")
tabs.add(tab12,text="Водолей")
tabs.add(tab13,text="Рыбы")
tabs.pack()
can=Canvas(tab2,width=300,height=200)
can.pack()






M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Все гороскопы",menu=m1)
m1.add_command(label="Главная", accelerator='Command+V',command=lambda:funktion(0))
m1.add_separator()
m1.add_command(label="Овен",command=lambda:funktion(1))
m1.add_command(label="Tелец",command=lambda:funktion(2))
m1.add_command(label="Близнецы",command=lambda:funktion(3))
m1.add_command(label="Рак",command=lambda:funktion(4))
m1.add_command(label="Лев",command=lambda:funktion(5))
m1.add_command(label="Дева",command=lambda:funktion(6))
m1.add_command(label="Весы",command=lambda:funktion(7))
m1.add_command(label="Скорпион",command=lambda:funktion(8))
m1.add_command(label="Стрелец",command=lambda:funktion(9))
m1.add_command(label="Козерог",command=lambda:funktion(10))
m1.add_command(label="Водолей",command=lambda:funktion(11))
m1.add_command(label="Рыбы",command=lambda:funktion(12))

m2=Menu(M,tearoff=0)
M.add_cascade(label="Цвета",menu=m2)
m2.add_command(label="Красный",command=lambda:root.config(bg="red"))
m2.add_command(label="Оранжевый",command=lambda:root.config(bg="#FFA500"))
m2.add_command(label="Зелёный",command=lambda:root.config(bg="green"))
m2.add_command(label="Синний",command=lambda:root.config(bg="blue"))
m2.add_command(label="Светло синний",command=lambda:root.config(bg="light blue"))
m2.add_command(label="Фиолетовый", command=lambda:root.config(bg="violet"))
m2.add_command(label="Белый",command=lambda:root.config(bg="white"))

imagetest = PhotoImage(file="goroskop.png")

button_qwer = tk.Button(tab1, image=imagetest, command=print_hello)
button_qwer.pack()


imagetest2 = PhotoImage(file="oven2.png")

button_qwer2 = tk.Button(tab2, image=imagetest2, command=print_hello2)
button_qwer2.pack()
imagetest3 = PhotoImage(file="telec2.png")

button_qwer3 = tk.Button(tab3, image=imagetest3, command=print_hello3)
button_qwer3.pack()

imagetest4 = PhotoImage(file="bliznece.png")

button_qwer4 = tk.Button(tab4, image=imagetest4, command=print_hello4)
button_qwer4.pack()

imagetest5 = PhotoImage(file="rak.png")

button_qwer5 = tk.Button(tab5, image=imagetest5, command=print_hello5)
button_qwer5.pack()

imagetest6 = PhotoImage(file="lev.png")

button_qwer6 = tk.Button(tab6, image=imagetest6, command=print_hello6)
button_qwer6.pack()

imagetest7 = PhotoImage(file="deva.png")

button_qwer7 = tk.Button(tab7, image=imagetest7, command=print_hello7)
button_qwer7.pack()

imagetest8 = PhotoImage(file="vesi.png")

button_qwer8 = tk.Button(tab8, image=imagetest8, command=print_hello8)
button_qwer8.pack()

imagetest9 = PhotoImage(file="skorpio.png")

button_qwer9 = tk.Button(tab9, image=imagetest9, command=print_hello9)
button_qwer9.pack()

imagetest10 = PhotoImage(file="strelec.png")

button_qwer10 = tk.Button(tab10, image=imagetest10, command=print_hello10)
button_qwer10.pack()

imagetest11 = PhotoImage(file="kozerog.png")

button_qwer11 = tk.Button(tab11, image=imagetest11, command=print_hello11)
button_qwer11.pack()

imagetest12 = PhotoImage(file="vodolei.png")

button_qwer12 = tk.Button(tab12, image=imagetest12, command=print_hello12)
button_qwer12.pack()

imagetest13 = PhotoImage(file="rebe.png")

button_qwer13 = tk.Button(tab13, image=imagetest13, command=print_hello13)
button_qwer13.pack()




tabs.pack(fill="both")
root.mainloop()
