from characters import Characters
from damage import Calculator

party = []
npc = []
animals = []



def main():
    menu()

def menu():
    print("1- Creador de Personajes")
    print("2- Combate")
    print("3- Salir")
    menu_num = int(input("Que opcion desea realizar "))

    if menu_num == 1:
        Characters(party, npc, animals)
    elif menu_num == 2:
        Calculator()
    elif menu_num == 3:
        exit
    else:
        raise Exception ("El numero ingresado no pertenece a las opciones")

main()