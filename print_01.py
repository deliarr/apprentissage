print("Bonjour le monde")

nom = "Franck"
ville = "Toulouse"
ans = str(51)

print("Bonjour je m'appelle : " + nom + " je vie à " + ville + " et j'ai " + ans + " ans")

""" Dans cette exemple nous allons utiliser la fonction INPUT pour poser une question et permettre 
d'y écrire quelque chose.
"""
annee = input("Saisissez une année : ")
annee = int(annee)
    
if annee % 400 == 0 or (annee % 4 == 0 and annee %100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas une année bissextile.")

# ici on peut aussi afficher des résultats de calculs.
a = 5
b = 12
c = 3
print(a + b)
print(a + b - c)
print(a % c)
print(a / b * c)
# Autres exemples ici on affiche un entier et un float
print(f"J'affiche l'entier {10} et le float {3.14}")
print(f"J'affiche la chaine {'Python'}")

# On peut aussi limiter le nombre de chiffre après la virgule
prop_GC = (4500 + 2575) / 14800
print("La proportion de GC est", prop_GC)
# Ici on limite à 2 chiffres après la virgule
print(f"La proportion de GC est {prop_GC:.2f}")
# Ici on limite à 3 chiffres après la virgule
print(f"La proportion de GC est {prop_GC:.3f}")

