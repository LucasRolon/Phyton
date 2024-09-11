kilometros=int
tiempo=float

kilometros = int((input("Ingrese su distancia recorrida en KM: ")))
tiempo = float((input("Ingrese el tiempo recorrido en minutos: ")))

if kilometros >= 11 and tiempo >= 60:
 print ("Su ritmo es: Rápido.")
elif kilometros <= 10 and tiempo <= 60:
    print ("Su ritmo es: moderado.")
elif kilometros <= 6 and tiempo <= 60:
    print ("Su ritmo es: lento. ")