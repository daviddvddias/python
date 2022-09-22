#/bin/python

''' Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.  '''


number_um = int(input("Digite o primeiro numero :"))

if number_um  < 0 :
    print("Negativo")
elif number_um == 0:
    print("Numero nulo")
else:
    print("Positivo")