from random import randint


class Calcular:

    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 = somar, 2 = subtrair, 3 = multiplicar
        self.__resultado = self._gerar_resultado

    @property
    def dificulade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'somar'
        elif self.operacao == 2:
            op = 'subração'
        elif self.operacao == 3:
            op = 'multiplicacao'
        else:
            op = 'Operação desconhecida'
        return f"Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDficuldade: {self.dificulade} \nOperação: {op}"

    @property
    def _gerar_valor(self: object) -> int:
        pass

    @property
    def _gerar_resultado(self: object) -> int:
        pass

    @property
    def checar_resultado(self: object, resposta: int) -> bool:
        pass

    def mostrar_operacao(self: object) -> None:
        pass
