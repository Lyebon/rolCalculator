class Characters:
    def __init__(self, party, npc, animals):
        self.party = party
        self.npc = npc
        self.animals = animals

class Player(Characters):
    def __init__(self, party):
        super().__init__(party)
        self.creator()
    
    def creator(self):
        pass

class NPC(Characters):
    def __init__(self, npc):
        super().__init__(npc)

class Animals(Characters):
    def __init__(self, animals):
        super().__init__(animals)