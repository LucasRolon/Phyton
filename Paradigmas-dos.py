precio=float
preciofinal=float
descuento=float

precio = float((input("Ingrese el precio original de su producto: ")))
if precio<50 and precio>0:
 print ("Su precio final es: ", precio)
elif precio<0: 
 print ("Error ingrese un valor correcto.")
if precio >= 50 and precio<=100:
    descuento= (precio * 10) / 100
    preciofinal=precio - descuento
    print ("Su precio final es de: ", preciofinal)
else:
    descuento= (precio * 20) / 100
    preciofinal=precio - descuento
    print ("Su precio final es de: ", preciofinal)        
