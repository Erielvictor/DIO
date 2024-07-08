menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        quant = float(input("Informe quanto será depositado: "))
        saldo += quant
        print(f"O seu saldo atual é de {saldo} após depositar {quant}")
        extrato += f'Depósito: R${quant:.2f}\n'



    elif opcao == 's':
         
        print("Saque")
        quant = float(input("Informe quanto será sacado: "))

        excedeu_saldo = quant > saldo

        excedeu_limite = quant > limite 

        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saques:
            print("Não é possível realizar mais saques! pois o limite diário foi atingido!")
                
        elif excedeu_limite:
            print("O valor do saque excede o limite diário! operação falhou!")

        elif excedeu_saldo: 
            print("O valor do saque excede o saldo! operação falhou!")
            

        elif quant > 0 and not excedeu_saques and not excedeu_limite and not excedeu_saldo:
            saldo -= quant
            print(f"O seu saldo atual é de {saldo} após sacar {quant}")
            extrato += f'Saque: R${quant:.2f}\n'
            numero_saques += 1

        elif saldo == 0:
            print("O seu saldo está zerado! logo não é possível fazer um saque")
       

    elif opcao == "e":
        if extrato == '':
            print("Não foram realizadas movimentações!")
        else:
            print(f'{10 * "="}EXTRATO {10 * "="}')
            print(f'\nSaldo: R$ {saldo:.2f}')
            print(f"{extrato}")
            print(f'{10 * "="}EXTRATO {10 * "="}')

    elif opcao == 'q':
        break

    else:
        print("Operação inválida!")