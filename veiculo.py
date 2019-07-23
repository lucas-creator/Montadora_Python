class Veiculo:
    def __init__(self, passageiros, tanque, consumo, cor, marcha, qtd_pneus):
          self._passageiros = passageiros
          self._tanque = tanque
          self._consumo = consumo
          self._cor = cor
          self._marcha = marcha
          self._qtd_pneus = qtd_pneus


    @property
    def passageiros(self):
        return self._passageiros
    @passageiros.setter
    def passageiros(self,passageiros):
        self._passageiros = passageiros


    @property
    def tanque(self):
        return self._tanque
    @tanque.setter
    def tanque(self,tanque):
        self._tanque = tanque


    @property
    def Consumo(self):
        return self._Consumo
    @Consumo.setter
    def Consumo(self,Consumo):
        self._Consumo = Consumo


    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self,cor):
        self._cor = cor


    @property
    def marcha(self):
        return self._marcha
    @marcha.setter
    def marcha(self,marcha):
        self._marcha = marcha


    @property
    def qtd_pneus(self):
        return self._qtd_pneus
    @qtd_pneus.setter
    def qtd_pneus(self,qtd_pneus):
        self._qtd_pneus = qtd_pneus



    def dados(self):
        print("tem capacidade para transportar {} pessoas.".format(self._passageiros))
        print("possui um tanque de {} litros.".format(self._tanque))
        print("Seu Consumo é de {} litros/km.".format(self._consumo))
        print("Sua Cor é:".format(self._cor))
        print("possui {} marchas.".format(self._marcha))
        print("possui {} rodas.".format(self._qtd_pneus))
        print("----------------------------------------------------------------------")
