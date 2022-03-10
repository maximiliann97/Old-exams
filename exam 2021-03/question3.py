class CosineSeries:
    def __init__(self, coef):
        self.coef = coef

    def __repr__(self):
        return f'Hello world'

    def __iter__(self):
        return iter(self.coef)

    def __len__(self):
        return len(self.coef)

    def evaluate_term(self, i, x):
        if x < 0:
            raise ValueError('X must be => 0')
