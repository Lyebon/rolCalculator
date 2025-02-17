from static_info import *
import random




class Creator_char():
    def __init__(self):
        self.personaje = {}
        self.info_personaje = player_info
        self.caracteristica = caracteristicas
        self.char_final = bonificador_car
        self.ensambler()

# puras
    def ran_generator(self):
        return random.randint(1,100)
    
    def check_out(self, num, dic):
        for dato in dic:
            if num <= dato:
                return dato

#impuras
    def ensambler(self):
        self.personaje["raza"] = self.raza_char()
        self.personaje["caracteristicas"] = self.generador_caracteristicas()
        
        
        print (self.personaje)

    def raza_char(self):
        raza_personaje = self.check_out(self.ran_generator(), raza)
        if raza_personaje == 75:
            return raza_humano[self.check_out(self.ran_generator(), raza_humano)]
        return raza[raza_personaje]

    def generador_caracteristicas(self):
        for char in caracteristicas:
            num = self.ran_generator()
            self.caracteristica[char] = num
            self.char_final[char] = numero_por_car[self.check_out(num, numero_por_car)]
        return self.caracteristica, self.char_final

