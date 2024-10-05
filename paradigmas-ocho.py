# Control de inventario de una tienda, con sus respectivos stocks, el programa deberá permitir transacciones como "Compra" o "Venta"
# varias veces sin detenerse. Y al final mostrar las cantidades de esos productos.
estado=int
inventario = int
ropavestir=int
ropavestir=1
pantalones=int
pantalones=1
camisetas=int
camisetas=1
vestidos=int
vestidos=1

while inventario!=0:
    print("0. Salir. ")
    print ("1. Ropa de vestir. ")
    print("2. Pantalones. ")
    print("3. Camisetas. ")
    print("4. Vestidos. ")
    inventario = int((input("Ingrese el nombre del producto: ")))
    if inventario!=0:
        print("1. Compra.")
        print("2. Venta.")
        estado = int((input("Ingrese su transaccion: ")))
#------------ COMPRA ---------------
    if estado==1 and inventario ==1:
        ropavestir=ropavestir+1
    if estado==1 and inventario ==2:
        pantalones=pantalones+1
    if estado==1 and inventario ==3:
        camisetas=camisetas+1
    if estado==1 and inventario == 4:
        vestidos=vestidos+1
#----------- VENTA -----------------
    if estado==2 and inventario==1:
        ropavestir=ropavestir-1
        if ropavestir <= -1:
            print("El producto deseado no se encuentra en stock. ")
            ropavestir=0
    if estado==2 and inventario == 2:
        pantalones=pantalones-1
        if pantalones <= -1:
            print("El producto deseado no se encuentra en stock. ")
            pantalones=0
    if estado==2 and inventario ==3:
        camisetas=camisetas-1
        if camisetas <= -1:
            print("El producto deseado no se encuentra en stock. ")
            camisetas=0
    if estado==2 and inventario == 4:
        vestidos=vestidos-1
        if vestidos <= -1:
            print("El producto deseado no se encuentra en stock. ")
            vestidos=0

print("El total de ropa de vestir es de: ", ropavestir)
print("El total de ropa de vestir es de: pantalones", pantalones)
print("El total de ropa de vestir es de: camisetas", camisetas)
print("El total de ropa de vestir es de: vestidos", vestidos)
