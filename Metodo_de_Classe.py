class Pessoa:
    Olhos=2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_class(cls):
        return f'{cls}-Olhos {cls.Olhos}'


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
    Pessoa.Olhos = 3
    print(Pessoa.Olhos)
    print(Ducles.Olhos)
    print(Obed.Olhos)
    print(id(Pessoa.Olhos),id(Ducles.Olhos),id(Ducles.Olhos))
    print(Pessoa.metodo_estatico(),Ducles.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_class(),Ducles.nome_e_atributo_de_class())
