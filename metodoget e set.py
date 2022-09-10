class cachorro:
    def __init__(self, raca, nome) -> None:
        self.raca = raca
        self.nome = nome

    def getraca(self):
        return self.raca
    def setraca(self, novaraca):
        self.raca = novaraca
    def getnome(self):
        return self.nome
    def setnome(self, novonome):
        self.nome = novonome


cachorro1 = cachorro('chiuaua', 'rex')
print("Mostrando o objeto 'cachorro1 | ANTES DA ALTERAÇÃO'")
print("=============================")
print('Nome: '+cachorro1.getnome())
print('Racça: '+cachorro1.getraca())
print("============================= \n\n")

cachorro1.setraca('pitbull')
cachorro1.setnome('paçoquinha')
print("Mostrando o objeto 'cachorro1 | DEPOIS DA ALTERAÇÃO'")
print("=============================")
print('Nome: '+cachorro1.getnome())
print('Racça: '+cachorro1.getraca())
print("============================= \n\n")


    