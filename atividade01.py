#Símbolos: > MAIOR < MENOR >= MAIOR OU IGUAL <= MENOR OU IGUAL == IGUAL
# if = primeira condição - elif = outra condição para testar - else = qualquer outro caso


nota01 = float(input('Informe a nota 01: '))
nota02 = float(input('Informe a nota 02: '))
nota03 = float(input('Informe a nota 03: '))
nota04 = float(input('Informe a nota 04: '))

#Processamento
soma_notas = nota01 + nota02 + nota03 + nota04
media_final = soma_notas / 4

#Saída
if media_final >= 7:
    print(f'Sua média final foi {media_final}, você está aprovado.')

elif media_final >= 5:
    print(f'Sua média final foi {media_final}, você está em recuperação.')

else:
    print(f'Sua média final foi {media_final}, você está reprovado.')

