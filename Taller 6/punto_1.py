import random

def multiplicacion(x):
    for i in range(x):
        numero_1 = random.randint(2, 10)
        numero_2 = random.randint(2, 10)
        
        respuesta = int(input(f"¿Cuanto es {numero_1} x {numero_2}? "))
        
        if respuesta == (numero_1 * numero_2):
            print("¡Respuesta Correcta!")
        else:
            print("Respuesta incorrecta")
    

if __name__ == "__main__":
    numero = int(input("> Ingrese el numero de multiplicaciones que desea realizar: \n>"))
    multiplicacion(numero)