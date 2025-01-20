class Characters:
    def __init__(self, party, npc, animals):
        self.party = party
        self.npc = npc
        self.animals = animals
        self.menu()


    def menu():
        print("1- PJ")
        print("2- NPC")
        print("3- Animal")
        print("4- Return")
        menu_num = int(input("Que tipo de personaje quiere crear"))

        if menu_num == 1:
            Player()
        elif menu_num == 2:
            NPC()
        elif menu_num == 3:
            Animals()
        elif menu_num == 4:
            exit
        else:
            raise Exception ("El numero ingresado no pertenece a las opciones")

class Player(Characters):
    def __init__(self, party):
        super().__init__(party)

class NPC(Characters):
    def __init__(self, npc):
        super().__init__(npc)

class Animals(Characters):
    def __init__(self, animals):
        super().__init__(animals)