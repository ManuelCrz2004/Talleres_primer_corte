def fibonacci(limite):
    
    lista_fibonacci = [0, 1]
    suma_interna = sum(lista_fibonacci)
    i = 0
    comprobante = False
    
    while comprobante == False:
        
        
        if suma_interna >= limite:
            comprobante = True
            return lista_fibonacci
        else:
            lista_fibonacci.append((lista_fibonacci[i] + lista_fibonacci[i+1]))
            i +=1
        
        
    

if __name__ == "__main__":
    x = int(input("> Limite entero arbitrario: "))
    fibonacci(x)