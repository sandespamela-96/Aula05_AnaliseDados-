valor_pedido = float(input('Digite o valor: R$' ))
distancia = float(input('Distância (km): '))
frete = 8

if valor_pedido > 50 and distancia <= 3:
    print(f'Você ganhou frete grátis! Valor do pedido: {valor_pedido}')

else:
    valor_final = valor_pedido + frete
    print(f'Valor do pedido: R$ {valor_pedido}\nValor do frete: R$ {frete} \nValor total: R$ {valor_final}')