import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from TrabalhoFinal import *

# Classe para a tela de login
class LoginWindow(QtWidgets.QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi('ui\login.ui', self)

        self.definir_imagem_voltar()
        self.exibir_imagem_user()

        self.pushButton.clicked.connect(self.fazer_login)
        self.pushButton_2.clicked.connect(self.voltar)

        self.autenticacao = AutenticacaoSimples()

    def definir_imagem_voltar(self):
        voltar_icon = QtGui.QIcon(r'PROJETOS1\21797173-seta-esquerda-icone-isolado-em-branco-fundo-vetor (1).jpg')  
        self.pushButton_2.setIcon(voltar_icon)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))

    def fazer_login(self):
        usuario = self.lineEdit.text()
        senha = self.lineEdit_2.text()

        funcionario = Funcionario(usuario, senha)

        if self.autenticacao.login(funcionario):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos!")

    def voltar(self):
        self.reject()

    def exibir_imagem_user(self):
        pixmap = QtGui.QPixmap(r"PROJETOS1\avatar_15484536.png")
        self.ajustar_imagem(pixmap, self.label)

    def ajustar_imagem(self, pixmap, label):
        if not pixmap.isNull():
            label_width = label.width()
            label_height = label.height()
            pixmap_resized = pixmap.scaled(label_width, label_height, QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)


# Classe principal da interface
class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui\PASTELARIA.ui', self)

        self.caixa = Caixa()

        self.pushButton_4.clicked.connect(self.abrir_relatorio)
        self.pushButton_5.clicked.connect(self.vender_produto)
        self.pushButton_6.clicked.connect(self.editar_produto)

        self.exibir_imagem_user()
        self.exibir_imagen_food()
        self.exibir_imagem_relatorio()

        self.inicializar_produtos()

    def exibir_imagem_user(self):
        pixmap = QtGui.QPixmap(r"PROJETOS1\user.png")
        self.ajustar_imagem(pixmap, self.label_6)

    def exibir_imagen_food(self):
        pixmap = QtGui.QPixmap(r"PROJETOS1\fast-food.png")
        self.ajustar_imagem(pixmap, self.label_7)

    def exibir_imagem_relatorio(self):
        pixmap = QtGui.QPixmap(r"PROJETOS1\report.png")
        self.ajustar_imagem(pixmap, self.label_5)

    def ajustar_imagem(self, pixmap, label):
        if not pixmap.isNull():
            label_width = label.width()
            label_height = label.height()
            pixmap_resized = pixmap.scaled(label_width, label_height, QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)

    def inicializar_produtos(self):
        ac = Acai(59, "AÇAI")
        sv = Sorvete(45, "SORVETE")
        misto = Pastel("MISTO", 10.0)
        coca = Bebidas("COCA 350ML", 5)
        porcao = Petisco("BATATA", 15)
        caixa = Caixa()
        ac = Acai(59, "AÇAI")
        sv = Sorvete(45, "SORVETE")
        misto = Pastel("MISTO", 10.0)
        coca = Bebidas("COCA 350ML", 5)
        porcao = Petisco("BATATA", 15)
        carne = Pastel("CARNE", 10)
        frango = Pastel("FRANGO", 10)
        Queijo_presunto = Pastel("QUEIJO E PRESUNTO", 10)
        Queijo_coalho_ou_mussarela = Pastel("QUEIJO COALHO OU MUSSARELA", 10)
        carne_queijo_milho = Pastel("CARNE, QUEIJO E MILHO", 10)
        frango_catupiry_milho = Pastel("FRANGO, CATUPIRY E MILHO", 10)
        queijo_presunto_bacon = Pastel("QUEIJO, PRESUNTO E BACON", 10)
        frango_catupiry = Pastel("FRANGO E CATUPIRY", 10)
        frango_cremoso = Pastel("FRANGO CREMOSO", 12)
        pizza_frango = Pastel("PIZZA DE FRANGO", 12)
        hot_dog = Pastel("HOT DOG", 12)
        Mexicano_Carne = Pastel("MEXICANO DE CARNE", 12)
        Mexicano_frango = Pastel("MEXICANO DE FRANGO", 12)
        Mexicabo_carne_geleia = Pastel("MEXICANO DE CARNE COM GELEIA", 12)
        franbacon = Pastel("FRANBACON", 12)
        xtudao = Pastel("XTUDÃO", 15)
        Big_frango = Pastel("BIG FRANGO", 15)
        Big_Vegetariano = Pastel("BIG VEGETARIANO", 15)
        doce_leite = Pastel("DOCE DE LEITE", 6)
        prestigio = Pastel("PRESTÍGIO", 6)
        nutele = Pastel("NUTELLA", 6)
        Romeu_Julieta = Pastel("ROMEU E JULIETA", 6)
        guarana = Bebidas("GUARANÁ 350ML", 5)
        fanta = Bebidas("FANTA 350ML", 5)
        coca_2l = Bebidas("COCA 2L", 12)
        coca_zero = Bebidas("COCA ZERO 350ML", 5)
        coca_cola_1l = Bebidas("COCA COLA 1L", 8)
        guarana_2l = Bebidas("GUARANÁ 2L", 12)
        fanta_2l = Bebidas("FANTA 2L", 12)
        self.caixa.adicionar_produto(ac)
        self.caixa.adicionar_produto(sv)
        self.caixa.adicionar_produto(misto)
        self.caixa.adicionar_produto(coca)
        self.caixa.adicionar_produto(porcao)
        self.caixa.adicionar_produto(carne)
        self.caixa.adicionar_produto(frango)
        self.caixa.adicionar_produto(Queijo_presunto)
        self.caixa.adicionar_produto(Queijo_coalho_ou_mussarela)
        self.caixa.adicionar_produto(carne_queijo_milho)
        self.caixa.adicionar_produto(frango_catupiry_milho)
        self.caixa.adicionar_produto(queijo_presunto_bacon)
        self.caixa.adicionar_produto(frango_catupiry)
        self.caixa.adicionar_produto(frango_cremoso)
        self.caixa.adicionar_produto(pizza_frango)
        self.caixa.adicionar_produto(hot_dog)
        self.caixa.adicionar_produto(Mexicano_Carne)
        self.caixa.adicionar_produto(Mexicano_frango)
        self.caixa.adicionar_produto(Mexicabo_carne_geleia)
        self.caixa.adicionar_produto(franbacon)
        self.caixa.adicionar_produto(xtudao)
        self.caixa.adicionar_produto(Big_frango)
        self.caixa.adicionar_produto(Big_Vegetariano)
        self.caixa.adicionar_produto(doce_leite)
        self.caixa.adicionar_produto(prestigio)
        self.caixa.adicionar_produto(nutele)
        self.caixa.adicionar_produto(Romeu_Julieta)
        self.caixa.adicionar_produto(guarana)
        self.caixa.adicionar_produto(fanta)
        self.caixa.adicionar_produto(coca_2l)
        self.caixa.adicionar_produto(coca_zero)
        self.caixa.adicionar_produto(coca_cola_1l)
        self.caixa.adicionar_produto(guarana_2l)
        self.caixa.adicionar_produto(fanta_2l)


    def abrir_relatorio(self):
        self.abrir_login()

    def vender_produto(self):
        print("Vendendo produto...")

    def editar_produto(self):
        if self.abrir_login():
            self.abrir_tela_editar()


    def abrir_login(self):
        self.login_window = LoginWindow()
        if self.login_window.exec_() == QtWidgets.QDialog.Accepted:
            return True
        return False

    def abrir_tela_editar(self):
        # Função para abrir a janela de edição
        self.editar_window = QtWidgets.QDialog()  # Cria uma instância da janela de edição
        uic.loadUi('ui\\editar.ui', self.editar_window)  # Carrega a interface da janela de edição

        # Conectar o campo de pesquisa à função de buscar e exibir os resultados
        self.editar_window.lineEdit.textChanged.connect(self.buscar_produto)

        # Conectar o evento de mudança de célula à função de atualização do produto
        self.editar_window.tableWidget.itemChanged.connect(self.atualizar_produto)

        # Exibir as imagens dos botões de inserir, editar, remover e da caixa de pesquisa
        self.exibir_imagem_inserir(self.editar_window)
        self.exibir_imagem_editar(self.editar_window)
        self.exibir_imagem_remover(self.editar_window)
        self.exibir_imagem_pesquisa(self.editar_window)

        # Definir o ícone do botão de voltar na tela de edição
        self.definir_imagem_voltar(self.editar_window)

        # Exibe a janela de edição
        self.editar_window.exec_()

    def buscar_produto(self):
        # Captura o texto inserido no campo de pesquisa
        texto_pesquisa = self.editar_window.lineEdit.text().lower()

        # Limpa o conteúdo atual da tabela
        self.editar_window.tableWidget.clearContents()
        
        # Remove todas as linhas atuais
        self.editar_window.tableWidget.setRowCount(0)

        # Variável para controlar o número de linhas a serem exibidas
        linha = 0

        # Percorre todos os produtos no caixa
        for tipo, conteudo in self.caixa._produtos.items():
            if isinstance(conteudo, list):  # Considera apenas categorias com listas de produtos
                for produto in conteudo:
                    if produto._nome.lower().startswith(texto_pesquisa):
                        # Insere uma nova linha na tabela
                        self.editar_window.tableWidget.insertRow(linha)

                        # Preenche as células com os dados do produto
                        self.editar_window.tableWidget.setItem(linha, 0, QtWidgets.QTableWidgetItem(produto._nome))
                        self.editar_window.tableWidget.setItem(linha, 1, QtWidgets.QTableWidgetItem(produto._unidade))
                        self.editar_window.tableWidget.setItem(linha, 2, QtWidgets.QTableWidgetItem(f"{produto._preco:.2f}"))

                        linha += 1

        # Ajusta o tamanho das colunas
        self.editar_window.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        # Define as proporções das colunas
        self.editar_window.tableWidget.setColumnWidth(0, 200)  # Nome com largura maior
        self.editar_window.tableWidget.setColumnWidth(1, 100)  # Unidade
        self.editar_window.tableWidget.setColumnWidth(2, 100)  # Preço

        # Define que as colunas restantes devem se esticar
        self.editar_window.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.editar_window.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        self.editar_window.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)

        # Ajusta a largura da coluna de nome
        self.editar_window.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)    


    def atualizar_produto(self, item):
        # Desconectar temporariamente o sinal de 'itemChanged' para evitar loops recursivos
        self.editar_window.tableWidget.blockSignals(True)

        row = item.row()
        col = item.column()

        # Encontrar o produto correspondente
        produto_encontrado = None
        tipo_produto = None

        # Percorre as categorias para encontrar o produto
        for tipo, conteudo in self.caixa._produtos.items():
            if isinstance(conteudo, list):  # Verifica se o conteúdo é uma lista
                if row < len(conteudo):  # Verifica se a linha está dentro do range da lista
                    produto_encontrado = conteudo[row]
                    tipo_produto = tipo
                    break

        # Verifica se o produto foi encontrado
        if produto_encontrado:
            if col == 0:  # Nome
                produto_encontrado._nome = item.text()
            elif col == 1:  # Unidade
                produto_encontrado._unidade = item.text()
            elif col == 2:  # Preço
                try:
                    produto_encontrado._preco = float(item.text())
                except ValueError:
                    # Lida com o erro de conversão, se o texto não for um número
                    QtWidgets.QMessageBox.warning(self.editar_window, "Erro", "Por favor, insira um preço válido.")

        # Reativar o sinal de 'itemChanged' após a atualização
        self.editar_window.tableWidget.blockSignals(False)

        # Recarrega a tabela para mostrar as atualizações, se necessário
        # self.buscar_produto()  # Isso pode ser removido se o loop recursivo não for desejado



    def definir_imagem_voltar(self, window):
        voltar_icon = QtGui.QIcon(r'PROJETOS1\21797173-seta-esquerda-icone-isolado-em-branco-fundo-vetor (1).jpg')  
        window.pushButton_2.setIcon(voltar_icon)
        window.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        window.pushButton_2.clicked.connect(window.reject)

    def exibir_imagem_inserir(self, window):
        pixmap = QtGui.QPixmap(r"PROJETOS1\check_15526414.png")  # Substitua pelo caminho correto da imagem de inserir
        self.ajustar_imagem(pixmap, window.label_7)  # Ajuste o nome do botão

    def exibir_imagem_editar(self, window):
        pixmap = QtGui.QPixmap(r"PROJETOS1\square_14034491.png")  # Substitua pelo caminho correto da imagem de editar
        self.ajustar_imagem(pixmap, window.label_6)  # Ajuste o nome do botão

    def exibir_imagem_remover(self, window):
        pixmap = QtGui.QPixmap(r"PROJETOS1\square_14034319.png")  # Substitua pelo caminho correto da imagem de remover
        self.ajustar_imagem(pixmap, window.label_8)  # Ajuste o nome do botão

    def exibir_imagem_pesquisa(self, window):
        pixmap = QtGui.QPixmap(r"PROJETOS1\search.png")  # Substitua pelo caminho correto da imagem da pesquisa
        self.ajustar_imagem(pixmap, window.label_10)  # Ajuste o nome do campo da pesquisa

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())
