from math import pi


class Shapes:
    def __init__(self, longueur, largeur, hauteur):
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        pass

    def volume(self):
        pass


class Rectangle(Shapes):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur, hauteur)

    def aire(self):
        return ((2 * self.longueur * self.largeur) + (2 * self.largeur * self.hauteur) + (
                    2 * self.longueur * self.hauteur))

    def volume(self):
        return (self.longueur * self.largeur * self.hauteur)


class Cylindre(Shapes):
    def __init__(self, rayon, hauteur):
        super().__init__(rayon, None, hauteur)
        self.rayon = rayon

    def aire(self):
        return (2 * pi * self.rayon ** 2) * (self.rayon + self.hauteur)

    def volume(self):
        return pi * self.rayon ** 2 * self.hauteur


class Sphere(Shapes):
    def __init__(self, rayon):
        super().__init__(rayon, None, None)
        self.rayon = rayon

    def aire(self):
        return 4 * pi * self.rayon ** 2

    def volume(self):
        return (4 / 3) * pi * self.rayon ** 3


class Head(Sphere):
    def __init__(self, rayon):
        super().__init__(rayon)


class Torso(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur, hauteur)


class Arms(Cylindre):
    def __init__(self, rayon, hauteur):
        super().__init__(rayon, hauteur)
        self.rayon = rayon


class Legs(Cylindre):
    def __init__(self, rayon, hauteur):
        super().__init__(rayon, hauteur)
        self.rayon = rayon


if __name__ == "__main__":
    # a = Rectangle(4, 5, 6)
    # print(a.aire())
    # print(a.volume())
    a = Cylindre(1, 2)
    print(a.aire())

    b = Arms(1, 2)
    print(b.aire())

    d = Legs(1, 2)
    print(d.aire())

    # c = Sphere(1)
    # print(c.aire())
    # print(c.volume())

    # arm * 20% = leg
