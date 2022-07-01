import random
import time

f = open(r"C:\Users\alumno\Desktop\palabras.txt", "r")
listaPalabras = f.readlines()
f.close()

lista = []
for s in listaPalabras:
    lista.append(s[:-1])    

palabra = []
eleccion = 0
while eleccion == 0:
    dificultad = input("Elija un nivel de dificultad(1, 2 o 3): ")
    if int(dificultad) == 1:
        palabra = random.choice(lista)
        intentos = 10000
        while len(palabra) != 4:
            palabra = random.choice(lista)
    elif int(dificultad) == 2:
        palabra = random.choice(lista)
        intentos = 7
        while len(palabra) != 5:
            palabra = random.choice(lista)
    elif int(dificultad) == 3:
        palabra = random.choice(lista)
        intentos = 5
        while len(palabra) != 6:
            palabra = random.choice(lista)

    

    palabraIngresada = input("Ingrese una palabra: ")
    start = time.perf_counter()
    start = start/1000
    print("tiempo inicio: ", start)


    terminar = 0
    while terminar == 0:
        guiones = ""
        i=0
        while i < len(palabra):
            if len(palabra) != len(palabraIngresada):
                if int(dificultad) == 1:
                    print("La palabra debe tener solo 4 caracteres. Vuelve a intentarlo.")
                elif int(dificultad) == 2:
                    print("La palabra debe tener solo 5 caracteres. Vuelve a intentarlo.")
                elif int(dificultad) == 3:
                    print("La palabra debe tener solo 6 caracteres. Vuelve a intentarlo.")
                palabraIngresada = ""
                palabraIngresada = input("Ingrese una palabra: ")

            if palabra[i] == palabraIngresada[i]:
                guiones += "="

            elif palabraIngresada[i] in palabra:
                guiones += "-"
                
            else:
                guiones += " "
            i += 1
        
        print(palabraIngresada)
        print(guiones) 

        
        if palabra != palabraIngresada:
            intentos = intentos - 1
            palabraIngresada = ""
            palabraIngresada = input("Ingrese otra palabra: ")

        if intentos == 0:
            terminar = 1
            print("Te quedaste sin intentos! :( ")
            rta = input("Queres volver a jugar? (si o no): ")
            if rta == "si":
                eleccion = 0
            else:
                print("Gracias por jugar!")
                eleccion = 1

        if palabraIngresada == palabra:
            terminar = 1
            print("Muy Bien! Adivinaste la palabra!")
            end = time.perf_counter()
            end = end/1000
            print("tiempo fin: ", end)
            print("transcurrió: ", end - start)
            rta = input("Queres volver a jugar? (si o no): ")
            if rta == "si":
                eleccion = 0
            else:
                print("Gracias por jugar!")
                eleccion = 1

    
        
   
        
