def programa_numero():
    
    numero_a = int(input("> Ingrese un número: "))
    numero_n = 0
    
    comprobacion = True
    
    while comprobacion == True:
        numero_n = int(input("> Ingrese otro número: "))
        
        if numero_n < numero_a:
            numero_a = numero_n
        elif numero_n >= numero_a:
            comprobacion = False
        else:
            pass
            
    

if __name__ == "__main__":
    programa_numero()