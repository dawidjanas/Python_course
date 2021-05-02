class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, var):
        self.name = var
        print(self.name, "constructed")

    def party(self):
	    self.x = self.x + 1
	    print("So far", self.x)
		
sally = PartyAnimal("Sally")
jim = PartyAnimal("Jim")

sally.party()
jim.party()