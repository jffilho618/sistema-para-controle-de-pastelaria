import tkinter as tk
from tkinter import messagebox


class SistemaDeVendasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Vendas")
        self.root.geometry("500x400")
        
        # Criando os botões principais para as funções do sistema
        self.criar_tela_principal()

    def criar_tela_principal(self):
        # Título
        titulo = tk.Label(self.root, text="Sistema de Vendas", font=("Arial", 18, "bold"))
        titulo.pack(pady=10)

        # Botões principais
        btn_adicionar = tk.Button(self.root, text="Adicionar Produto", command=self.adicionar_produto, width=30)
        btn_adicionar.pack(pady=5)

        btn_editar = tk.Button(self.root, text="Editar Produto", command=self.editar_produto, width=30)
        btn_editar.pack(pady=5)

        btn_remover = tk.Button(self.root, text="Remover Produto", command=self.remover_produto, width=30)
        btn_remover.pack(pady=5)

        btn_vender = tk.Button(self.root, text="Registrar Venda", command=self.registrar_venda, width=30)
        btn_vender.pack(pady=5)

        btn_imprimir_cardapio = tk.Button(self.root, text="Imprimir Cardápio", command=self.imprimir_cardapio, width=30)
        btn_imprimir_cardapio.pack(pady=5)

        btn_historico = tk.Button(self.root, text="Histórico de Vendas", command=self.historico_vendas, width=30)
        btn_historico.pack(pady=5)

    def adicionar_produto(self):
        messagebox.showinfo("Adicionar Produto", "Funcionalidade de Adicionar Produto")

    def editar_produto(self):
        messagebox.showinfo("Editar Produto", "Funcionalidade de Editar Produto")

    def remover_produto(self):
        messagebox.showinfo("Remover Produto", "Funcionalidade de Remover Produto")

    def registrar_venda(self):
        messagebox.showinfo("Registrar Venda", "Funcionalidade de Registrar Venda")

    def imprimir_cardapio(self):
        messagebox.showinfo("Imprimir Cardápio", "Funcionalidade de Imprimir Cardápio")

    def historico_vendas(self):
        messagebox.showinfo("Histórico de Vendas", "Funcionalidade de Histórico de Vendas")


# Inicializando a interface Tkinter
root = tk.Tk()
app = SistemaDeVendasGUI(root)
root.mainloop()
