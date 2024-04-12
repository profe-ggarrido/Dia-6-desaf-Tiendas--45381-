from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

def main():
    print("Bienvenido al sistema de tiendas")
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de entrega: "))

    tipo_tienda = input("Seleccione el tipo de tienda (Restaurante/Supermercado/Farmacia): ")
    if tipo_tienda.lower() == "restaurante":
        tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "supermercado":
        tienda = Supermercado(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "farmacia":
        tienda = Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda inválido")
        return

    while True:
        print("\nMenu:")
        print("1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto (opcional, default 0): ") or "0")
            producto = Producto(nombre, precio, stock)
            tienda.ingresar_producto(producto)
            print("Producto ingresado exitosamente.")
        elif opcion == "2":
            print(tienda.listar_productos())
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            print(tienda.realizar_venta(nombre_producto, cantidad))
        elif opcion == "4":
            print("******* G A M E    O V E R **********")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()