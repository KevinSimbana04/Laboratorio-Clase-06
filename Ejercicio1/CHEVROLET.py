contadorTalleres=0
numTalleres=1
while numTalleres <=3:
    print (f'¿El taller {numTalleres} tiene alguna fuga de gas?')
    estadoTaller= input("Ingrese si o no: ")
    if estadoTaller== "si":
        contadorTalleres+=1
    numTalleres +=1
if contadorTalleres>1 :
    print("ALERTA EXISTE UNA FUGA DE GAS")

#CHEVROLET for

contadorTalleres=0
for i in range (1,4):
    print (f'¿El taller {i} tiene alguna fuga de gas?')
    estadoTaller= input("Ingrese si o no: ")
    if estadoTaller=='si':
        contadorTalleres+=1

if contadorTalleres>1:
    print("ALERTA EXISTE UNA FUGA DE GAS")
