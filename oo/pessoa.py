class Pessoa:
    olhos = 2

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
    amanda.olhos = 1
    del amanda.olhos
    print(amanda.__dict__)
    print(paul.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(amanda.olhos)
    print(paul.olhos)
    print(id(Pessoa.olhos), id(amanda.olhos), id(paul.olhos))
