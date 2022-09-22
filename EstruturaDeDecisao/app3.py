#/bin/python

''' Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. '''


from operator import ge


genero = str(input("Digite F- Feminino, M - Masculino:")).strip().upper()

saniteze_genero =  genero[0]

if saniteze_genero == 'F':
    print("FEMININO")
elif saniteze_genero == 'M':
    print("MACULINO")
else:
    print("SEXO INVALIDO")