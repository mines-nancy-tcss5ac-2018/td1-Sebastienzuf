#exercice euler 16

def solve(n):
    nombre = str(2**n)          #on transforme 2^n en une chaine de caractère
    Somme = 0                   #on initialise la somme
    for i in range ( len(nombre) ):
        Somme = Somme + int( nombre[i] )  #on ajoute à la somme le ième chiffre de 2^n
    return( Somme )


assert solve ( 15 ) == 26
assert solve ( 8 ) == 13

print(solve(1000))