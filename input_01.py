# Présentation de la fonction Input
#
#########################################

# Ici on cré un variable annee qui est = input ("une question") qui est un int entier
annee = input("Saisissez une année : ")
annee = int(annee)
    
if annee % 400 == 0 or (annee % 4 == 0 and annee %100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas une année bissextile.")
    
# Ici on demande le nom et on affiche le nom
def demander_nom():
    nom = input("Quel est votre nom: ")
    return nom

nom_personne = demander_nom()
print(nom_personne)

# Ici on pose une question ou l'on demande le nom, mais si la personne ne rentre rien, il y a le message Erreur: le nom ne doit pas être vide
def demander_nom():
    nom = input("Quel est votre nom: ")
    if nom == "":
        print("ERREUR : Le nom ne doit pas être vide")
        return demander_nom()
    return nom

nom_personne = demander_nom()

# Vous l'aurez compris Input permet de pouvoir poser une question ou de faire un choix
a=int(input("Saisir a: "))
if a ==0:
    print('a=0')
print("C'est gagne! ")
