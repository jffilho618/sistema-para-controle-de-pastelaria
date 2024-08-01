from TrabalhoFinal import *

def main():
    try:
        caixa = Caixa()
        ac = Acai(59, "AÇAI")
        sv = Sorvete(45, "SORVETE")
        misto = Pastel("MISTO", 10.0032582739842)
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




        caixa.adicionar_produto(ac)
        caixa.adicionar_produto(sv)
        caixa.adicionar_produto(misto)
        caixa.adicionar_produto(coca)
        caixa.adicionar_produto(porcao)
        caixa.adicionar_produto(carne)
        caixa.adicionar_produto(frango)
        caixa.adicionar_produto(Queijo_presunto)
        caixa.adicionar_produto(Queijo_coalho_ou_mussarela)
        caixa.adicionar_produto(carne_queijo_milho)
        caixa.adicionar_produto(frango_catupiry_milho)
        caixa.adicionar_produto(queijo_presunto_bacon)
        caixa.adicionar_produto(frango_catupiry)
        caixa.adicionar_produto(frango_cremoso)
        caixa.adicionar_produto(pizza_frango)
        caixa.adicionar_produto(hot_dog)
        caixa.adicionar_produto(Mexicano_Carne)
        caixa.adicionar_produto(Mexicano_frango)
        caixa.adicionar_produto(Mexicabo_carne_geleia)
        caixa.adicionar_produto(franbacon)
        caixa.adicionar_produto(xtudao)
        caixa.adicionar_produto(Big_frango)
        caixa.adicionar_produto(Big_Vegetariano)
        caixa.adicionar_produto(doce_leite)
        caixa.adicionar_produto(prestigio)
        caixa.adicionar_produto(nutele)
        caixa.adicionar_produto(Romeu_Julieta)
        caixa.adicionar_produto(guarana)
        caixa.adicionar_produto(fanta)
        caixa.adicionar_produto(coca_2l)
        caixa.adicionar_produto(coca_zero)
        caixa.adicionar_produto(coca_cola_1l)
        caixa.adicionar_produto(guarana_2l)
        caixa.adicionar_produto(fanta_2l)
        op = 11
        while op != 0:
            menu_principal()
            try:
                op = int(input("DIGITE A OPÇÃO DESEJADA: "))
            except ValueError:
                print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                continue

            match op:
                case 1:
                    menu_cadastro()
                    try:
                        op2 = int(input("DIGITE A OPÇÃO DESEJADA: "))
                    except ValueError:
                        print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                        continue

                    match op2:

                        case 0:
                            continue
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
                        case 3:
                            try:
                                nome = input("DIGITE O NOME DO PETISCO: ").upper()
                                preco = float(input("DIGITE O PREÇO DO PETISCO: "))
                            except ValueError:
                                print("Entrada inválida! Por favor, insira um valor numérico para o preço.")
                                continue

                            petisco = Petisco(nome, preco)
                            caixa.adicionar_produto(petisco)

                        
                case 2:
                    nome_produto = input("DIGITE O NOME DO PRODUTO QUE DESEJA EDITAR: ").upper()
                    caixa.editar_produto(nome_produto)
                case 3:
                    nome_produto = input("DIGITE O NOME DO PRODUTO QUE DESEJA REMOVER: ").upper()
                    caixa.remover_produto(nome_produto)
                case 4:
                    caixa.registrar_venda()
                case 5:
                    cont =0
                    if not caixa._pedidos:
                        print("SEM VENDAS REGISTRADAS!")
                        continue
                    try:
                        id_pedido = int(input("DIGITE O ID DO PEDIDO: "))
                        for pedido in caixa._pedidos:
                            if pedido._id_pedido == id_pedido:
                                cont = 1
                                while True:
                                    op6 = 11
                                    menu_editar_pedido()
                                    try:
                                        op6 = int(input("DIGITE A OPÇÃO DESEJADA: "))
                                        match op6:
                                            case 0:
                                                break
                                            case 1:
                                                caixa.decrementar_pedido(pedido)
                                            case 2:
                                                caixa.alterar_quantidade(pedido)
                                            case 3:
                                                caixa.alterar_cliente(pedido)
                                            case 4:
                                                caixa.cancelar_pedido(pedido)
                                    except ValueError:
                                        print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                                        continue
                        if cont == 0:
                            print("ID NÃO ENCONTRADO.")
                            continue
                    except ValueError:
                        print("ID INVÁLIDO! TENTE NOVAMENTE.")
                        continue
                case 6:
                    menu_historico()
                    try:
                        op5 = int(input("DIGITE A OPÇÃO DESEJADA: "))
                    except ValueError:
                        print("OPÇÃO INVAlIDA! TENTE NOVAMENTE.")
                        continue

                    match op5:
                        case 1:
                            if not caixa._pedidos:
                                print("SEM VENDAS REGISTRADAS!")
                                continue
                            nome_cliente = input("DIGITE O NOME DO CLIENTE: ").upper()
                            for pedido in caixa._pedidos:
                                if pedido._cliente == nome_cliente:
                                    pedido.imprimir_nota()
                        case 2:
                            if not caixa._pedidos:
                                print("SEM VENDAS REGISTRADAS!")
                                continue
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
                            if not caixa._pedidos:
                                print("SEM VENDAS REGISTRADAS!")
                                continue
                            try:
                                id_pedido = int(input("DIGITE O ID DO PEDIDO: "))
                            except ValueError:
                                print("ID inválido! Por favor, insira um número.")
                                continue

                            for pedido in caixa._pedidos:
                                if pedido._id_pedido == id_pedido:
                                    pedido.imprimir_nota()
                case 7:
                    caixa.imprimir_cardapio()
                case 0:
                    print("SAINDO...")
                case _:
                    print("OPÇÃO INVÁLIDA")
                    continue
    except Exception as e:
        print(f"Erro ao executar o sistema: {e}")

def main2():
    autenticacao = AutenticacaoSimples()
    tentativas = 3

    while tentativas > 0:
        if autenticar_usuario(autenticacao):
            main()
            break
        else:
            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}")

    if tentativas == 0:
        print("Número máximo de tentativas alcançado. Encerrando o programa.")

if __name__ == "__main__":
    main2()