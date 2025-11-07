negatiu = False
i = 0

print("Introdueix 10 nombres:")

# Bucle while que es repeteix 10 vegades (mentre i < 10)
while i < 10:
    # Demanem el nombre a l'usuari
    nombre = int(input(f"Introdueix el nombre {i+1} de 10: "))

    # Comprovem si el nombre és negatiu
    if nombre < 0:
        negatiu = True
        break  # Sortim del bucle immediatament

    i += 1
# Després del bucle, comprovem si hi havia algun nombre negatiu
if negatiu:
    print("Hi havia almenys un nombre negatiu")
else:
    print("No hi ha cap nombre negatiu")