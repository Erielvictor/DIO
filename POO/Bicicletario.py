class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Biiii biii")

    def parar(self):
        print("Bicicleta parando...")
        
        print("Bicicleta parada")
    
    def correr(self):
        print("A bicicleta está acelerando")

b1 = Bicicleta("Vermelha", "Caloi", 2022, 650)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.ano, b1.modelo, b1.valor)