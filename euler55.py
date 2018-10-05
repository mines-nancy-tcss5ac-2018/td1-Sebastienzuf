# exercice euler 55

def palindrome(n):                     #fonction qui dit si un nombre est un palindrome
    nombre = str(n)                            #on transforme le nombre en une chaine de caractère
    for i in range ( len(nombre)//2 ):
        if nombre[i] != nombre[-i-1]:
            return( False )
    return( True )   
    

def inverse_nombre(n):          #fonction qui inverse l'ordre des chiffres dans un nombre
    nombre = str(n)
    inverse = str()
    for i in range (len(nombre)):
        inverse = inverse + nombre[-1-i]   #on inverse les positions
    return( int(inverse) )


def Lychrel(n):             #*fonction qui renvoie 1 si n est un nombre de Lychrel
    nombre = n                        
    inverse = inverse_nombre( n )
    for i in range (51):            #on fait au maximu 51 opérations
        if palindrome( nombre+inverse ) == True:    #si la somme du nombre et de l'inverse est un palindrome
            return( 0 )                            #alors n n'est pas un palindrome
        nombre = nombre + inverse               #on recommence avec les nouvelles valeurs
        inverse = inverse_nombre(nombre)
    return( 1 )


def solve(n):
    Nombre_Lychrel = 0                  #Zcompteur du nombre de nombre de Lychrel
    for i in range (1,n+1):
        Nombre_Lychrel = Nombre_Lychrel + Lychrel(i)
    return( Nombre_Lychrel )


assert palindrome(121) == True
assert palindrome(123 )== False
assert inverse_nombre(123) == 321
assert inverse_nombre(5426) == 6245
assert Lychrel(196) == 1
assert Lychrel(10677) == 1
assert Lychrel(47) == 0

print(solve(10000))






        


        




    