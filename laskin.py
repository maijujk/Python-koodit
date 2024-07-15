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
root.configure(bg='dim grey')  # Ikkunan taustaväri
# Globaalit muuttujat
expression = ""

# Päivitä näyttö
def update_display():
    global expression
    if len(expression) > 14:
        expression = expression[:14]  # Rajaa näytettävät merkit 14:een ensimmäiseen
    display_var.set(expression)

# Lisää merkki
def add_to_expression(value):
    global expression
    if value == "" or value == "x":
        return
    # Tarkistetaan, että expression ei sisällä vielä operaattorimerkkiä
    if any(op in expression for op in "+-*/%."):
        if value.isdigit() or (value in "+-*/%." and len(expression) == 1):
            # Sallitaan toinen merkki, jos ensimmäinen on numero ja toinen on operaattori
            expression += str(value)
    elif not expression and value in "+-*/%.":
        expression += "0" + str(value)
    else:
        expression += str(value)
    update_display()

# Laske tulos
def evaluate_expression():
    global expression
    try:
        result = eval(expression)
        if isinstance(result, float) and result.is_integer():
            result = int(result)  # Muunnetaan desimaaliluku kokonaisluvuksi, jos mahdollista
        expression = str(result)
    except Exception as e:
        expression = "Error"
    update_display()

# Tyhjennä näyttö
def clear_expression():
    global expression
    expression = ""
    update_display()
    
# Poista viimeinen merkki
def delete_last():
    global expression
    if expression == "Error":        
        return
    elif expression.isdigit() and expression in "+-*/%" or len(expression) > 0:
        expression = expression[:-1]
        if len(expression) == "0":
            expression = ""
    update_display()
    
# Funktio, joka vaihtaa napin väriä, kun hiiri on napin päällä
def on_enter(event, btn):
    btn['bg'] = 'dim grey'

# Funktio, joka palauttaa napin värin, kun hiiri poistuu napin päältä
def on_leave(event, btn):
    btn['bg'] = 'grey'

# Käyttöliittymän luominen
display_var = tk.StringVar()

# # Näyttö
display = tk.Label(root, textvariable=display_var, font=('Arial', 24), width=20, bg='dim grey', fg='black')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# # Painikkeet
buttons = [
    '', 'C', 'x', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '', '0', '.', '='
]

row = 1
col = 0

for button in buttons:
    action = lambda x=button: add_to_expression(x) if x != '=' else evaluate_expression()   
    if button == "C":
        # C-painike
        btn = tk.Button(root, text='C', bd=2, padx=30, pady=10, font=('Arial', 14), command=clear_expression, bg='grey', fg='black', activebackground='dim grey')
    elif button == "x":
        # x-painike
        btn = tk.Button(root, text='x', bd=2, padx=30, pady=10, font=('Arial', 14), command=delete_last, bg='grey', fg='black', activebackground='dim grey')
    else:
        btn = tk.Button(root, text=button, bd=2, padx=27, pady=7, font=('Arial', 14), command=action, bg='grey', fg='black', activebackground='dim grey')
    btn.grid(row=row, column=col, sticky="nsew")  

    # Bindaa Enter- ja Leave-tapahtumat napille
    btn.bind("<Enter>", lambda event, b=btn: on_enter(event, b))
    btn.bind("<Leave>", lambda event, b=btn: on_leave(event, b))

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