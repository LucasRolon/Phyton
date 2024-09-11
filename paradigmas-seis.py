numeros=int
num=int
impar=0
par=0

numeros = int((input ("Ingrese la cantidad de numeros: ")))
for i in range (numeros):
 num = float((input("Ingrese un numero: ")))
 if num % 2 == 0:
    par=par+1
 if num % 2 != 0:
    impar=impar+1

print ("La cantidad de numeros pares es de: ", par)
print ("La cantidad de numeros impares es de: ", impar)