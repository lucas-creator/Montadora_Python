from veiculo import Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo,passageiros, tanque, consumo, cor, marcha, qtd_pneus):
        super(). __init__(passageiros, tanque, consumo, cor, marcha, qtd_pneus)
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self,marca):
        self.__marca = marca


    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self,modelo):
        self.__modelo = modelo


    def dados(self):
        print("O Veiculo é {} da marca {}.".format(self.__modelo,self.__marca))
        super().dados()
