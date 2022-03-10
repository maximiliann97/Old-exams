class RepeatedList:
    def __init__(self, lista, repetitions):
        self.lista = lista
        self.repetitions = repetitions

    def __len__(self):
        return len(self.lista) * self.repetitions

    def __getitem__(self, i: int):
        if i < 0 or i >= len(self.lista):
            raise IndexError("Out of bounds")
        return self.lista[i % len(self.lista)]

    def __str__(self):
        return f'{self.lista}*{self.repetitions}'

    def tolist(self):
        return self.lista * self.repetitions

    def __iter__(self):
        return RepeatedListIterator(self)


class RepeatedListIterator:
    def __init__(self, repeatedList):
        self.repeatedList = repeatedList
        self.repetition = 0
        self.seqiter = iter(self.repeatedList.lista)

    def __next__(self):
        if self.repetition < self.repeatedList.repetitions:
            try:
                return next(self.seqiter)
            except StopIteration:
                self.repetition += 1
                if self.repetition == self.repeatedList.repetitions:
                    raise
                self.seqiter = iter(self.repeatedList.lista)
                return next(self.seqiter)
        else:
            raise StopIteration




print("Test [1,2,3]x3")
x = RepeatedList([1,2,3], 3)
assert len(x) == 9 # Verify true length
assert len(x.tolist()) == 9 # Verify the length of the expanded list
print(x) # Test printing
for i, v in enumerate(x): # Iterate over entire sequence (9 elements)
    print(f'{i}: {v}')
print(x.tolist()) # Expand the list to verify the order is as expected
assert x.tolist() == [v for v in x] # Verify that tolist and iterating are consistent

print("\nTest [4,5,6]x0")
y = RepeatedList([4,5,6], 0)
assert len(y) == 0
print(y) # Test printing
for v in y:
    assert False # Should not occur, zero elements

print("\nTest []x0")
z = RepeatedList([], 3)
assert len(y) == 0
print(z)
for v in z:
    assert False # Should not occur, zero elements

print("\nTest 3 quintillion floats!")
w = RepeatedList([3.14, 2.72, 1.41], 1000000000000000000)
assert len(w) == 3000000000000000000 # Verify the length
print(w) # Test printing
print(w[2999999999999999999]) # Test getting items out of the list

