class Animal:
    def __init__(self, patas):
        self.patas = patas

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{c} = {v}' for c, v in self.__dict__.items()])}"
    pass

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        
        super().__init__(**kw)

    pass

class Ave(Animal):
    def __init__(self, patas):
        self.patas = patas
        super().__init__(patas)
    pass

class Gato(Mamifero):
    pass

class cachorro(Mamifero):
    pass

class Pato(Ave):
    pass

class Onitorrinco(Ave, Mamifero):
    pass

gato = Gato(cor_pelo = "cinza", patas = 4)
print(gato)