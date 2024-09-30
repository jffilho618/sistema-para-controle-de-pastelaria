import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore  # Adicionado QtCore
from TrabalhoFinal import *

# Carrega o arquivo .ui
class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui\PASTELARIA.ui', self)  # Substitua pelo nome correto do arquivo .ui
        
        self.caixa = Caixa()

        # Conectando botões da interface a funções
        self.pushButton_4.clicked.connect(self.abrir_relatorio)
        self.pushButton_5.clicked.connect(self.vender_produto)
        self.pushButton_6.clicked.connect(self.editar_produto)

        # Exibindo as imagens nos QLabels
        self.exibir_imagem_user()
        self.exibir_imagen_food()
        self.exibir_imagem_relatorio()

        # Adiciona os produtos ao caixa
        self.inicializar_produtos()

    def exibir_imagem_user(self):
        # Carrega a imagem e define no QLabel, mantendo a proporção
        pixmap = QtGui.QPixmap(r"PROJETOS1\user.png")
        self.ajustar_imagem(pixmap, self.label_6)

    def exibir_imagen_food(self):
        # Carrega a imagem e define no QLabel, mantendo a proporção
        pixmap = QtGui.QPixmap(r"PROJETOS1\fast-food.png")
        self.ajustar_imagem(pixmap, self.label_7)

    def exibir_imagem_relatorio(self):
        # Carrega a imagem e define no QLabel, mantendo a proporção
        pixmap = QtGui.QPixmap(r"PROJETOS1\report.png")
        self.ajustar_imagem(pixmap, self.label_5)

    def ajustar_imagem(self, pixmap, label):
        # Ajusta a imagem ao tamanho do QLabel, preservando a proporção
        if not pixmap.isNull():
            # Obtém o tamanho do QLabel
            label_width = label.width()
            label_height = label.height()
            # Redimensiona a imagem mantendo a proporção
            pixmap_resized = pixmap.scaled(label_width, label_height, QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)

    def inicializar_produtos(self):
        # Função para inicializar os produtos
        ac = Acai(59, "AÇAI")
        sv = Sorvete(45, "SORVETE")
        misto = Pastel("MISTO", 10.0)
        coca = Bebidas("COCA 350ML", 5)
        porcao = Petisco("BATATA", 15)
        # Adicione os outros produtos...
        self.caixa.adicionar_produto(ac)
        self.caixa.adicionar_produto(sv)
        self.caixa.adicionar_produto(misto)
        self.caixa.adicionar_produto(coca)
        self.caixa.adicionar_produto(porcao)

    def abrir_relatorio(self):
        # Função que será chamada quando o botão RELATÓRIO for clicado
        print("Abrindo relatório...")

    def vender_produto(self):
        # Função que será chamada quando o botão VENDER for clicado
        print("Vendendo produto...")

    def editar_produto(self):
        # Função que será chamada quando o botão EDITAR for clicado
        nome_produto = input("Digite o nome do produto que deseja editar: ").upper()
        self.caixa.editar_produto(nome_produto)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()  # Exibe a janela em tela cheia
    sys.exit(app.exec_())
