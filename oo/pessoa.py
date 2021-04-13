class Pessoa:
    def __init__(self, *filhos, nome=None, idade=29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    paul = Pessoa(nome='Paul')
    amanda = Pessoa(paul, nome='Amanda')
    print(Pessoa.cumprimentar(amanda))
    print(id(amanda))
    print(amanda.cumprimentar())
    print(amanda.nome)
    print(amanda.idade)
    for filho in amanda.filhos:
        print(filho.nome)
    amanda.sobrenome = 'Wirthmann'
    del amanda.filhos
    print(amanda.__dict__)
    print(paul.__dict__)
