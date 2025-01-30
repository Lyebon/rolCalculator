# [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]

from character import *
from calculator import *
import json

with open("char_info.json", "r") as json_file:
    char_info = json_file.read()
    characters = json.loads(char_info)

def main():
    menu()

def menu():
    while True:
        print (f'Bienvenido a la aplicación\nPara ir a cada opción ingrese el numero correspondiente')
        opc = int(input(f'1. Crear un personaje\n2. Resolucion de tiradas\n3. Salir\nIngrese su opción: '))
        if opc == 1:
            new_characters = Character(characters)
        elif opc == 2:
            Calculator()
        elif opc ==3:
            quit()
        else:
            raise ValueError("El numero ingresado no es valido")


main()