opcao = int(input('Valor da venda: '))

match opcao:
    case _ if opcao >=500:
        print('Venda grande')
    case _ if opcao > 100:
        print('Venda média')
    case _ if opcao < 100:
        print('Venda pequena')