import abc
import random
from datetime import datetime, time

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

def menu_historico():
    print("╔══════════════════════════════════════╗")
    print("║               HISTORICO              ║")
    print("╠══════════════════════════════════════╣")
    print("║ [1] TODAS AS COMPRAS DE UM CLIENTE   ║")
    print("║ [2] TODAS AS COMPRAS EM UM PERIODO   ║")
    print("║ [3] HISTÓRICO COMPLETO               ║")
    print("║ [4] VENDA ESPECÍFICA                 ║")
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
    print("║ [5] CUZCUZ                           ║")
    print("║ [6] MASSA                            ║")
    print("║ [7] PETISCO                          ║")
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
        try:
            self._nome = input("DIGITE O NOVO NOME DA BEBIDA: ").upper()
            self._preco = float(input("DIGITE O NOVO PREÇO DA BEBIDA: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Pastel(Produto):
    def __init__(self, nome, preco, unidade = "UNI"):
        super().__init__(nome, preco, unidade)

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

    def editar(self):
        try:
            self._nome = input("DIGITE O NOVO NOME DO PASTEL: ").upper()
            self._preco = float(input("DIGITE O NOVO PREÇO DO PASTEL: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Acai(Produto):
    def __init__(self, preco, nome):
        super().__init__("AÇAI", preco, "KG")

    def calcular_preco(self, peso):
        return self._preco * (peso / 1000)

    def editar(self):
        try:
            self._preco = float(input("DIGITE O NOVO PREÇO DO AÇAI: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Sorvete(Produto):
    def __init__(self, preco, nome):
        super().__init__("SORVETE", preco, "KG")

    def calcular_preco(self, peso):
        return self._preco * (peso / 1000)

    def editar(self):
        try:
            self._preco = float(input("DIGITE O NOVO PREÇO DO SORVETE: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Cuzcuz(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco, "UNI") 

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

    def editar(self):
        try:
            self._preco = float(input("DIGITE O NOVO PREÇO DO CUZCUZ: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Massa(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco, 'UNI')

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

    def editar(self):
        try:
            self._preco = float(input("DIGITE O NOVO PREÇO DA MASSA: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Petisco(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco, 'UNI')

    def calcular_preco(self, quantidade):
        return self._preco * quantidade

    def editar(self):
        try:
            self._preco = float(input("DIGITE O NOVO PREÇO DO PETISCO: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um valor numérico para o preço.")

class Pedido:
    def __init__(self, cliente):
        self._cliente = cliente
        self._produtos = []
        self._id_pedido = random.randint(1000, 9999)
        now = datetime.now()
        self._data = now.toordinal()  # Convertendo para data Juliana
        self._hora = now.time()  # Armazenando a hora

    def adicionar_produto(self, produto, quantidade, tipo_produto):
        self._produtos.append((produto, quantidade, tipo_produto))

    def calcular_total(self):
        total = 0
        for produto, quantidade, tipo_produto in self._produtos:
            total += produto.calcular_preco(quantidade)
        return total

    def imprimir_nota(self):
        data_gregoriana = datetime.fromordinal(self._data)  # Convertendo de volta para data Gregoriana
        print("\n")
        print("╔══════════════════════════════════════════════════════════════════════════════════╗")
        print("║                                    NOTA FISCAL                                   ║")
        print("╠══════════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ ID DO PEDIDO: {self._id_pedido:<65}  ║")
        print(f"║ NOME DO CLIENTE: {self._cliente:<62}  ║")
        print(f"║ DATA DO PEDIDO: {data_gregoriana.strftime('%d/%m/%Y'):<63}  ║")
        print(f"║ HORA DO PEDIDO: {self._hora.strftime('%H:%M:%S'):<63}  ║")
        print("╠══════════════════════════════════════════════════════════════════════════════════╣")
        for produto, quantidade, tipo_produto in self._produtos:
            if tipo_produto == "AÇAI" or tipo_produto == "SORVETE":
                print(f"║ {tipo_produto:<7} {produto._nome:50} PESO: {quantidade:<4}g  {produto.calcular_preco(quantidade):>5.2f} R$ ║")
            else:
                print(f"║ {tipo_produto:<7} {produto._nome:50} QUANT: {quantidade:<4}  {produto.calcular_preco(quantidade):>5.2f} R$ ║")
        print("╠══════════════════════════════════════════════════════════════════════════════════╣")
        print(f"║ TOTAL: {self.calcular_total():>70.2f} R$ ║")
        print("╚══════════════════════════════════════════════════════════════════════════════════╝\n")

class Caixa:
    def __init__(self):
        self._produtos = {
            'PASTEL': [],
            'BEBIDA': [],
            'AÇAI': [],
            'SORVETE': [],
            'CUZCUZ': {'BASES': ["CARNE","FRANGO","CALABRESA","SALCICHA","BACON","PRESUNTO"],
                       'ACOMPANHAMENTOS': ["AZEITONA","MILHO","ERVILHA","TOMATE","CEBOLA","OREGANO","PIMENTA CALABRESA"],
                       'QUEIJOS': ["MUSSARELA","COALHO","CATUPIRY"]},
            'MASSA': {'MOLHOS': ["BRANCO","ROSÊ"], 'BASES': ["CARNE","FRANGO","CALABRESA","SALCICHA","BACON","PRESUNTO"],
                      'ACOMPANHAMENTOS': ["AZEITONA","MILHO","ERVILHA","TOMATE","CEBOLA","OREGANO","PIMENTA CALABRESA"],
                      'QUEIJOS': ["MUSSARELA","COALHO","CATUPIRY","PARMESÃO"],},
            'PETISCO': []
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
        elif isinstance(produto, Cuzcuz):
            self._produtos['CUZCUZ'].append(produto)
        elif isinstance(produto, Massa):
            self._produtos['MASSA'].append(produto)
        elif isinstance(produto, Petisco):
            self._produtos['PETISCO'].append(produto)

    def editar_produto(self, nome_produto):
        try:
            for tipo, lista_produtos in self._produtos.items():
                for produto in lista_produtos:
                    if produto._nome == nome_produto:
                        produto.editar()
                        print(f"{tipo} EDITADO COM SUCESSO!")
                        return
            print("PRODUTO NÃO ENCONTRADO!")
        except Exception as e:
            print(f"Erro ao editar produto: {e}")

    def remover_produto(self, nome_produto):
        try:
            for tipo, lista_produtos in self._produtos.items():
                for produto in lista_produtos:
                    if produto._nome == nome_produto:
                        lista_produtos.remove(produto)
                        print(f"{tipo} REMOVIDO COM SUCESSO!")
                        return
            print("PRODUTO NÃO ENCONTRADO!")
        except Exception as e:
            print(f"Erro ao remover produto: {e}")

    def registrar_venda(self):
        try:
            nome_cliente = input("DIGITE O NOME DO CLIENTE: ").upper()
            pedido = Pedido(nome_cliente)

            while True:
                menu_venda()
                try:
                    op3 = int(input("DIGITE A OPÇÃO DESEJADA: "))
                except ValueError:
                    print("Opção inválida! Por favor, insira um número.")
                    continue

                if op3 == 0:
                    break
                elif op3 in [1, 2, 3, 4, 5, 6, 7]:
                    tipo_produto = {1: 'PASTEL', 2: 'BEBIDA', 3: 'AÇAI', 4: 'SORVETE', 5: 'CUZCUZ', 6: 'MASSA', 7:'PETISCO'}[op3]
                    cont = 1
                    print(f"{tipo_produto}")

                    if tipo_produto == "CUZCUZ":
                        desc = []

                        print("\nBASES")
                        for i in range(3):
                            print(f"0 - CANCELAR")
                            for base in self._produtos[tipo_produto]['BASES']:
                                print(f"{cont} - {base}")
                                cont += 1
                            try:
                                op4 = int(input(f"DIGITE O NÚMERO DO DESEJADO: ")) - 1
                            except ValueError:
                                print("Opção inválida! Por favor, insira um número.")
                                continue

                            if op4 == -1:
                                break
                            if 0 <= op4 < len(self._produtos[tipo_produto]['BASES']):
                                desc.append(self._produtos[tipo_produto]['BASES'][op4])
                            else:
                                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                            cont = 1

                        print("\nACOMPANHAMENTOS")
                        while True:
                            print(f"0 - CANCELAR")
                            for acomp in self._produtos[tipo_produto]['ACOMPANHAMENTOS']:
                                print(f"{cont} - {acomp}")
                                cont += 1
                            try:
                                op4 = int(input(f"DIGITE O NÚMERO DO DESEJADO: ")) - 1
                            except ValueError:
                                print("Opção inválida! Por favor, insira um número.")
                                continue

                            if op4 == -1:
                                break
                            if 0 <= op4 < len(self._produtos[tipo_produto]['ACOMPANHAMENTOS']):
                                desc.append(self._produtos[tipo_produto]['ACOMPANHAMENTOS'][op4])
                            else:
                                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                            cont = 1
                            if op4 == -1:
                                break

                        print("\nQUEIJOS")
                        for queijo in self._produtos[tipo_produto]['QUEIJOS']:
                            print(f"{cont} - {queijo}")
                            cont += 1
                        try:
                            op4 = int(input(f"DIGITE O NÚMERO DO DESEJADO: ")) - 1
                        except ValueError:
                            print("Opção inválida! Por favor, insira um número.")
                            continue

                        if 0 <= op4 < len(self._produtos[tipo_produto]['QUEIJOS']):
                            desc.append(self._produtos[tipo_produto]['QUEIJOS'][op4])

                        desc = " ".join(desc)
                        print(desc)
                        c = Cuzcuz(desc, 10)
                        try:
                            quantidade = int(input("DIGITE A QUANTIDADE DESEJADA: "))
                        except ValueError:
                            print("Quantidade inválida! Por favor, insira um número.")
                            continue

                        pedido.adicionar_produto(c, quantidade, tipo_produto)

                    elif tipo_produto == "MASSA":
                        desc = []

                        print("\nMOLHOS")
                        for molho in self._produtos[tipo_produto]['MOLHOS']:
                            print(f"{cont} - {molho}")
                            cont += 1
                        try:
                            op4 = int(input(f"DIGITE O NÚMERO DO DESEJADO: ")) - 1
                        except ValueError:
                            print("Opção inválida! Por favor, insira um número.")
                            continue

                        if 0 <= op4 < len(self._produtos[tipo_produto]['MOLHOS']):
                            desc.append(self._produtos[tipo_produto]['MOLHOS'][op4])

                        print("\nBASES")
                        for i in range(3):
                            print(f"0 - CANCELAR")
                            for base in self._produtos[tipo_produto]['BASES']:
                                print(f"{cont} - {base}")
                                cont += 1
                            try:
                                op4 = int(input(f"DIGITE O NÚMERO DO DESEJADO: ")) - 1
                            except ValueError:
                                print("Opção inválida! Por favor, insira um número.")
                                continue

                            if op4 == -1:
                                break
                            if 0 <= op4 < len(self._produtos[tipo_produto]['BASES']):
                                desc.append(self._produtos[tipo_produto]['BASES'][op4])
                            else:
                                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                            cont = 1

                        print("\nACOMPANHAMENTOS")
                        while True:
                            print(f"0 - CANCELAR")
                            for acomp in self._produtos[tipo_produto]['ACOMPANHAMENTOS']:
                                print(f"{cont} - {acomp}")
                                cont += 1
                            try:
                                op4 = int(input(f"DIGITE O NÚMERO DO DESEJADO: ")) - 1
                            except ValueError:
                                print("Opção inválida! Por favor, insira um número.")
                                continue

                            if op4 == -1:
                                break
                            if 0 <= op4 < len(self._produtos[tipo_produto]['ACOMPANHAMENTOS']):
                                desc.append(self._produtos[tipo_produto]['ACOMPANHAMENTOS'][op4])
                            else:
                                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                            cont = 1
                            if op4 == -1:
                                break

                        print("\nQUEIJOS")
                        for queijo in self._produtos[tipo_produto]['QUEIJOS']:
                            print(f"{cont} - {queijo}")
                            cont += 1
                        try:
                            op4 = int(input(f"DIGITE O NÚMERO DO DESEJADO: ")) - 1
                        except ValueError:
                            print("Opção inválida! Por favor, insira um número.")
                            continue

                        if 0 <= op4 < len(self._produtos[tipo_produto]['QUEIJOS']):
                            desc.append(self._produtos[tipo_produto]['QUEIJOS'][op4])

                        desc = " ".join(desc)
                        print(desc)
                        m = Massa(desc, 18)
                        try:
                            quantidade = int(input("DIGITE A QUANTIDADE DESEJADA: "))
                        except ValueError:
                            print("Quantidade inválida! Por favor, insira um número.")
                            continue

                        pedido.adicionar_produto(m, quantidade, tipo_produto)

                    else:
                        if not self._produtos[tipo_produto]:
                            print(f"SEM {tipo_produto} DISPONÍVEIS NO MOMENTO")
                            continue
                        for produto in self._produtos[tipo_produto]:
                            print(f"{cont} - {produto._nome} - {produto._preco} R$")
                            cont += 1
                        try:
                            op4 = int(input(f"DIGITE O NÚMERO DO {tipo_produto} DESEJADO: ")) - 1
                        except ValueError:
                            print("Opção inválida! Por favor, insira um número.")
                            continue

                        if 0 <= op4 < len(self._produtos[tipo_produto]):
                            try:
                                quantidade = int(input("DIGITE A QUANTIDADE DESEJADA: "))
                            except ValueError:
                                print("Quantidade inválida! Por favor, insira um número.")
                                continue

                            pedido.adicionar_produto(self._produtos[tipo_produto][op4], quantidade, tipo_produto)
                        else:
                            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
            pedido.imprimir_nota()
            confirmar = input("DESEJA REALIZAR A VENDA? (S/N): ").upper()
            if confirmar == 'S':
                self._pedidos.append(pedido)
                print("VENDA REALIZADA COM SUCESSO!")
            else:
                print("VENDA CANCELADA!")
        except Exception as e:
            print(f"Erro ao registrar venda: {e}")

    def historico_completo(self):
        try:
            for pedido in self._pedidos:
                pedido.imprimir_nota()
        except Exception as e:
            print(f"Erro ao imprimir histórico completo: {e}")

    def imprimir_cardapio(self):
        try:
            print("\n╔═══════════════════════════════════════╗")
            print("║               CARDÁPIO                ║")
            print("╚═══════════════════════════════════════╝")

            for tipo, lista_produtos in self._produtos.items():
                if tipo != "CUZCUZ" and tipo != "MASSA":
                    print(f"{tipo.upper()}")
                    print("╔═════════════════════════════════════════════════╗")
                    print("║              NOME            ║ PREÇO  ║ UNIDADE ║")
                    print("╠═════════════════════════════════════════════════╣")
                    for produto in lista_produtos:
                        print(f"║ {produto._nome:28} ║ {produto._preco:6.2f} ║ {produto._unidade:7} ║")
                    print("╚═════════════════════════════════════════════════╝\n")
        except Exception as e:
            print(f"Erro ao imprimir cardápio: {e}")

def main():
    try:
        caixa = Caixa()
        ac = Acai(59, "AÇAI")
        sv = Sorvete(45, "SORVETE")
        misto = Pastel("MISTO", 10)
        coca = Bebidas("COCA 350ML", 5)
        porcao = Petisco("PORÇÃO DE BATATA SIMPLES", 15)
        caixa.adicionar_produto(ac)
        caixa.adicionar_produto(sv)
        caixa.adicionar_produto(misto)
        caixa.adicionar_produto(coca)
        caixa.adicionar_produto(porcao)
        op = 11
        while op != 0:
            menu_principal()
            try:
                op = int(input("DIGITE A OPÇÃO DESEJADA: "))
            except ValueError:
                print("Opção inválida! Por favor, insira um número.")
                continue

            match op:
                case 1:
                    menu_cadastro()
                    try:
                        op2 = int(input("DIGITE A OPÇÃO DESEJADA: "))
                    except ValueError:
                        print("Opção inválida! Por favor, insira um número.")
                        continue

                    match op2:
                        case 1:
                            nome = input("DIGITE O NOME DO PASTEL: ").upper()
                            try:
                                preco = float(input("DIGITE O PREÇO DO PASTEL: "))
                            except ValueError:
                                print("Entrada inválida! Por favor, insira um valor numérico para o preço.")
                                continue

                            pastel = Pastel(nome, preco)
                            caixa.adicionar_produto(pastel)
                        case 2:
                            nome = input("DIGITE O NOME DA BEBIDA: ").upper()
                            try:
                                preco = float(input("DIGITE O PREÇO DA BEBIDA: "))
                            except ValueError:
                                print("Entrada inválida! Por favor, insira um valor numérico para o preço.")
                                continue

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
                    menu_historico()
                    try:
                        op5 = int(input("DIGITE A OPÇÃO DESEJADA: "))
                    except ValueError:
                        print("Opção inválida! Por favor, insira um número.")
                        continue

                    match op5:
                        case 1:
                            nome_cliente = input("DIGITE O NOME DO CLIENTE: ").upper()
                            for pedido in caixa._pedidos:
                                if pedido._cliente == nome_cliente:
                                    pedido.imprimir_nota()
                        case 2:
                            tot = 0
                            try:
                                data_inicial = datetime.strptime(input("DIGITE A DATA INICIAL (DD/MM/AAAA): "), "%d/%m/%Y").toordinal()
                                data_final = datetime.strptime(input("DIGITE A DATA FINAL (DD/MM/AAAA): "), "%d/%m/%Y").toordinal()
                            except ValueError:
                                print("Data inválida! Por favor, insira a data no formato DD/MM/AAAA.")
                                continue

                            for pedido in caixa._pedidos:
                                if data_inicial <= pedido._data <= data_final:
                                    pedido.imprimir_nota()
                                    tot += pedido.calcular_total()

                            print("╔════════════════════════════════════════════════════════════════╗")
                            print(f"║ TOTAL DE VENDAS NO PERÍODO: {tot:>31.2f} R$ ║")
                            print("╚════════════════════════════════════════════════════════════════╝\n")
                        case 3:
                            caixa.historico_completo()
                        case 4:
                            try:
                                id_pedido = int(input("DIGITE O ID DO PEDIDO: "))
                            except ValueError:
                                print("ID inválido! Por favor, insira um número.")
                                continue

                            for pedido in caixa._pedidos:
                                if pedido._id_pedido == id_pedido:
                                    pedido.imprimir_nota()
                case 6:
                    caixa.imprimir_cardapio()
                case 0:
                    print("SAINDO...")
                case _:
                    print("OPÇÃO INVÁLIDA")
                    continue
    except Exception as e:
        print(f"Erro ao executar o sistema: {e}")

if __name__ == "__main__":
    main()
