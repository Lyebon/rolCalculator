class Calculator:
    def __init__(self, tirada, lista):
        self.tirada = tirada
        self.lista = lista
    
    def pifia(self, tirada, arma):
        if tirada <= arma:
            return ('Pifia de arma')

    def result(self, tirada, lista):
        for num in lista:
            if tirada <= num:
                return num
        return ValueError("Numero Invalido")