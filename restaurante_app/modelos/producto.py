class Producto:

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    @staticmethod
    def validar_texto(valor, campo):
        # Reutiliza una validacion basica para datos obligatorios.
        if not valor or not valor.strip():
            raise ValueError(f"El campo {campo} no puede estar vacio.")
        return valor.strip()

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        self._codigo = self.validar_texto(valor, "codigo")

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self._nombre = self.validar_texto(valor,"nombre")

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        self._categoria = self.validar_texto(valor,"categoria")

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        try:
            precio = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser numerico.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self._precio = precio

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int) -> None:

        try:
            stock = int(valor)

        except (TypeError, ValueError):
            raise ValueError("El stock debe ser un numero entero.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self._stock = stock

    @property
    def estado(self) -> str:

        if self.stock > 0:
            return f"Stock disponible: {self.stock}"

        return "Sin stock"
