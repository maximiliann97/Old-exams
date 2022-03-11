import abc

class Crypto(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def encrypt(self, msg):
        pass

    @abc.abstractmethod
    def decrypt(self, msg):
        pass


class PirateLangauge(Crypto):
    consonants = 'bcdfghjklmnpqrstvwx'

    def encrypt(self, s):
        for c in self.consonants:
            s = s.replace(c, c + 'o' + c).replace(c.upper(), c.upper() + 'o' + c)
        return s

    def decrypt(self, s):
        for c in self.consonants:
            s = s.replace(c + 'o' + c, c).replace(c.upper() + 'o' + c, c.upper())
        return s


class CharacterCrypto(Crypto):
    @abc.abstractmethod
    def encrypt_char(self, c):
        pass

    @abc.abstractmethod
    def decrypt_char(self, c):
        pass

    def encrypt(self, s):
        return ''.join([self.encrypt_char(c) for c in s])

    def decrypt(self, s):
        return ''.join([self.decrypt_char(c) for c in s])



class Rotator(CharacterCrypto):
    alphabet = 'bcdefghijklmnopqrstuvwxyz'
    def __init__(self, offset):
        self.offset = offset


    @staticmethod
    def shift(self, c, offset):
        p = Rotator.alphabet.find(c.lower())
        if p == -1:
            return c
        else:
            new_c = Rotator.alphabet[(p + offset) % len(Rotator.alphabet)]
            return new_c if c.islower() else new_c.upper()

    def encrypt_char(self, c):
        return self.shift(c, self.offset)

    def decrypt_char(self, c):
        return self.shift(c, -self.offset)

class Replacer(CharacterCrypto):
    def __init__(self, d: dict):
        self.d = d