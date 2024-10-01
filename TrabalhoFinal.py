import abc
import random
from datetime import datetime, time


class Funcionario():
    def __init__(self, usuario, senha):
        self._usuario = usuario
        self._senha = senha
        
class Autenticacao(abc.ABC):
    @abc.abstractmethod
    def login(self, usuario, senha):
        pass

class AutenticacaoSimples:
    def __init__(self):
        self.usuario_padrao = "admin"
        self.senha_padrao = "admin"

    def login(self, funcionario: Funcionario):
        if funcionario._usuario == self.usuario_padrao and funcionario._senha == self.senha_padrao:
            return True
        else:
            return False

Autenticacao.register(AutenticacaoSimples)

def obter_credenciais():
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    return Funcionario(usuario, senha)

def autenticar_usuario(autenticacao: Autenticacao):
    funcionario = obter_credenciais()
    if autenticacao.login(funcionario):
        print("Login bem-sucedido!")
        return True
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
        return False
    
def autenticacao():
    autenticacao = AutenticacaoSimples()
    tentativas = 3

    while tentativas > 0:
        if autenticar_usuario(autenticacao):
            menu_historico()
            break
        else:
            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}")

        if tentativas == 0:
            print("Número máximo de tentativas alcançado!")
            continue

def menu_principal():
    print("╔══════════════════════════════════════╗")
    print("║               D'GUSTA                ║")
    print("╠══════════════════════════════════════╣")
    print("║ [1] CADASTRAR PRODUTO                ║")
    print("║ [2] EDITAR PRODUTO                   ║")
    print("║ [3] REMOVER PRODUTO                  ║")
    print("║ [4] REGISTRAR VENDA                  ║")
    print("║ [5] EDITAR PEDIDO                    ║")
    print("║ [6] HISTÓRICO DE VENDAS              ║")
    print("║ [7] IMPRIMIR CARDÁPIO                ║")
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
    print("║ [3] PETISCO                          ║")
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
    print("║ [8] FINALIZAR PEDIDO                 ║")
    print("║ [0] MENU ANTERIOR                    ║")
    print("╚══════════════════════════════════════╝\n")

def menu_editar_pedido():
    print("╔══════════════════════════════════════╗")
    print("║           EDIÇÃO DE PEDIDO           ║")
    print("╠══════════════════════════════════════╣")
    print("║ [1] REMOVER PRODUTO                  ║")
    print("║ [2] ALTERAR QUANTIDADE               ║")
    print("║ [3] ALTERAR CLIENTE                  ║")
    print("║ [4] CANCELAR PEDIDO                  ║")
    print("║ [0] MENU ANTERIOR                    ║")
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
    def __init__(self, cliente, id_pedido):
        self._cliente = cliente
        self._produtos = []
        self._id_pedido = id_pedido
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
            'CUZCUZ': {'BASES': ["CARNE","FRANGO","CALABRESA","SALCICHA","BACON","PRESUNTO","OVO"],
                       'ACOMPANHAMENTOS': ["AZEITONA","MILHO","ERVILHA","TOMATE","CEBOLA","OREGANO","PIMENTA CALABRESA"],
                       'QUEIJOS': ["MUSSARELA","COALHO","CATUPIRY"]},
            'MASSA': {'MOLHOS': ["BRANCO","ROSÊ"], 'BASES': ["CARNE","FRANGO","CALABRESA","SALCICHA","BACON","PRESUNTO"],
                      'ACOMPANHAMENTOS': ["AZEITONA","MILHO","ERVILHA","TOMATE","CEBOLA","OREGANO","PIMENTA CALABRESA"],
                      'QUEIJOS': ["MUSSARELA","COALHO","CATUPIRY","PARMESÃO"],},
            'PETISCO': []
        }
        self._pedidos = []

    def adicionar_produto(self, produto):
        if produto._preco <= 0:
            print("PREÇO INVÁLIDO! PRODUTO NÃO CADASTRADO!")
            return
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
            for tipo, conteudo in self._produtos.items():                
                if isinstance(conteudo, list):
                    for produto in conteudo:
                        if produto._nome == nome_produto:
                            print("╔═════════════════════════════════════════════════╗")
                            print("║              NOME            ║ PREÇO  ║ UNIDADE ║")
                            print("╠═════════════════════════════════════════════════╣")    
                            print(f"║ {produto._nome:28} ║ {produto._preco:6.2f} ║ {produto._unidade:7} ║")
                            print("╚═════════════════════════════════════════════════╝\n")
                            print("\n1 - EDITAR")
                            print("0 - CANCELAR")
                            try:
                                op = int(input("DIGITE A OPÇÃO DESEJADA: "))
                                if op == 0:
                                    return
                                elif op == 1:
                                    produto.editar()
                                    print(f"{tipo} EDITADO COM SUCESSO!")
                                    return
                                else:
                                    print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                                    continue
                            except ValueError:
                                print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                                continue
                            
           
            print("PRODUTO NÃO ENCONTRADO!")
        except Exception as e:
            print(f"Erro: {str(e)}")

    def remover_produto(self, nome_produto):
        try:
            for tipo, lista_produtos in self._produtos.items():
                for produto in lista_produtos:
                    if produto._nome == nome_produto:
                        if tipo == "AÇAI" or tipo == "SORVETE":
                            print("NÃO É POSSÍVEL REMOVER AÇAÍ OU SORVETE!")
                            return
                        print("╔═════════════════════════════════════════════════╗")
                        print("║              NOME            ║ PREÇO  ║ UNIDADE ║")
                        print("╠═════════════════════════════════════════════════╣")    
                        print(f"║ {produto._nome:28} ║ {produto._preco:6.2f} ║ {produto._unidade:7} ║")
                        print("╚═════════════════════════════════════════════════╝\n")
                        print("\n1 - REMOVER")
                        print("0 - CANCELAR")
                        try:
                            op = int(input("DIGITE A OPÇÃO DESEJADA: "))
                            if op == 0:
                                return
                            elif op == 1:
                                lista_produtos.remove(produto)
                                print(f"{tipo} REMOVIDO COM SUCESSO!")
                                return
                            else:
                                print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                                continue
                        except ValueError:
                            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                            continue
                        
            print("PRODUTO NÃO ENCONTRADO!")
        except Exception as e:
            print(f"PRODUTO NÃO ENCONTRADO!")
    
    def cancelar_pedido(self,pedido):
        try:
            
            pedido.imprimir_nota()
            confirmar = input("DESEJA CANCELAR O PEDIDO? (S/N): ").upper()
            if confirmar == 'S':
                self._pedidos.remove(pedido)
                print("PEDIDO CANCELADO COM SUCESSO!")
                return
            else:
                print("CANCELAMENTO DE PEDIDO CANCELADO!")
                return
        except ValueError:
            print("ID INVÁLIDO! TENTE NOVAMENTE.")

    def decrementar_pedido(self, pedido):
        pedido.imprimir_nota()
        try:
            prod = input("DIGITE O NOME DO PRODUTO QUE DESEJA REMOVER DO PEDIDO: ").upper()
            for produto, quantidade, tipo_produto in pedido._produtos:
                if produto._nome == prod:
                    pedido._produtos.remove((produto, quantidade, tipo_produto))
                    pedido.imprimir_nota()
                    print("PRODUTO REMOVIDO COM SUCESSO!")
                    if not pedido._produtos:
                        self._pedidos.remove(pedido)
                        print("PEDIDO CANCELADO!")
                    return
            else:
                print("PRODUTO NÃO ENCONTRADO!")
        except Exception as e:
            print("ERRO AO REMOVER PRODUTO DO PEDIDO!")
    
    def alterar_quantidade(self, pedido):
        try:
            pedido.imprimir_nota()
            prod = input("DIGITE O NOME DO PRODUTO QUE DESEJA ALTERAR A QUANTIDADE: ").upper()
            for produto, quantidade, tipo_produto in pedido._produtos:
                if produto._nome == prod:
                    nova_quantidade = int(input("DIGITE A NOVA QUANTIDADE: "))
                    if nova_quantidade <= 0:
                        print("QUANTIDADE INVÁLIDA! TENTE NOVAMENTE.")
                        continue
                    pedido._produtos.remove((produto, quantidade, tipo_produto))
                    pedido.adicionar_produto(produto, nova_quantidade, tipo_produto)
                    pedido.imprimir_nota()
                    print("QUANTIDADE ALTERADA COM SUCESSO!")
                    return
            else:
                print("PRODUTO NÃO ENCONTRADO!")
        except Exception as e:
            print("ERRO AO ALTERAR QUANTIDADE DO PRODUTO!")
    
    def alterar_cliente(self, pedido):
        try:
            pedido.imprimir_nota()
            novo_cliente = input("DIGITE O NOME DO NOVO CLIENTE: ").upper()
            pedido._cliente = novo_cliente
            pedido.imprimir_nota()
            print("CLIENTE ALTERADO COM SUCESSO!")
        except Exception as e:
            print("ERRO AO ALTERAR CLIENTE DO PEDIDO!")

    def registrar_venda(self):
        try:
            nome_cliente = input("DIGITE O NOME DO CLIENTE: ").upper()
            id_pedido = self.sorteia_id_não_repetido()
            pedido = Pedido(nome_cliente, id_pedido)
            

            while True:
                menu_venda()
                try:
                    op3 = int(input("DIGITE A OPÇÃO DESEJADA: "))
                except ValueError:
                    print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                    continue

                if op3 == 8 or op3 == 0:
                    break
                elif op3 in [1, 2, 3, 4, 5, 6, 7]:
                    tipo_produto = {1: 'PASTEL', 2: 'BEBIDA', 3: 'AÇAI', 4: 'SORVETE', 5: 'CUZCUZ', 6: 'MASSA', 7:'PETISCO'}[op3]
                    cont = 1
                    print(f"{tipo_produto}")

                    if tipo_produto == "CUZCUZ":
                        desc = []

                        aux = 0
                        print("\nBASES")
                        while True:
                            print(f"0 - CANCELAR")
                            for base in self._produtos[tipo_produto]['BASES']:
                                print(f"{cont} - {base}")
                                cont += 1
                            try:
                                op4 = int(input(f"DIGITE O NÚMERO DO DESEJADO: ")) - 1
                            except ValueError:
                                print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                                cont=1
                                continue

                            if op4 == -1:
                                break
                            if 0 <= op4 < len(self._produtos[tipo_produto]['BASES']):
                                desc.append(self._produtos[tipo_produto]['BASES'][op4])
                                aux += 1
                                cont = 1
                            else:
                                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                                cont = 1
                            
                            if aux == 3:
                                break
                        
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
                                print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                                cont=1
                                continue

                            if op4 == -1:
                                break
                            if 0 <= op4 < len(self._produtos[tipo_produto]['ACOMPANHAMENTOS']):
                                desc.append(self._produtos[tipo_produto]['ACOMPANHAMENTOS'][op4])
                                cont = 1
                            else:
                                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                                cont = 1
                            cont = 1
                            if op4 == -1:
                                break
                        cont = 1

                        aux = 0
                        while True:
                            print("\nQUEIJOS")
                            print(f"0 - CANCELAR")
                            for queijo in self._produtos[tipo_produto]['QUEIJOS']:
                                print(f"{cont} - {queijo}")
                                cont += 1
                            try:
                                op4 = int(input(f"DIGITE O NÚMERO DO DESEJADO: ")) - 1
                            except ValueError:
                                print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                                continue

                            if op4 == -1:
                                break

                            if 0 <= op4 < len(self._produtos[tipo_produto]['QUEIJOS']):
                                desc.append(self._produtos[tipo_produto]['QUEIJOS'][op4])
                                aux += 1
                                cont = 1
                            
                            else:
                                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                                cont = 1
                                
                            
                            if aux == 1:
                                break
                            

                        desc = " ".join(desc)
                        print(desc)
                        c = Cuzcuz(desc, 10)
                        quantidade = int(input("DIGITE A QUANTIDADE DESEJADA: "))
                        if quantidade <= 0:
                            print("QUANTIDADE INVÁLIDA. TENTE NOVAMENTE.")
                            continue

                        pedido.adicionar_produto(c, quantidade, tipo_produto)

                    elif tipo_produto == "MASSA":
                        desc = []
                        cont = 1
                        aux = 0
                        while True:
                            print("\nMOLHOS")
                            print(f"0 - CANCELAR")
                            for molho in self._produtos[tipo_produto]['MOLHOS']:
                                print(f"{cont} - {molho}")
                                cont += 1
                            try:
                                op4 = int(input(f"DIGITE O NÚMERO DO DESEJADO: ")) - 1
                            except ValueError:
                                print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                                cont=1
                                continue

                            if op4 == -1:
                                break

                            if 0 <= op4 < len(self._produtos[tipo_produto]['MOLHOS']):
                                desc.append(self._produtos[tipo_produto]['MOLHOS'][op4])
                                aux += 1
                                cont = 1
                            else:
                                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                            cont = 1
                            if aux == 1:
                                break

                        aux = 0
                        cont = 1
                        print("\nBASES")
                        while True:
                            print(f"0 - CANCELAR")
                            for base in self._produtos[tipo_produto]['BASES']:
                                print(f"{cont} - {base}")
                                cont += 1
                            try:
                                op4 = int(input(f"DIGITE O NÚMERO DO DESEJADO: ")) - 1
                            except ValueError:
                                print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                                cont=1
                                continue

                            if op4 == -1:
                                break
                            if 0 <= op4 < len(self._produtos[tipo_produto]['BASES']):
                                desc.append(self._produtos[tipo_produto]['BASES'][op4])
                                aux += 1
                                cont = 1
                            else:
                                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                            cont = 1
                            
                            if aux == 3:
                                break
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
                                print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                                cont=1
                                continue

                            if op4 == -1:
                                break
                            if 0 <= op4 < len(self._produtos[tipo_produto]['ACOMPANHAMENTOS']):
                                desc.append(self._produtos[tipo_produto]['ACOMPANHAMENTOS'][op4])
                                cont = 1
                            else:
                                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                                cont = 1
                            if op4 == -1:
                                break
                        cont = 1

                        aux = 0
                        while True:
                            print("\nQUEIJOS")
                            print(f"0 - CANCELAR")
                            for queijo in self._produtos[tipo_produto]['QUEIJOS']:
                                print(f"{cont} - {queijo}")
                                cont += 1
                            try:
                                op4 = int(input(f"DIGITE O NÚMERO DO DESEJADO: ")) - 1
                            except ValueError:
                                print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                                cont=1
                                continue

                            if op4 == -1:
                                break

                            if 0 <= op4 < len(self._produtos[tipo_produto]['QUEIJOS']):
                                desc.append(self._produtos[tipo_produto]['QUEIJOS'][op4])
                                aux += 1
                                cont = 1
                            
                            else:
                                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                                cont = 1
                            
                            if aux == 1:
                                break
                        desc = " ".join(desc)
                        print(desc)
                        m = Massa(desc, 18)
                        quantidade = int(input("DIGITE A QUANTIDADE DESEJADA: "))
                        if quantidade <= 0:
                            print("QUANTIDADE INVÁLIDA. TENTE NOVAMENTE.")
                            continue
                        pedido.adicionar_produto(m, quantidade, tipo_produto)

                    else:
                        if not self._produtos[tipo_produto]:
                            print(f"SEM {tipo_produto} DISPONÍVEIS NO MOMENTO")
                            continue
                        for produto in self._produtos[tipo_produto]:
                            print(f"{cont} - {produto._nome} - {produto._preco:.2f} R$")
                            cont += 1
                        try:
                            op4 = int(input(f"DIGITE O NÚMERO DO {tipo_produto} DESEJADO: ")) - 1
                        except ValueError:
                            print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                            continue

                        if 0 <= op4 < len(self._produtos[tipo_produto]):
                              
                            quantidade = int(input("DIGITE A QUANTIDADE DESEJADA: "))
                            if quantidade <= 0:
                                print("QUANTIDADE INVÁLIDA. TENTE NOVAMENTE.")
                                continue

                            pedido.adicionar_produto(self._produtos[tipo_produto][op4], quantidade, tipo_produto)
                        else:
                            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
                            continue
                else:
                    print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
                    continue       
                
            if op3 == 8 :
                if not pedido._produtos:
                    print("PEDIDO VAZIO! VENDA CANCELADA!")
                else:
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
            if not self._pedidos:
                print("SEM VENDAS REGISTRADAS!")
                return
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

    def sorteia_id_não_repetido(self):
        id = random.randint(1, 10000)
        while id in [pedido._id_pedido for pedido in self._pedidos]:
            id = random.randint(1, 10000)
        return id

# Função principal integrando autenticação

