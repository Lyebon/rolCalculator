from damage import *

tabla_daños = [40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150]


def main():
    menu()

def menu():
    while True:
        tirada = int(input("Ingrese la tirada"))
        resultado = Calculator(tirada, tabla_daños)
        print (resultado)
        



main()