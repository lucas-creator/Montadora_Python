from veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo,passageiros, tanque, consumo, cor, marcha, qtd_pneus):
        super(). __init__(passageiros, tanque, consumo, cor, marcha, qtd_pneus)
        self._marca = marca
        self._modelo = modelo

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca = marca


    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self,modelo):
        self._modelo = modelo


    def dados(self):
        print("O Veiculo é {} da marca {}.".format(self._modelo,self._marca))
        super().dados()
