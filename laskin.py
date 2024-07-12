# -----------------------------------------------------------------------------
# tkInter-kirjastoa hyödyntäen graafinen laskin, 
# jossa perustoiminnot: + - * / = 
# ja syöttökentän tyhjennys

import tkinter as tk

# Luo pääikkuna
root = tk.Tk()
root.title("Laskin")
root.geometry("325x380")  # Suurenna ikkunaa
root.resizable(0, 0)
root.configure(bg='grey')  # Ikkunan taustaväri
# Globaalit muuttujat
expression = ""

# Päivitä näyttö
def update_display():
    display_var.set(expression)

# Lisää merkki
def add_to_expression(value):
    global expression
    expression += str(value)
    update_display()

# Laske tulos
def evaluate_expression():
    global expression
    try:
        result = str(eval(expression))
        expression = result
    except Exception as e:
        expression = "Error"
    update_display()

# Tyhjennä näyttö
def clear_expression():
    global expression
    expression = ""
    update_display()

# Käyttöliittymän luominen
display_var = tk.StringVar()

# Näyttö
display = tk.Entry(root, textvariable=display_var, font=('Arial', 24), insertwidth=2, width=14, borderwidth=8, bg='grey', fg='black')
display.grid(row=0, column=0, columnspan=3, padx=10, pady=30)  # Lisää padding
tk.Button(root, text='C', bd=3, padx=30, pady=10, font=('Arial', 14), command=clear_expression, bg='grey', fg='black').grid(row=0, column=3, padx=5, pady=5)

# # Painikkeet
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    ',', '0', '=', '+'
]

row = 1
col = 0

for button in buttons:
    action = lambda x=button: add_to_expression(x) if x != '=' else evaluate_expression()
    tk.Button(root, text=button, bd=3, padx=27, pady=7, font=('Arial', 14), command=action, bg='grey', fg='black').grid(row=row, column=col, sticky="nsew")  # Poista padding ja lisää sticky
    col += 1
    if col > 3:
        col = 0
        row += 1

# # Lisää ruudukon laajennus
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(row+1):
    root.grid_rowconfigure(i, weight=1)

# Käynnistä pääsilmukka
root.mainloop()