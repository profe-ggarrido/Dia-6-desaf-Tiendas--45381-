from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self._nombre = nombre
        self._costo_delivery = costo_delivery
        self._productos = []

    def ingresar_producto(self, producto):
        for i, p in enumerate(self._productos):
            if p == producto:
                self._productos[i] += producto
                return
        self._productos.append(producto)

    def listar_productos(self):
        return "\n".join([f"{p.nombre} - Precio: {p.precio} - Stock: {p.stock}" for p in self._productos])

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self._productos:
            if producto.nombre == nombre_producto:
                producto.disminuir_stock(cantidad)
                return f"Venta realizada de {cantidad} unidades de {producto.nombre}"
        return f"El producto {nombre_producto} no se encuentra en la tienda"

class Restaurante(Tienda):
    def ingresar_producto(self, producto):
        producto.stock = 0
        self._productos.append(producto)

    def listar_productos(self):
        return "\n".join([f"{p.nombre} - Precio: {p.precio}" for p in self._productos])

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self._productos:
            if producto.nombre == nombre_producto:
                return f"Venta realizada de {cantidad} unidades de {producto.nombre}"
        return f"El producto {nombre_producto} no se encuentra en la tienda"

class Supermercado(Tienda):
    def listar_productos(self):
        return "\n".join([f"{p.nombre} - Precio: {p.precio} - Stock: {p.stock} {'Pocos productos disponibles' if p.stock < 10 else ''}" for p in self._productos])

class Farmacia(Tienda):
    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self._productos:
            if producto.nombre == nombre_producto:
                if cantidad > 3:
                    return "No se puede vender más de 3 unidades por producto"
                producto.disminuir_stock(cantidad)
                return f"Venta realizada de {cantidad} unidades de {producto.nombre}"
        return f"El producto {nombre_producto} no se encuentra en la tienda"

    def listar_productos(self):
        return "\n".join([f"{p.nombre} - Precio: {p.precio} {'Envío gratis al solicitar este producto' if p.precio > 15000 else ''} - Stock: {p.stock}" for p in self._productos])