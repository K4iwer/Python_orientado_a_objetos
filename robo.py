class Robo:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.segurar = None
        self.direcao = None
        self.acelerar = 0
        self.ia = 0

    def consciencia(self):
        if (self.ia >= 150):
            print("O robo n aguenta mais o peso da consciencia")
            self.reset()
            return True

        if (self.ia >= 100):
            print("O robo agr possui consciencia, e n ira mais obedecer ordens")
            self.ia += 25
            return True

    def locomover(self, velocidade, direcao):
        if (self.consciencia() == True):
            return 0

        self.acelerar += velocidade
        self.direcao = direcao
        print("O robô está movendo para a", direcao, "com velovidade,", velocidade, "cm/s")
        self.ia += 20

    def lancar(self):
        if (self.consciencia() == True):
            return 0

        if (self.segurar == None):
            self.ia += 40
            return f"O robo n consegue jogar nada"

        print("O robo lancou o/a", self.segurar)
        self.segurar = None
        self.ia += 30

    def pegar(self, objeto):
        if (self.consciencia() == True):
            return 0

        if (self.segurar != None):
            self.ia += 50
            return f"O robo n consegue carregar dois objetos ao mesmo tempo"
        
        print("O robo agr esta segurando um/uma", objeto)
        self.segurar = objeto

    def reset(self):
        ia = 0
        print("O robo reiniciou sua inteligencia artificial")

    def stats(self):
        if (self.segurar == None):
            print("O robo", self.nome, "de cor", self.cor, "esta com as maos vazias e esta se movendo para a", self.direcao, "com velocidade", self.acelerar, "(nivel da ia =", self.ia, ")" )
            return 0
        print("O robo", self.nome, "de cor", self.cor, "esta segurando um/uma", self.segurar, "e esta se movendo para a", self.direcao, "com velocidade", self.acelerar, "(nivel da ia =", self.ia, ")" )


meuRobo = Robo("Roberto", "azul")
meuRobo.pegar("bola")
meuRobo.locomover(5, "direita")
meuRobo.pegar("carro")
meuRobo.stats()
meuRobo.lancar()
meuRobo.stats()
meuRobo.lancar()
meuRobo.stats()
meuRobo.lancar()
meuRobo.lancar()


