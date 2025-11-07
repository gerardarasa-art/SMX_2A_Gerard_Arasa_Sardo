# Demana els tres nombres a l'usuari
num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))
num3 = int(input("Introdueix el tercer nombre: "))

# Utilitza la funció max() per trobar el nombre més gran
major = max(num1, num2, num3)

# Mostra el resultat
print(f"El nombre major és: {major}")