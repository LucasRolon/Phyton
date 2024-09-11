notas=int
calificacion=float
suma=0
promedio=float

notas = int((input ("Ingrese la cantidad de notas a promediar: ")))
for i in range (notas):
 calificacion = float((input("Ingrese la calificacion: ")))
 suma=suma+calificacion
 
promedio = suma / notas
print ("El promedio de las notas es de: ", promedio)