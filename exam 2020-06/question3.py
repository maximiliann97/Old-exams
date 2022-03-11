from datetime import date


class Person:
    def __init__(self, firstname, lastname, born, dead=None):
        self.firstname = firstname
        self.lastname = lastname
        self.born = born
        self.dead = dead
        self._parents = set()
        self._children = set()
        self._spouse = None

    def add_parent(self, parent):
        self._parents.add(parent)

    def add_child(self, child):
        if child in self._children:
            raise InvalidPerson('Cannot be multiple of the same child')
        self._children.add(child)

    def set_spouse(self, spouse):
        self._spouse = spouse

    def show(self):
        print(self)
        if self._parents:
            print(f'Parents: {self._parents}')
        elif self._children:
            print(f'Children: {self._children}')
        elif self._spouse:
            print(f'Spouse: {self._spouse}')

    def counts_descendants(self):
        count = len(self._children)
        for c in self._children:
            count += c.count_descendants()
        return count

    def __repr__(self):
        if self.dead is None:
            dead = 'No'
        else:
            dead = self.dead
        return f'Person({self.firstname} {self.lastname} ({self.born}). Deceased: ({dead}))'


class Family:
    def __init__(self, parent1: Person, parent2: Person = None):
        self.parents = [parent1]
        if parent2:
            if parent2 == parent1:
                raise InvalidPerson('Cannot have two of the same parent')
            self.parents.append(parent2)
            parent1.set_spouse(parent2)
            parent2.set_spouse(parent1)

    def add_child(self, child):
        for p in self.parents:
            if child == p:
                raise InvalidPerson('Parent and child cannot be the same')
            if child.born <= p.born:
                raise InvalidPerson('A child cannot be older than its parents')
            p.add_child(child)
            child.add_parent(p)


class InvalidPerson(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg



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


try:
    f3 = Family(p1, p1)
except InvalidPerson as e:
    print(e)
try:
    f2.add_child(p2)
except InvalidPerson as e:
    print(e)
try:
    f2.add_child(p3)
except InvalidPerson as e:
    print(e)
try:
    f2.add_child(p5)
except InvalidPerson as e:
    print(e)