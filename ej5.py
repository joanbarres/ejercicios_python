frase = input("Introdueix un frase:")
lletraRemplaçada = input("Introdueix una lletra per remplaçar en la frase: ")
lletraRemplaçadora = input("Introdueix la lletra per la que vols remplaçarla: ")
contadorLLetra = frase.count(lletraRemplaçada)
resultat = frase.replace(lletraRemplaçada, lletraRemplaçadora)

print("\nNombre de vegades que la lletra apareix:", contadorLLetra)
print("Frase despres del reemplaçament:", resultat)
