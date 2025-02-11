from static_info import *
import random



class Creator_char():
    def __init__(self):
        self.caracteristica = caracteristicas
        self.char_final = bonificador_car
        self.bonificador_de_char = numero_por_car
        character = self.ensambler()
        print (character)
    
    def ran_generator(self):
        return random.randrange(1,100)

    def ensambler(self):
        personaje = {}
        personaje["caracteristicas"].update(self.generador_caracteristicas())
        personaje.update(self.generador_bonif_caracteristicas(personaje["caracteristicas"]))
        return personaje

    def generador_caracteristicas(self):
        for key in self.caracteristica:
            self.caracteristica[key] = self.ran_generator()
        return self.caracteristica
    
    def generador_bonif_caracteristicas(self):
        for key in self.caracteristica:
            self.char_final[key]
            

class Lvl_up(Creator_char):
    pass