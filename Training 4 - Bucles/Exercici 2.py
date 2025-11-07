deu = False
nota = 0  # Pot ser qualsevol valor diferent de -1

print("Introdueix notes (de 0 a 10). Introdueix -1 per finalitzar.")

while nota != -1:
    nota = int(input("Introdueix una nota (de 0 a 10): ")) # Demana la nota a l'usuari

    if nota == 10: # Si la nota és 10
        deu = True

if deu: # Després del bucle, mostrem el resultat
    print("Hi ha hagut alguna nota que té un 10")
else:
    print("No hi ha cap 10")
# Fi del programa