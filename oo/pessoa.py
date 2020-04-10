class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def comprimentar(self):
        return 'Olá Zacarias'


if __name__ == '__main__':
    # p = Pessoa('Maria')
    # p = Pessoa()
    # p.idade = 76
    # p.nome = 'Maria de Lurdes'
    # print('Diga algo para ele - ', Pessoa.comprimentar(p))
    # print(id(p))
    # print(p.comprimentar())
    # print('A idade de ', p.nome, ' é igual a ', p.idade)

    ederson = Pessoa(nome='Éderson')
    print(ederson.nome)
    print(ederson.idade)
    luciano = Pessoa(ederson, nome='Luciano',idade=30)
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

    #Atributos dinâmicos
    luciano.sobrenome = 'Ramalho'   #cria um atributo sobrenome dinamicamente
    del luciano.filhos              #exclui um atributo dinamicamente
    print(luciano.__dict__)         #mostrando os atributos de luciano
    print(ederson.__dict__)






