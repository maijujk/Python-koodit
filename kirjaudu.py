
# -----------------------------------------------------------------------------

# Graafinen käyttöliittymä tkinter-kirjastoa hyödyntäen, 
# Ohjelma pyytää käyttäjältä nimen ja salasanan.
# Kun tunnukset on oikein, ohjelma toivottaa tervetulleeksi,
# jos väärin pyydetään yrittämään uudestaan.
from tkinter import *

def tyhjenna():
  syote1.delete(0, END)
  syote2.delete(0, END)
  lista.delete(0,"end")
    
def suorita():
  syote1 = syote_temp1.get()
  syote2 = syote_temp2.get()
  if syote1 != "nimi" or syote2 != "salasana":
   lista.insert("end", "Yritä uudestaan!")
  
  else:
   lista.insert("end", "Tervetuloa!")

ikkuna = Tk()

ikkuna.title("Kirjaudu")

text1 = Label(text="Nimi").grid(row=0)
syote_temp1 = StringVar()
syote1 = Entry(ikkuna,  textvariable=syote_temp1)
syote1.grid(row=0, column=1)

text1 = Label(text="Salasana", fg="black").grid(row=1)
syote_temp2 = StringVar()
syote2 = Entry(ikkuna, textvariable=syote_temp2)
syote2.grid(row=1, column=1)

painike1 = Button(text="Kirjaudu", command=suorita)
painike1.grid(row=2, column=1)

lista = Listbox(ikkuna, height=3, bg="light grey")
lista.grid(row=3, column=1)

painike2 = Button(ikkuna, text="Tyhjennä", command=tyhjenna)
painike2.grid(row=4, column=1)

ikkuna.mainloop()