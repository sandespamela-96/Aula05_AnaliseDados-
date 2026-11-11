nota_final = float(input('Nota final: '))
frequencia = float(input('Frequência (%): '))
valor_mensalidade = float(input('Valor da mensalidade: R$ '))

#evitar:
# bolsa = valor_mensalidade * 0.20
# mensalidade_desconto = valor_mensalidade - bolsa

if nota_final >= 7 and frequencia >= 75:
    bolsa = valor_mensalidade * 0.20
    mensalidade_desconto = valor_mensalidade - bolsa
    print(f'Você ganhou uma bolsa no valor de R$ {bolsa}\nMensalidade a pagar R$ {mensalidade_desconto}')

else:
    print(f'Você não tem direito a bolsa.\nMensalidade a pagar R$ {valor_mensalidade}')
