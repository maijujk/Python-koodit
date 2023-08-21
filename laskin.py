
# -----------------------------------------------------------------------------

# Ohjelmoi tkInter-kirjastoa hyödyntäen graafinen laskin, 
# jossa perustoiminnot: + - * / = 
# ja syöttökentän tyhjennys.
from tkinter import *

x = ""

def paina(numero):
    global x
    x = x + str(numero)
    julkaisu.set(x)

def yhteensa():
    global x
    yhteensa = str(eval(x))
    julkaisu.set(yhteensa)
 
def tyhjenna():
    global x
    x = ""
    julkaisu.set("")
    
ikkuna = Tk()
ikkuna.configure(background="light grey")
ikkuna.title("Laskin")
ikkuna.geometry("265x280")

julkaisu = StringVar()
kentta = Entry(ikkuna, textvariable=julkaisu)
kentta.grid(columnspan=3, ipadx=20)
 
painike7 = Button(ikkuna, text="7", fg="black",
                    command=lambda: paina(7), height=3, width=8)
painike7.grid(row=1, column=0)
 
painike8 = Button(ikkuna, text="8", fg="black",
                command=lambda: paina(8), height=3, width=8)
painike8.grid(row=1, column=1)
 
painike9 = Button(ikkuna, text="9", fg="black",
                    command=lambda: paina(9), height=3, width=8)
painike9.grid(row=1, column=2)
 
painike4 = Button(ikkuna, text="4", fg="black",
                    command=lambda: paina(4), height=3, width=8)
painike4.grid(row=2, column=0)
 
painike5 = Button(ikkuna, text="5", fg="black",
                command=lambda: paina(5), height=3, width=8)
painike5.grid(row=2, column=1)
 
painike6 = Button(ikkuna, text="6", fg="black",
                command=lambda: paina(6), height=3, width=8)
painike6.grid(row=2, column=2)
 
painike1 = Button(ikkuna, text="1", fg="black",
                    command=lambda: paina(1), height=3, width=8)
painike1.grid(row=3, column=0)
 
painike2 = Button(ikkuna, text="2", fg="black",
                command=lambda: paina(2), height=3, width=8)
painike2.grid(row=3, column=1)
 
painike3 = Button(ikkuna, text="3", fg="black",
                command=lambda: paina(3), height=3, width=8)
painike3.grid(row=3, column=2)
 
painike0 = Button(ikkuna, text="0", fg="black",
                    command=lambda: paina(0), height=3, width=8)
painike0.grid(row=4, column=1)
 
jako = Button(ikkuna, text="/", fg="black",
               command=lambda: paina("/"), height=3, width=8)
jako.grid(row=0, column=3)
 
kerto = Button(ikkuna, text="*", fg="black",
                command=lambda: paina("*"), height=3, width=8)
kerto.grid(row=1, column=3)
 
miinus = Button(ikkuna, text="-", fg="black",
                command=lambda: paina("-"), height=3, width=8)
miinus.grid(row=2, column=3)
 
plus = Button(ikkuna, text="+", fg="black",
                command=lambda: paina("+"), height=3, width=8)
plus.grid(row=3, column=3)
 
yhteensa = Button(ikkuna, text="=", fg="black",
                command=yhteensa, height=3, width=8)
yhteensa.grid(row=4, column=3)
 
tyhjenna = Button(ikkuna, text="C", fg="black",
                command=tyhjenna, height=3, width=8)
tyhjenna.grid(row=4, column=0)
 
Desimaali= Button(ikkuna, text=",", fg="black",
                command=lambda: paina(","), height=3, width=8)
Desimaali.grid(row=4, column=2)


ikkuna.mainloop()