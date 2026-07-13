class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = 0

    def actualizar_stock(self, cantidad: int):
        self.stock += cantidad
        return self.stock

    def obtener_precio_total(self, cantidad: int) -> float:
        return self.precio * cantidad