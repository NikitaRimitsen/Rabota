from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import fileinput
from tkinter.messagebox import *


def funktion(a):
	tabs.select(a)


def image_(name,i):
    global img
    tabs.select(i)
    img=PhotoImage(file=name)
    can.create_image(20,20,image=img,anchor=NW)




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


m3=Menu(M,tearoff=0)
M.add_cascade(label="Image",menu=m3)
m3.add_command(label="Овен",command=lambda:image_("oven.png",1))
m3.add_command(label="Телец",command=lambda:image_("telec.png",2))






tabs.pack(fill="both")
root.mainloop()
