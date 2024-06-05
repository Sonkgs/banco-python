menu = """
==========================================
=== ESCOLHA QUE OPERAÇÃO DESEJA FAZER ====

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==========================================
=> """

saldo = 0
limite_valor = 500
limite_quantidade = 3
extrato = ""
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        try:
            valor = float(input("\nInforme o valor a depositar: "))
            if valor > 0:
                saldo += valor
                print(f"\nO valor de R$ {valor:.2f} foi depositado com sucesso!")
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("\nValor inválido.")

        except:
            print("\nOcorreu um erro. Por favor, tente novamente")

    elif opcao.lower() == "s":
        if limite_quantidade == 0:
            print("\nJá atingiu seu limite de saques diários")
        else: 
            try:
                saque = float(input("\nInforme o valor a sacar: "))

                if saque > saldo:
                    print("\nSaldo insuficiente.")

                elif saque > limite_valor:
                    print(f"\nA solicitação excede seu limite de saque de {limite_valor}.")

                elif saque > 0:
                    saldo -= saque
                    print(f"\nO valor de R$ {saque:.2f} foi retirado com sucesso!")
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    limite_quantidade -= 1
                else:
                    print("\nValor inválido")

            except:
                print("\nOcorreu um erro. Por favor, tente novamente")

    elif opcao.lower() == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao.lower() == "q":
        break

    else:
        print("\nOperação inválida. Por favor, selecione novamente a operação desejada.")