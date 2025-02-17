from static_info import *
import random




class Creator_char():
    def __init__(self):
        self.caracteristica = caracteristicas
        self.char_final = bonificador_car
        self.personaje_raza = self.raza_char()
        personaje = self.generador_caracteristicas()
        print (personaje, self.personaje_raza)


    def ran_generator(self):
        return random.randint(1,100)
    
    def check_out(self, num, dic):
        for dato in dic:
            if num <= dato:
                return dato

    def generador_caracteristicas(self):
        for char in caracteristicas:
            num = self.ran_generator()
            self.caracteristica[char] = num
            self.char_final[char] = numero_por_car[self.check_out(num, numero_por_car)]
        return self.caracteristica, self.char_final

    def raza_char(self):
        raza_personaje = self.check_out(self.ran_generator(), raza)
        if raza_personaje == 75:
            return raza[75][self.check_out(self.ran_generator(), raza[raza_personaje])]
        return raza[raza_personaje]