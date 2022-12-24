from class_Human import Human
class Creation:
    def __init__(self):
        self.name = input("Bonojour au simulateur d'humain. Veuiller donner un nom à votre humain svp: ")
        self.age = input("Veuiller donner un age à votre humain svp: ")
        self.nom = self.name
        self.name = Human(self.age)
        print (self.name, self.name.body_parts())
while True:
    user = Creation()



