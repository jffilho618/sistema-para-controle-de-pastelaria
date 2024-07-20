import abc
class Produto(abc.ABC):
    def __init__(self, nome, preco, tipo):
        self._nomenome = nome
        self._preco = preco
        self._tipo = tipo

    @abc.abstractmethod
    def calcular_preco(self):
        pass

class Bebidas(Produto):
    def __init__(self, nome, preco, volume):
        super().__init__(nome, preco, tipo)
        self._volume = volume

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

class Pastel(Produto):
    def __init__(self, nome, preco, sabor):
        super().__init__(nome, preco)
        self._sabor = sabor

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

class Acai(Produto):
    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self._peso = peso

    def calcular_preco(self):
        return self._preco * (self._peso / 100)
    
class Caixa:
    def __init__(self, produto, quantidade):
        self._produto = produto
        self._quantidade = quantidade
        self._produto = {}

    def realizar_venda(self):
        if isinstance(self._produto, Produto):
            return self._produto.calcular_preco(self._quantidade)
        else:
            raise ValueError("Produto inválido")
    
    def adicionar_produto(self, produto, quantidade):
        self._produto[produto] = quantidade
    
