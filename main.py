import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QDialog, QDialogButtonBox, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon

class CadastroDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Cadastro")
        self.setGeometry(150, 150, 300, 200)

        # Layout principal
        layout = QVBoxLayout()

        # Título
        title_label = QLabel("Menu Cadastro", self)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Botões do menu
        btn_pastel = QPushButton("PASTEL", self)
        btn_bebida = QPushButton("BEBIDA", self)

        # Layout dos botões
        button_layout = QVBoxLayout()
        button_layout.addWidget(btn_pastel)
        button_layout.addWidget(btn_bebida)

        layout.addLayout(button_layout)

        # Botões OK e Cancel
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("D'GUSTA")
        self.setGeometry(100, 100, 300, 400)

        # Define o ícone da janela
        self.setWindowIcon(QIcon("icon.png"))  # Substitua "icon.png" pelo caminho do seu ícone

        # Cria os widgets
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("logo.png")  # Substitua "logo.png" pelo caminho da sua imagem
        self.image_label.setPixmap(pixmap)
        
        self.btn_cadastrar = QPushButton("CADASTRAR PRODUTO", self)
        self.btn_editar = QPushButton("EDITAR PRODUTO", self)
        self.btn_remover = QPushButton("REMOVER PRODUTO", self)
        self.btn_registrar = QPushButton("REGISTRAR VENDA", self)
        self.btn_historico = QPushButton("HISTÓRICO DE VENDAS", self)
        self.btn_sair = QPushButton("SAIR", self)

        # Conecta os botões a funções
        self.btn_cadastrar.clicked.connect(self.cadastrar_produto)
        self.btn_editar.clicked.connect(self.editar_produto)
        self.btn_remover.clicked.connect(self.remover_produto)
        self.btn_registrar.clicked.connect(self.registrar_venda)
        self.btn_historico.clicked.connect(self.historico_vendas)
        self.btn_sair.clicked.connect(self.sair)

        # Define o layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.btn_cadastrar)
        layout.addWidget(self.btn_editar)
        layout.addWidget(self.btn_remover)
        layout.addWidget(self.btn_registrar)
        layout.addWidget(self.btn_historico)
        layout.addWidget(self.btn_sair)

        # Define o widget central
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def cadastrar_produto(self):
        dialog = CadastroDialog()
        dialog.exec_()

    def editar_produto(self):
        print("Editar produto selecionado")

    def remover_produto(self):
        print("Remover produto selecionado")

    def registrar_venda(self):
        print("Registrar venda selecionado")

    def historico_vendas(self):
        print("Histórico de vendas selecionado")

    def sair(self):
        print("Sair selecionado")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
