# Si trobem un 10, la canviarem a True.
deu_trobat = False

# Lectura de la primera nota.
# El programa s'aturarà aquí esperant una entrada de l'usuari.
print("Introdueix una nota (0-10) o -1 per finalitzar:")
nota = int(input())

# Bucle principal: continuarà mentre la nota llegida NO sigui -1.
while nota != -1:
    
    # Comprovem si la nota actual és un 10.
    if nota == 10:
        # Trobem el primer 10, ja no cal canviar aquesta variable més.
        deu_trobat = True
    
    # Lectura de la següent nota per a la pròxima iteració.
    print("Introdueix la següent nota (0-10) o -1 per finalitzar:")
    nota = int(input())

# Fi del bucle. S'ha llegit el -1.

# Comprovació del resultat final només amb 'if' i 'else'.
if deu_trobat == True:
    print("Hi ha hagut alguna nota que té un 10")
else:
    print("No hi ha cap 10")