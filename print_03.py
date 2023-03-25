
x = 32
nom = "John"
print("%s a %d ans" % (nom, x))
# Ici un autre cas
nb_G = 4500
nb_C = 2575
prop_GC = (nb_G + nb_C)/14800
print("On a %d G et %d C -> prop GC = %.2f" % (nb_G, nb_C, prop_GC))

#Ici on nous allons étudier la methode .format()
x = 32
nom = "Franck"
print("{} a {} ans".format(nom, x))

# Toujours la methode .format(), mais on constate qu'il y a un inconvénient par rapport au f.string
nb_G = 4500
nb_C = 2575
prop_GC = (nb_G + nb_C)/14800
# ici avec .format()
print("On a {} G et {} C -> prop GC = {:.2f}".format(nb_G, nb_C, prop_GC))
# Ici avec me f.string du coup beaucoup plus lisible.
print(f"On a {nb_G} G et {nb_C} C -> prop GC = {prop_GC:.2f}")
