venda = int(input('Valor da venda: R$ '))

match venda:
    case venda if venda < 500:
        print('Venda média')
    case venda if venda < 100:
        print('Venda pequena')
    case _:
        print('Venda grande')