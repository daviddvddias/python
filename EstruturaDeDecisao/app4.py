#/bin/python

''' Faça um Programa que verifique se uma letra digitada é vogal ou consoante '''


from operator import ge
from traceback import print_tb


vogal = str(input("Digite a letra :")).strip().upper()

vogais = [ "A","E","I","O","U" ]

if len(vogal) == 1:
   if vogal in vogais:
    print("Isso é uma vogal")
   else:
     print("Consoante")

else:
    print("Por favor digite somente uma letra para avaliação")