#exercice euler 22

# -*- coding: utf-8 -*-

import os
os.chdir("C:/Users/Sébastien/Desktop/Sébastien/Ecole/Mines Nancy 18-21/1 année/Info python/Euler 22")

def valeur_lettre(x):
    initialisation = ord('A')                 #les éléments dans le fichier sont en majuscules, il faut donc faire attention
    return ( ord(x) - initialisation + 1 )         #une fois la valeur de A définie, on peut calculer les suivantes


def score_mot(x):                       #fonction qui calcule le score d'un mot x qui ets une chaine de caractère
    Score=0
    for i in range (len(x)):
        Score = Score + valeur_lettre(x[i])     #on somme les valeurs de chaque lettres
    return(Score)


def transformation_fichier():           #fonction qui transforme le fichier en une liste de chaine de caractères triés
    file = open("p022_names.txt", "r")      #on ouvre le fichier
    liste = []
    for s in file:
        liste = liste + s.split('","')          #on met dans une liste chaque chaine de caractère
    liste[0] = liste[0].split('"').pop()                      #cependant au début et à la fin il reste des "
    liste[ len(liste)-1 ] = liste[ len(liste)-1 ].split('"').pop(0)       #on les supprime
    liste.sort()                        #on trie la liste
    return ( liste )
 

def solve():
    liste = transformation_fichier()
    Somme_score = 0
    for i in range(len(liste)):
        Somme_score = Somme_score + score_mot( liste[i] )*(i+1)       #il ne reste plus qu'à sommer pour chaque mot
    return( Somme_score )                                #on multiplie par i+1 car il y a un décalage d'indice dans les listes


assert valeur_lettre('C') == 3
assert valeur_lettre('G') == 7
assert score_mot('ABC') == 6
assert score_mot('COLIN') == 53

print(solve())



        
    


        
        
            
         