num = float(input('Escolha um número: '))

match num:
    case 0:
        print(f'O número escolhido é igual a zero')
    case num if num > 0:
        print(f'O número {num} escolhido é positivo')
    case num if num < 0:
        print(f'O número {num} escolhido é negativo')

