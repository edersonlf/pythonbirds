class Pessoa:
    def __int__(self, nome=None, idade=35):
        self.nome = nome
        self.idade = idade

    def comprimentar(self):
        return 'Olá Zacarias'


if __name__ == '__main__':
    #p = Pessoa('Maria')        #não funcionou
    p = Pessoa()
    p.idade = 76
    p.nome = 'Maria de Lurdes'
    print('Diga algo para ele - ', Pessoa.comprimentar(p))
    print(id(p))
    print(p.comprimentar())
    print('A idade de ', p.nome, ' é igual a ', p.idade)




