def main() #crea la funcion mai, que es la que estara ligada al menu
    entrada = 78 #crea la variable entrada y le asigna un valor entero aleatorio, este valor no es relevante
    while entrada != "": #inicia un bucle con while en el que ejecutara el programa en el interior asta que la variable entrada este vacia, cosa que no pasa en ningun momento por lo que el bucle continuara asta que se seleccione la obcion 4, que lo detendra con un break
        print("¿Que quiere hacer?(Introduzca el numero de la acción deseada.)") #le dice al usuario cuales son las obciones del menu
        print("1.Agregar un coche al almacen")
        print("2.Modificar un coche del almacen")
        print("3.Eliminar un coche del almacen")
        print("4.Consultar todos los coches del almacen")
        print("5.Salir del programa")
        entrada = int(input()) #recoge en la varibale entrada el valor pedido previamente como un entero, para asegurar que solo se introduzcan numeros
        if entrada == 1: #comprueba con un if si el valor de la variable entrada es igual a 1, si es asi llama a la funcion con el programa asignaado al 1, si no, pasa a la siguiente comprobación
            agregar_producto()
        elif entrada == 2: #comprueba si el valor de la variable entrada es igual a 2, si es asi llama a la funcion con el programa asignaado al 2, si no, pasa a la siguiente comprobación
            modificar_producto()
        elif entrada == 3: #comprueba si el valor de la variable entrada es igual a 3, si es asi llama a la funcion con el programa asignaado al 3, si no, pasa a la siguiente comprobación
            eliminar_producto()
        elif entrada == 4: #comprueba si el valor de la variable entrada es igual a 4, si es asi llama a la funcion con el programa asignaado al 3, si no, pasa a la siguiente comprobación
            mostrar_inventario()
        elif entrada == 5: #comprueba si el valor de la variable entrada es igual a 5, si es asi termina el bucle con un break, dando por finalizado el programa, si no, pasa al else final
            break
        else: #llegados a este punto, si el valor no a coincidido con ninguna obcion se le pide al usuario antes de que se reinicie el bucle que introduzca un valo valido
            print("entrada incorrecta, vuelvelo a intentar")
