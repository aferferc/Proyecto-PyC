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

def agregar_producto(): #crea la funcion agragar producto
    marca = str(input("introduce la marca del coche")) #asigna a la variable marca un valor str dado por el usuario en un input
    modelo = str(input("introduce el modelo del coche")) #asigna a la variable modelo un valor str dado por el usuario en un input
    color = str(input("Introduce el color del Coche")) #asigna a la variable color un valor str dado por el usuario en un input
    potencia = int(input("Introduce la potencia del coche en HP")) #asigna a la variable potencia un valor int dado por el usuario en un input
    eje_tracción = str(input("Introduce el eje de tracción del Coche")) #asigna a la variable eje_tracción un valor str dado por el usuario en un input
    tipo_carroceria = str(input("Introduce el tipo de carroceria del Coche")) #asigna a la variable eje_tracción un valor str dado por el usuario en un input
    precio = float(input("Introduce el precio del coche")) #asigna a la variable precio un valor float dado por el usuario en un input

    for i in inventario: #antes de pasar a la parte del codigo de la funcion que agregara el cohe a el inventario, como el maestro dijo que no hubiese objetos repetidos, se crea un bucle en el que se compruba si la marca y el modelo del coche que emos registrado coincide cocon algunos de los objetos guardados en inventario, si es asi, se le dice al usuario que ya hay un producto asi registrado y se detiene a la funcion con return
        if i.modelo == modelo and i.marca == marca:
            print("Ya hay un coche asi registrado")
            return
    inventario.append(veiculo(color, potencia, tipo_carroceria, precio, marca, modelo)) #se añaden los datos del coche a el inventario, que es una lista, con append. 
    print("Se a agregado el coche al inventario") #se le dice a el usuario que el coche se a agregado al inventario.


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
