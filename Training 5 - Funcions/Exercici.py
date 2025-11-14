def calcular_area_quadrat():
    Costat = float(input("Introdueix el costat del quadrat: ")) # Demanem el costat del quadrat a l'usuari

    Area = Costat * Costat # Calculem l'àrea del quadrat

    print("L'àrea del quadrat és: ", Area) # Imprimim el resultat a la consola


def calculs():
    a = float(input("Introdueix el primer valor: ")) # Convertim l'entrada a float per permetre nombres decimals
    b = float(input("Introdueix el segon valor: ")) # Convertim l'entrada a float per permetre nombres decimals

    print("La suma és: ", a + b) # Imprimim el resultat de la suma
    print("La resta és: ", a - b) # Imprimim el resultat de la resta
    print("La multiplicació és: ", a * b) # Imprimim el resultat de la multiplicació
    print("La divisió és: ", a / b) # Imprimim el resultat de la divisió
   
    
def CrearFrase():
    p1 = input("Introdueix la primera paraula: ") # Demanem la primera paraula a l'usuari
    p2 = input("Introdueix la segona paraula: ") # Demanem la segona paraula a l'usuari
    p3 = input("Introdueix la tercera paraula: ") # Demanem la tercera paraula a l'usuari

    print("La frase és: " + p1 + " " + p2 + " " + p3) # Imprimim la frase completa a la consola


def Decimal_Enter():
    num_1 = float(input("Introdueix el primer nombre decimal: ")) # Demanem el primer nombre decimal a l'usuari
    num_2 = float(input("Introdueix el segon nombre decimal: ")) # Demanem el segon nombre decimal a l'usuari

    suma_decimal = num_1 + num_2 # Calculem la suma dels dos nombres decimals

    suma_entera = int(suma_decimal) # Convertim la suma decimal a un nombre enter

    print("\n--- Resultat ---") # Imprimim el resultat
    print(f"Suma original (float): {suma_decimal}") # Mostrem la suma original en format float
    print(f"Suma convertida (int): **{suma_entera}**") # Mostrem la suma convertida en format int
    
    
def Edat():
    # Demana l'edat a l'usuari i la converteix a un nombre enter
    edat = int(input("Introdueix la teva edat: "))

    # Comprova si l'edat és 18 o més
    if edat >= 18:
        print("Ets major d'edat")
    else:
        print("Ets menor d'edat")   
        
        
def Nombre_major():
    # Demana els tres nombres a l'usuari
    num1 = int(input("Introdueix el primer nombre: "))
    num2 = int(input("Introdueix el segon nombre: "))
    num3 = int(input("Introdueix el tercer nombre: "))

    # Utilitza la funció max() per trobar el nombre més gran
    major = max(num1, num2, num3)

    # Mostra el resultat
    print(f"El nombre major és: {major}")
    
    
def Positiu_Negatiu():
    # Demana un nombre a l'usuari
    nombre = int(input("Introdueix un nombre enter: "))

    # Comprova si el nombre és zero o més (Positiu)
    if nombre >= 0:
        print("El nombre és positiu (o zero)")
    else:
        print("El nombre és negatiu")
    
    
def Nombres_Parells():
    print("Nombres parells entre 1 i 200:") # Imprimeix el missatge d'inici

    X = 2 # Primer nombre parell

    while X <= 200: # Bucle mentre X sigui menor o igual a 200
        print(X)
        X += 2
    # Incrementa X en 2 per obtenir el següent nombre parell


    def major():
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
        

def main():
    while True:
        print("\n--- Menú de Funcions ---")
        print("1. Calcular àrea del quadrat")
        print("2. Operacions bàsiques")
        print("3. Crear frase amb paraules")
        print("4. Suma decimal i conversió a enter")
        print("5. Comprovar edat")
        print("6. Trobar nombre major")
        print("7. Comprovar si un nombre és positiu o negatiu")
        print("8. Llistar nombres parells entre 1 i 200")
        print("9. Comprovar si hi ha nombres negatius entre 10 entrades")
        print("0. Sortir")

        opcio = input("Selecciona una opció (0-9): ")

        if opcio == '1':
            calcular_area_quadrat()
        elif opcio == '2':
            calculs()
        elif opcio == '3':
            CrearFrase()
        elif opcio == '4':
            Decimal_Enter()
        elif opcio == '5':
            Edat()
        elif opcio == '6':
            Nombre_major()
        elif opcio == '7':
            Positiu_Negatiu()
        elif opcio == '8':
            Nombres_Parells()
        elif opcio == '9':
            major()
        elif opcio == '0':
            print("Sortint del programa.")
            break
        else:
            print("Opció no vàlida. Si us plau, intenta-ho de nou.")

if __name__ == "__main__":
    main()