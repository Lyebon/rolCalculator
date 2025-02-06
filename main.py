# [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]
from char_info import *
character_info = char_info

def main():
    new_character(character_info)

def menu():
    while True:
        print (f'Bienvenido a la aplicación\nPara ir a cada opción ingrese el numero correspondiente')
        opc = int(input(f'1. Crear un personaje\n2. Resolucion de tiradas\n3. Salir\nIngrese su opción: '))
        if opc == 1:
            character = new_character(character_info)
        elif opc == 2:
            pass
        elif opc ==3:
            quit()
        else:
            raise ValueError("El numero ingresado no es valido")

def new_character(character_info):
    for info in character_info:
        for data in character_info[info]:
            character_info[info][data] = input(f"Enter the data for {data}: ")
        

main()