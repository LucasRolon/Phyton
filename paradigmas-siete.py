# Reserva de mesas en un restaurante, para determinado grupo de personas. Las mesas estarán compuestas por, grupos de dos, cuatro, seis y ocho personas.

personas = int
mesadoble=int
mesadoble=2
mesacuatro=int
mesacuatro=2
mesaseis=int
mesaseis=2
mesaocho=int
mesaocho=2

while personas !=0:
    print ("Mesas de dos personas disponibles: ", mesadoble)
    print ("Mesas de cuatro personas disponibles: ", mesacuatro)
    print ("Mesas de seis personas disponibles: ", mesaseis)
    print ("Mesas de ocho personas disponibles: ", mesaocho)
    print ("0. Salir. ")
    personas=int(input("Ingrese el tamaño de su grupo: "))
    if personas < 0:
        print("Error, opción incorrecta. ")
    if personas > 0 and personas <= 2:
        mesadoble=mesadoble-1
        if mesadoble <= -1:
            print("No nos quedan mesas de dos personas disponibles. ")
            mesadoble=0
    if personas > 2 and personas <= 4:
        mesacuatro=mesacuatro-1
        if mesacuatro <=-1:
            print ("No nos quedan mesas de cuatro disponibles. ")
            mesacuatro=0
    if personas > 4 and personas <= 6:
        mesaseis=mesaseis-1
        if mesaseis <= -1:
            print("No nos quedan mesas de seis personas disponibles. ")
            mesaseis=0
    if personas > 6 and personas <= 8:
        mesaocho=mesaocho-1
        if mesaocho <= -1:
            print("No nos quedan mesas de ocho personas disponibles. ")
            mesaocho=0
    if personas > 8:
        print("Lo sentimos, no disponemos de mesas para el grupo indicado. ")
