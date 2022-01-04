"""
Le but de l'exercice est de calculer la somme des 100 premiers entiers naturels
information : 
programme sur les pas du celebre mathematicien Gauss
https://fr.wikipedia.org/wiki/Somme_(arithm%C3%A9tique)
"""

x = 0
solution = 0
for x in range(100 + 1):
    solution = solution + x
print(solution)
