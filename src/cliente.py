class Cliente:
    def __init__(self, cedula: str, nombre: str, email: str):
        self.cedula = cedula
        self.nombre = nombre
        self.email = email
        self.compras_realizadas = []

    def registrar_compra(self, detalle_compra: str):
        self.compras_realizadas.append(detalle_compra)
        return f"Compra registrada para {self.nombre}"

    def obtener_perfil(self) -> str:
        return f"Cliente: {self.nombre} | Email: {self.email}"