temperatura=float

temperatura = float((input("Ingrese la temperatura en Celsius: ")))

if temperatura<0:
 print ("Su temperatura corresponde a la categoría: Congelante.")
if temperatura >= 0 and temperatura <= 15:
    print ("Su temperatura es: Fría. ")
if temperatura >= 16 and temperatura <= 25:
    print ("Su temperatura es: Templada. ")
if temperatura >= 25:
    print ("Su temperatura es: Cálida. ")
