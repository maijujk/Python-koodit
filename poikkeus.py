
# -----------------------------------------------------------------------------

#[ ] Täydennä funktio`isValid` joka tarkistaa onko käyttäjän antama numero positiivinen parillinen luku.
# Funktion nostaa poikkeuksen jos käyttäjä antaa parittoman luvun.
# Valmis koodi huolehtii poikkeuksen käsittelyn 

#Lisää siis koodi kohtaan todo.
def isValid(num): #nosta poikkeus
      if num < 1 or num % 2 != 0:
        raise ValueError("Noup")#!!!!!!!!!!
      else:
        return num

valid = False
while not valid:
    try:
        x = int(input("Enter an odd positive number: "))
        x = isValid(x)
        valid = True
    except ValueError as except_object:
        print("{}".format(except_object))

print("{:d} was accepted".format(x))