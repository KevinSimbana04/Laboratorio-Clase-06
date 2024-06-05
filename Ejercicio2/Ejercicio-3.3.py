cantidadNegativos=0
suma=0
sumaTotal=0
cantidadN=10
contador=0

while contador < cantidadN:
    num = float(input("Ingrese un numero: "))
    
    if num <0:
        cantidadNegativos += 1
    
    if 1 <num and num<10:
        suma += num
    
    sumaTotal += num
    contador += 1

promedio = sumaTotal/cantidadN

print (f"La cantidad de numeros negativos es: {cantidadNegativos}")
print (f"La suma de los numeros que se encuentran entre el 1 y el 10: {suma}")
print (f"El promedio de todos los numeros: {promedio}")
