import abc
import random
from datetime import datetime

def menu_principal():
    print("╔══════════════════════════════════════╗")
    print("║               D'GUSTA                ║")
    print("╠══════════════════════════════════════╣")
    print("║ [1] CADASTRAR PRODUTO                ║")
    print("║ [2] EDITAR PRODUTO                   ║")
    print("║ [3] REMOVER PRODUTO                  ║")
    print("║ [4] REGISTRAR VENDA                  ║")
    print("║ [5] HISTÓRICO DE VENDAS              ║")
    print("║ [6] IMPRIMIR CARDÁPIO                ║")
    print("║ [0] SAIR                             ║")
    print("╚══════════════════════════════════════╝\n")

def menu_cadastro():
    print("╔══════════════════════════════════════╗")
    print("║            MENU CADASTRO             ║")
    print("╠══════════════════════════════════════╣")
    print("║ [1] PASTEL                           ║")
    print("║ [2] BEBIDA                           ║")
    print("║ [0] MENU ANTERIOR                    ║")
    print("╚══════════════════════════════════════╝\n")

def menu_venda():
    print("╔══════════════════════════════════════╗")
    print("║             MENU VENDAS              ║")
    print("╠══════════════════════════════════════╣")
    print("║ [1] PASTEL                           ║")
    print("║ [2] BEBIDA                           ║")
    print("║ [3] AÇAI                             ║")
    print("║ [4] SORVETE                          ║")
    print("║ [0] REGISTRAR VENDA                  ║")
    print("╚══════════════════════════════════════╝\n")

class Produto(abc.ABC):
    def __init__(self, nome, preco, unidade):
        self._nome = nome
        self._preco = preco
        self._unidade = unidade

    @abc.abstractmethod
    def calcular_preco(self, quantidade):
        pass

    @abc.abstractmethod
    def editar(self):
        pass

class Bebidas(Produto):
    def __init__(self, nome, preco, unidade = "UNI"):
        super().__init__(nome, preco, unidade)

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

    def editar(self):
        self._nome = input("DIGITE O NOVO NOME DA BEBIDA: ").upper()
        self._preco = float(input("DIGITE O NOVO PREÇO DA BEBIDA: "))

class Pastel(Produto):
    def __init__(self, nome, preco, unidade = "UNI"):
        super().__init__(nome, preco, unidade)

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

    def editar(self):
        self._nome = input("DIGITE O NOVO NOME DO PASTEL: ").upper()
        self._preco = float(input("DIGITE O NOVO PREÇO DO PASTEL: "))

class Acai(Produto):
    def __init__(self, preco, nome):
        super().__init__("AÇAI", preco, "KG")

    def calcular_preco(self, peso):
        return self._preco * (peso / 1000)

    def editar(self):
        self._preco = float(input("DIGITE O NOVO PREÇO DO AÇAI: "))

class Sorvete(Produto):
    def __init__(self, preco, nome):
        super().__init__("SORVETE", preco, "KG")

    def calcular_preco(self, peso):
        return self._preco * (peso / 1000)

    def editar(self):
        self._preco = float(input("DIGITE O NOVO PREÇO DO SORVETE: "))

class Pedido:
    def __init__(self, cliente):
        self._cliente = cliente
        self._produtos = []
        self._id_pedido = random.randint(1000, 9999)
        self._data = datetime.now()

    def adicionar_produto(self, produto, quantidade, tipo_produto):
        self._produtos.append((produto, quantidade, tipo_produto))

    def calcular_total(self):
        total = 0
        for produto, quantidade, tipo_produto in self._produtos:
            total += produto.calcular_preco(quantidade)
        return total

    def imprimir_nota(self):
        print("\n")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                         NOTA FISCAL                          ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print(f"║ ID DO PEDIDO: {self._id_pedido:<47}║")
        print(f"║ NOME DO CLIENTE: {self._cliente:<44}║")
        print(f"║ DATA DO PEDIDO: {self._data.strftime('%d/%m/%Y'):<45}║")
        print(f"║ HORA DO PEDIDO: {self._data.strftime('%H:%M:%S'):<45}║")
        print("╠══════════════════════════════════════════════════════════════╣")
        for produto, quantidade, tipo_produto in self._produtos:
            print(f"║ {tipo_produto:<7} {produto._nome:32} QUANT: {quantidade:<2}  {produto.calcular_preco(quantidade):>5.2f} R$ ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print(f"║ TOTAL: {self.calcular_total():>50.2f} R$ ║")
        print("╚══════════════════════════════════════════════════════════════╝\n")


class Caixa:
    def __init__(self):
        self._produtos = {
            'PASTEL': [],
            'BEBIDA': [],
            'AÇAI': [],
            'SORVETE': []

        }
        self._pedidos = []

    def adicionar_produto(self, produto):
        if isinstance(produto, Pastel):
            self._produtos['PASTEL'].append(produto)
        elif isinstance(produto, Bebidas):
            self._produtos['BEBIDA'].append(produto)
        elif isinstance(produto, Acai):
            self._produtos['AÇAI'].append(produto)
        elif isinstance(produto, Sorvete):
            self._produtos['SORVETE'].append(produto)

    def editar_produto(self, nome_produto):
        for tipo, lista_produtos in self._produtos.items():
            for produto in lista_produtos:
                if produto._nome == nome_produto:
                    produto.editar()
                    print(f"{tipo} EDITADO COM SUCESSO!")
                    return
        print("PRODUTO NÃO ENCONTRADO!")

    def remover_produto(self, nome_produto):
        for tipo, lista_produtos in self._produtos.items():
            for produto in lista_produtos:
                if produto._nome == nome_produto:
                    lista_produtos.remove(produto)
                    print(f"{tipo} REMOVIDO COM SUCESSO!")
                    return
        print("PRODUTO NÃO ENCONTRADO!")

    def registrar_venda(self):
        nome_cliente = input("DIGITE O NOME DO CLIENTE: ").upper()
        pedido = Pedido(nome_cliente)

        while True:
            menu_venda()
            op3 = int(input("DIGITE A OPÇÃO DESEJADA: "))
            if op3 == 0:
                break
            elif op3 in [1, 2, 3, 4]:
                tipo_produto = {1: 'PASTEL', 2: 'BEBIDA', 3: 'AÇAI', 4: 'SORVETE'}[op3]
                if not self._produtos[tipo_produto]:
                    print(f"SEM {tipo_produto} DISPONÍVEIS NO MOMENTO")
                    continue
                cont = 1
                print(f"{tipo_produto}")
                for produto in self._produtos[tipo_produto]:
                    print(f"{cont} - {produto._nome} - R${produto._preco}")
                    cont += 1
                while True:
                    op4 = int(input(f"DIGITE O NÚMERO DO {tipo_produto} DESEJADO: ")) - 1
                    if 0 <= op4 < len(self._produtos[tipo_produto]):
                        break
                    else:
                        print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                quantidade = int(input("DIGITE A QUANTIDADE DESEJADA: "))
                pedido.adicionar_produto(self._produtos[tipo_produto][op4], quantidade, tipo_produto)
        pedido.imprimir_nota()
        confirmar = input("DESEJA REALIZAR A VENDA? (S/N): ").upper()
        if confirmar == 'S':
            self._pedidos.append(pedido)
            print("VENDA REALIZADA COM SUCESSO!")
        else:
            print("VENDA CANCELADA!")

    def imprimir_cardapio(self):
        print("\n╔═══════════════════════════════════════╗")
        print("║               CARDÁPIO                ║")
        print("╚═══════════════════════════════════════╝")

        for tipo, lista_produtos in self._produtos.items():
            print(f"{tipo.upper()}")
            print("╔═════════════════════════════════════════════════╗")
            print("║              NOME            ║ PREÇO  ║ UNIDADE ║")
            print("╠═════════════════════════════════════════════════╣")
            for produto in lista_produtos:
                print(f"║ {produto._nome:28} ║ {produto._preco:6.2f} ║ {produto._unidade:7} ║")
            print("╚═════════════════════════════════════════════════╝\n")

def main():
    caixa = Caixa()
    ac = Acai(59, "AÇAI")
    sv = Sorvete(45, "SORVETE")
    misto = Pastel("MISTO", 10)
    coca = Bebidas("COCA 350ml", 5)
    caixa.adicionar_produto(ac)
    caixa.adicionar_produto(sv)
    caixa.adicionar_produto(misto)
    caixa.adicionar_produto(coca)
    op = 11
    while op != 0:
        menu_principal()
        op = int(input("DIGITE A OPÇÃO DESEJADA: "))
        match op:
            case 1:
                menu_cadastro()
                op2 = int(input("DIGITE A OPÇÃO DESEJADA: "))
                match op2:
                    case 1:
                        nome = input("DIGITE O NOME DO PASTEL: ").upper()
                        preco = float(input("DIGITE O PREÇO DO PASTEL: "))
                        pastel = Pastel(nome, preco)
                        caixa.adicionar_produto(pastel)
                    case 2:
                        nome = input("DIGITE O NOME DA BEBIDA: ").upper()
                        preco = float(input("DIGITE O PREÇO DA BEBIDA: "))
                        bebida = Bebidas(nome, preco)
                        caixa.adicionar_produto(bebida)
            case 2:
                nome_produto = input("DIGITE O NOME DO PRODUTO QUE DESEJA EDITAR: ").upper()
                caixa.editar_produto(nome_produto)
            case 3:
                nome_produto = input("DIGITE O NOME DO PRODUTO QUE DESEJA REMOVER: ").upper()
                caixa.remover_produto(nome_produto)
            case 4:
                caixa.registrar_venda()
            case 5:
                pass
            case 6:
                caixa.imprimir_cardapio()
            case 0:
                print("SAINDO...")
            case _:
                print("OPÇÃO INVÁLIDA")
                continue

if __name__ == "__main__":
    main()
