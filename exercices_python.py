# -*- coding: utf-8 -*-
"""Exercices Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xWcxR8qV2z2Asb6K-ciPJIWuVUTIajs4

Exercice 1.3
"""

nombreSTR=input()
nombre = int(nombreSTR)
type(nombre)
if nombre > 0:
  print("Ce chiffre est positif")
elif nombre < 0:
  print("ce chiffre est négatif")
else:
  print("Le 0 ne compte pas ici")

"""Exercice 1.4"""

nombreSTR1=input()
nombreSTR2=input()
nombre1 = int(nombreSTR1)
nombre2 = int(nombreSTR2)
if (nombre1 * nombre2 > 0):
  print("Le produit de ces deux nombres est positif")
elif (nombre1 * nombre2 < 0):
    print("Le produit de ces deux nombres est négatif")
else:
  print("Ce résultat n'est pas pris en compte")

"""Exercice 1.5"""

nombreSTR=input()
nombre = int(nombreSTR)
i = 0
while i <= 10:
  print(nombre)
  nombre += 1
  i += 1

"""Exercice 1.6"""

nombreSTR = input()
nombre = int(nombreSTR)
i = 0
resultat = 0
while i<nombre:
  i += 1
  resultat += i
print(resultat)

