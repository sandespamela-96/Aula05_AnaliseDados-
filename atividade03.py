valor_compra = float(input('Valor total da compra: R$ '))
programa_fidelidade = input('Tem cadastro no programa de fidelidade? [S/N] ').lower()[0]

#Constante = uso da letra maiuscula, o valor não altera até o final do código
#valores fixos ficam na entrada, variáveis não

FRETE = 25.0

if valor_compra > 200 or programa_fidelidade == 's':
    print(f'Você ganhou frete grátis! Valor a pagar: R$ {valor_compra}')

else:
    print(f'Valor da compra: R$ {valor_compra} + Frete: {FRETE}\nValor total a pagar: R$ {valor_compra + FRETE}')