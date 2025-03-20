#Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, 
# o valor unitário de cada peça 1, o código de uma peça 2,
# o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
codigo_peça1 = input()
numerp_de_peças1 = input()
valor_de_peça = float(input())
codigo_peça2 = input()
numerp_de_peças2 = input()
valor_de_peça2 = float(input())
calculo = (numerp_de_peças1 * valor_de_peça) + (numerp_de_peças2 * valor_de_peça2)
print('VALOR A PAGAR: R$ %.2f'%calculo)