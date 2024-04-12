class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    def aumentar_stock(self, cantidad):
        self.__stock += cantidad

    def disminuir_stock(self, cantidad):
        if self.__stock - cantidad < 0:
            self.__stock = 0
        else:
            self.__stock -= cantidad

    def __eq__(self, other):
        return self.__nombre == other.__nombre

    def __add__(self, other):
        if self == other:
            self.aumentar_stock(other.__stock)
            return self
        else:
            raise ValueError("No se puede sumar productos diferentes")

    def __sub__(self, other):
        if self == other:
            self.disminuir_stock(other.__stock)
            return self
        else:
            raise ValueError("No se puede restar productos diferentes")