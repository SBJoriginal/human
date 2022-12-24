from class_shapes_and_bodyparts import Head, Torso, Arms, Legs


class Human:
    def __init__(self, age):
        self.age = age
        self.head_number = 1
        self.torso_number = 1
        self.arms_number = 2
        self.legs_number = 2
        self.head = Head(self.age)
        self.torso = Torso(self.age * 2, self.age, self.age * 3)
        self.arm = Arms(self.age, self.age * 3)
        self.leg = Legs(self.age, self.age * 3)

    def body_parts(self):
        body_parts = self.head_number + self.arms_number + self.legs_number + self.torso_number
        return("has", body_parts, "body parts. Including", self.head_number, "head,", self.arms_number,
                     "arms and", self.legs_number, "legs!")

    def aire(self):
        return self.head.aire() + self.torso.aire() + 2 * ((self.arm.aire()) + (1.2 * (self.leg.aire())))

    def volume(self):
        return self.head.volume() + self.torso.volume() + 2 * ((self.arm.volume()) + (1.2 * (self.leg.volume())))

if __name__ == "__main__":
    Gab = Human(19)
    print(Gab.body_parts())
    print(Gab.aire())
    print(Gab.volume())
