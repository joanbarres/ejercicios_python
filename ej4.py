frase = input("Introdueix una frase: ")
posicioInicial = int(input("Introdueix un numero: "))
longitud= int(input("Introdueix altre numero: "))
posicioFinal = posicioInicial+longitud

resultat = frase[posicioInicial:posicioFinal]
print("El resultat es: ", resultat)