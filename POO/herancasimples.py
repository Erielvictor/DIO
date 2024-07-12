class veiculo:
    def __init__(self, cor, placa, modelo):
        self.cor = cor
        self.placa = placa
        self.modelo = modelo

    def carregado(self):
        print("Esta carregado")
    
    def ligar_motor(self):
        print("Vrum vrum")
        

class motocicleta(veiculo):
    pass

class Carro(veiculo):
    pass

class Caminhao(veiculo):
    def __init__(self, cor, placa, modelo, carregado):
        super().__init__(cor, placa, modelo)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")
    pass

moto = motocicleta("Preta", "SKY-222", "YAMAHA")
moto.ligar_motor()
print(moto)


carro = Carro("Vermelho", "QJU-111", "BMW")
carro.ligar_motor()
print(carro)

caminhao = Caminhao("Azul", "FJA-333", "SCANIA", True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)

print('')
