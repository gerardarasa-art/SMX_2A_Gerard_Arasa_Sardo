negatiu = False

print("Introdueix 10 nombres (enters o decimals):")

# Bucle per llegir 10 nombres
for i in range(10):
    # Demanem el nombre i el convertim directament a decimal amb el float
    nombre = float(input(f"Nombre {i + 1}: "))
    
    # Comprovem la condició per canviar la bandera
    if nombre < 0:
        # Si el nombre és menor que zero, canviem la bandera a True.
        negatiu = True
        break # Podem sortir del bucle ja que hem trobat un nombre negatiu

print("\n--- Resultat ---") # Comprovació visual

# Comprovem l'estat final de la bandera
if negatiu:
    print("Hi havia almenys un nombre negatiu.")
else:
    print("No hi ha cap nombre negatiu.")