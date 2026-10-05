class Venta:
    def __init__(self, identificador, usuario_id, producto_codigo, fecha):

        self.identificador = identificador
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.fecha = fecha
        
    @staticmethod
    def validar_texto(valor, campo):
        if not valor or not valor.strip():
            raise ValueError(f"El campo {campo} no puede estar vacio.")

        return valor.strip()

    @property
    def identificador(self):
        return self._identificador

    @identificador.setter
    def identificador(self, valor):
        self._identificador = self.validar_texto(valor,"identificador")
        
    @property
    def usuario_id(self) -> str:
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, valor: str) -> None:
        self._usuario_id = self.validar_texto(valor, "usuario_id")

    @property
    def producto_codigo(self) -> str:
        return self._producto_codigo

    @producto_codigo.setter
    def producto_codigo(self, valor: str) -> None:
        self._producto_codigo = self.validar_texto(valor, "producto_codigo")

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = self.validar_texto(valor, "fecha")

