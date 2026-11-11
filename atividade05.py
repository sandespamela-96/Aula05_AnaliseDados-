opcao = int(input('Escolha um número: '))

match opcao:
    case 0:
        print('Zero')
    case _ if opcao > 0:
        print('Positivo')
    case _ if opcao < 0:
        print('Negativo')

