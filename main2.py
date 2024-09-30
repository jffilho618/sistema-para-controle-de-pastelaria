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
        self.caixa.adicionar_produto(ac)
        self.caixa.adicionar_produto(sv)
        self.caixa.adicionar_produto(misto)
        self.caixa.adicionar_produto(coca)
        self.caixa.adicionar_produto(porcao)

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
        self.editar_window = QtWidgets.QDialog()
        uic.loadUi('ui\editar.ui', self.editar_window)

        # Exibir as imagens dos botões de inserir/editar/remover e da caixa de pesquisa
        self.exibir_imagem_inserir(self.editar_window)
        self.exibir_imagem_editar(self.editar_window)
        self.exibir_imagem_remover(self.editar_window)
        self.exibir_imagem_pesquisa(self.editar_window)

        # Definir ícone do botão de voltar na tela de edição
        self.definir_imagem_voltar(self.editar_window)

        self.editar_window.exec_()

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
