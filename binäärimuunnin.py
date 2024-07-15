import tkinter as tk

# Luo pääikkuna
root = tk.Tk()
root.title("Binäärimuunnin")
root.geometry("325x380")  # Suurenna ikkunaa
root.resizable(0, 0)
root.configure(bg='grey')  # Ikkunan taustaväri

# Globaalit muuttujat
expression = ""

# Päivitä näyttö
def update_display():
    global expression
    if len(expression) > 20:
        expression = expression[:20]  # Rajaa näytettävät merkit 20:een ensimmäiseen
    display_var.set(expression)

# Lisää merkki
def add_to_expression(value):
    global expression
    if value == "" or value == "x":
        return
    expression += str(value)
    update_display()

def decimal_to_binary():
    global expression
    try:
        decimal_number = int(expression)
    except ValueError:
        expression = "Error"
        update_display()
        return
    
    if decimal_number == 0:
        expression = "0"
    else:
        binary_number = ""
        while decimal_number > 0:
            remainder = decimal_number % 2
            binary_number = str(remainder) + binary_number
            decimal_number = decimal_number // 2
        expression = binary_number
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
    elif len(expression) > 0:
        expression = expression[:-1]
    update_display()
    
# Funktio, joka vaihtaa napin väriä, kun hiiri on napin päällä
def on_enter(event, btn):
    btn['bg'] = 'grey'

# Funktio, joka palauttaa napin värin, kun hiiri poistuu napin päältä
def on_leave(event, btn):
    btn['bg'] = 'dim grey'

# Käyttöliittymän luominen
display_var = tk.StringVar()

# Näyttö
display = tk.Label(root, textvariable=display_var, font=('Arial', 20), width=20, bg='grey', fg='black')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=30)

# Painikkeet
buttons = [
    '', 'C', 'x', 
    '7', '8', '9', 
    '4', '5', '6', 
    '1', '2', '3', 
    '', '0', '=', 
]

row = 1
col = 0

for button in buttons:
    action = lambda x=button: add_to_expression(x) if x != '=' else decimal_to_binary()   
    if button == "C":
        # C-painike
        btn = tk.Button(root, text='C', bd=2, padx=40, pady=10, font=('Arial', 14), command=clear_expression, bg='dim grey', fg='black', activebackground='dim grey')
    elif button == "x":
        # x-painike
        btn = tk.Button(root, text='x', bd=2, padx=40, pady=10, font=('Arial', 14), command=delete_last, bg='dim grey', fg='black', activebackground='dim grey')
    else:
        btn = tk.Button(root, text=button, bd=2, padx=40, pady=10, font=('Arial', 14), command=action, bg='dim grey', fg='black', activebackground='dim grey')
    btn.grid(row=row, column=col, sticky="nsew")  

    # Bindaa Enter- ja Leave-tapahtumat napille
    btn.bind("<Enter>", lambda event, b=btn: on_enter(event, b))
    btn.bind("<Leave>", lambda event, b=btn: on_leave(event, b))

    col += 1
    if col > 2:
        col = 0
        row += 1

# Lisää ruudukon laajennus
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(row+1):
    root.grid_rowconfigure(i, weight=1)

# Käynnistä pääsilmukka
root.mainloop()
