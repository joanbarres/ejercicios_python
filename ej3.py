cadena = input("Introdueix una cadena de caracters:")

primers_caracters = cadena[0:3]
ultims_caracters = cadena[len(cadena)-3:]
resultat = primers_caracters + ultims_caracters
print(resultat)