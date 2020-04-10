class Pessoa:
    olhos = 2       #atributo default ou de classe

    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def comprimentar(self):
        return 'Olá Zacarias'


if __name__ == '__main__':
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
    print(ederson.__dict__)         #atributos de ederson
    print('olhos de Pessoa = ', Pessoa.olhos, '  olhos de ederson = ', ederson.olhos,'  olhos de luciano = ', luciano.olhos)
    print(id(Pessoa.olhos), id(ederson.olhos), id(luciano.olhos))






