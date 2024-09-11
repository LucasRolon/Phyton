temperatura=float
lluvia = str
temperatura = float((input("Ingrese la temperatura en Celsius: ")))
lluvia = str((input("Se espera lluvia para hoy S/N: ")))

if lluvia == 'N' and temperatura <= 15.00:
    print ("El clima está un poco frío, recomendamos este atuendo: ")
    print ("1. Camiseta larga. ")
    print ("2. Campera abrigada. ")
    print ("3. Pantalón largo. ")
    print ("4. Zapatillas. ")
elif lluvia == 'N' and temperatura > 15.00:
    print ("El clima está agradable, recomendamos este atuendo: ")
    print ("1. Camiseta corta. ")
    print ("2. Campera liviana. ")
    print ("3. Pantalón largo. ")
    print ("4. Zapatillas. ")
elif lluvia == 'S' and temperatura < 15.00:
    print ("Parece que puede llover en cualquier momento, recomendamos este atuendo: ")
    print ("1. Camiseta larga. ")
    print ("2. Campera abrigada. ")
    print ("3. Pantalón largo. ")
    print ("4. Botas de lluvia. ")
    print ("5. Guantes")
elif lluvia == 'S' and temperatura >= 15.00:
    print ("El clima está agradable pero hay posibilidad de lluvia! Recomendamos este atuendo: ")
    print ("1. Camiseta corta. ")
    print ("2. Buzo liviano. ")
    print ("3. Pantalón largo. ")
    print ("4. Zapatillas. ")
else:
    print("Error") 
