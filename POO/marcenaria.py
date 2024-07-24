from time import sleep

class Marcenaria:
    def __init__(self, movel, tamanho):
        self.movel = movel
        self.tamanho = tamanho
        
    def movel_info(self):
        preco = self.tamanho * 135
        frete = preco * 0.10
        print(f"O móvel: {self.movel}, tendo um tamanho de: {self.tamanho} metro(s), custa R$ {preco}, considerando o valor de R$ 135/m \n O frete fica: R${frete}")

    def construir(self):
        
        global tempo
        tempo = self.tamanho / 2

        print(f"A construção de um {self.movel} demora {tempo} dia(s)!")
        for i in range(int(tempo)):
            sleep(tempo)
            print(f"Dia {i + 1}")
        

    def enviar(self):

        entrega = tempo * 5

        if not self.enviar:
            print("O móvel não foi enviado")
            self.enviar = False

        print(f"O móvel foi enviado e irá chegar em {int(entrega)} dias")
        self.enviar = True

        for i in range(int(entrega), -1, -1):
            sleep(1)
            print(f"Chegando em {i} Dia(s)!")

            if i == 0:
                print("O móvel foi entregue!")
        


m1 = Marcenaria("Banco", 3)
m1.movel_info()
m1.construir()
m1.enviar()

