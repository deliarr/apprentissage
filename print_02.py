# Ici je vais m'interesser à l'affichage des nombres
#
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
#
nb_G = 4500
nb_C = 2575
print(f"Ce génome contient {nb_G:d} G et {nb_C:d} C, soit une prop de GC de {prop_GC:.2f}")
perc_GC = prop_GC * 100
print(f"Ce génome contient {nb_G:d} G et {nb_C:d}")
# Ici un 
print(f"Le résultat de 5 * 5 vaut {5 * 5}")
print(f"Résultat d'une opération avec des floats : {(4.1 * 6.7)}")
print(f"Le minimum est {min(1, -2, 4)}")
entier = 2
print(f"Le type de {entier} est {type(entier)}")
# Il y a aussi des écritures scientifique
print(f"{1_000_000_000:e}")
print(f"{0.000_000_001:e}")
# Ici on défini le nombre de chiffre après la virgule
avogadro_number = 6.022_140_76e23
print(f"{avogadro_number:.0e}")
print(f"{avogadro_number:.3e}")
print(f"{avogadro_number:.6e}")