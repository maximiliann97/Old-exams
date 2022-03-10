from datetime import date


class Person:
    def __init__(self, firstname, lastname, born, dead=None):
        self.firstname = firstname
        self.lastname = lastname
        self.born = born
        self.dead = dead

    def add_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.child = child

    def set_spouse(self, spouse):
        self.spouse = spouse

    def show(self):
        return

    def counts_descendants(self):
        pass

    def __repr__(self):
        if self.dead is None:
            dead = 'No'
        else:
            dead = self.dead
        return f'Person({self.firstname} {self.lastname} ({self.born}). Deceased: ({dead}))'


class Family:
    def __init__(self, parent1: Person, parent2: Person = None):
        self.parent1 = parent1
        self.parent2 = parent2

    def add_child(self, child):
        self.child = child


class InvalidPerson:
    pass



p1 = Person("Glenn", "Svensson", date(1990, 10, 21))
p2 = Person("Ada", "Andersson", date(1992, 5, 11))
p3 = Person("Lotta", "Svensson", date(2013, 9, 17))
p4 = Person("Knut", "Andersson", date(2015, 8, 29))
p5 = Person("Lovisa", "Eriksson", date(1927, 7, 3), date(2003, 2, 9))

print(p1, p2, sep=", ")
print(p3, p4, sep=", ")


f1 = Family(p5)
f1.add_child(p2)

f2 = Family(p2, p1)
f2.add_child(p3)
f2.add_child(p4)

p1.show()
p3.show()