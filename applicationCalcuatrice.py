#
# Nom du Fichier : applicationCalculatrice.py
# Auteur: Thanina Adda
# But: Permet de faire les operations de la calculatrice.
#
#

A = float(input("veuillez saisir la valeur de A: "))
op = input("veuillez saisir l'opérateur: ")
B = float(input("veuillez saisir la valeur de B: "))


if op=="+":
    print("A + B =", A+B)

elif op=="-":
    print("A - B =", A-B)

elif op=="/":
    
    print("A / B =", A/B)

elif op=="*":
    print("A * B =", A*B)

else:
    print("L'opération est incorrecte et non fonctionnelle")
