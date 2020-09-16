class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Obed = Pessoa(nome='Obed')
    Ducles = Pessoa(Obed, nome='Ducles')
    print(Pessoa.cumprimentar(Ducles))
    print(id(Ducles))
    print(Ducles.cumprimentar())
    print(Ducles.nome)
    print(Ducles.idade)
    for filho in Ducles.filhos:
       print(filho.nome)
    Ducles.sobrenome = 'Bedo'
    del Ducles.filhos
    print(Ducles.__dict__ )
    print(Obed.__dict__)
