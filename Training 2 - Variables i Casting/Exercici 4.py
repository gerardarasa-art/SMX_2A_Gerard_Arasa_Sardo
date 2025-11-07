num_1 = float(input("Introdueix el primer nombre decimal: ")) # Demanem el primer nombre decimal a l'usuari
num_2 = float(input("Introdueix el segon nombre decimal: ")) # Demanem el segon nombre decimal a l'usuari

suma_decimal = num_1 + num_2 # Calculem la suma dels dos nombres decimals

suma_entera = int(suma_decimal) # Convertim la suma decimal a un nombre enter

print("\n--- Resultat ---") # Imprimim el resultat
print(f"Suma original (float): {suma_decimal}") # Mostrem la suma original en format float
print(f"Suma convertida (int): **{suma_entera}**") # Mostrem la suma convertida en format int