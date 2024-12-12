class veiculo(): #creacion de la clase para el producto, en este caso un veiculo
    def __init__(self, color, potencia, tipo_carroceria, eje_traccion, precio, marca, modelo): #creacion del constructor asignando las variables externas que contienen los atributos
        self.color = color #creacion del atributo color a traves de la variable externa color
        self.potencia = potencia #creacion del atributo potencia a traves de la variable externa potencia
        self.tipo_carroceria = tipo_carroceria #creacion del tipo_carroceria color a traves de la variable externa tipo_carroceria
        self.eje_traccion = eje_traccion #creacion del atributo eje_traccion a traves de la variable externa eje_traccion
        self.precio = precio #creacion del atributo precio a traves de la variable externa precio
        self.marca = marca #creacion del atributo marca a traves de la variable externa marca
        self.modelo = modelo #creacion del atributo modelo a traves de la variable externa modelo

    def.descripcion(self):
        return f"Especificaciones: {self.marca} {self.modelo}, Carroceria: {self.tipo_carroceria}, Color: {self.color}, Potencia: {self.potencia}, Traccion: {self.eje_traccion}"

inventario = [] #crea la variable inventario asignandole una lista vacia



def main(): #crea la funcion mai, que es la que estara ligada al menu
    while True: #Inicia un bucle infinitro asignando un valor buleano
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
if __name__ == "__main__": #comprueba si el nombre de la funcion es main, si es asi llama la funcion main, esto es solo para llamar a la funcion main cuando inicia el programa
    main()
