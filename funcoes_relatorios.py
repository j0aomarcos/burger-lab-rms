from externo import *
def relatorio_clientes():
    clientes = recup_clientes()
    print("-" * 75)
    print(f"{'2. CLIENTES CADASTRADOS':^75}")
    print("-" * 75)
    for id_cliente, dados in clientes.items():
        nome = dados[0]
        email = dados[1]
        status = "Ativo" if dados[3] else "Inativo"
        print(f'nome: {nome}')
        print(f'e-mail: {email}')
        print(f'status: {status}')
        print()
    print()


def relatorio_cardapio():
    cardapio = recup_cardapio()
    print("-" * 75)
    print(f"{'1. ITENS DO CARDÁPIO':^75}")
    print("-" * 75)
    for codigo_item, dados in cardapio.items():
        nome_item = dados[0]
        preco_bruto = dados[1]
        disponivel = "Disponível" if dados[2] else "Indisponível"
        print(f'nome: {nome_item}')
        print(f'preço:{preco_bruto}')
        print(f'disponibilidade: {disponivel}')
    print()

def relatorio_pedidos():
    pedidos = recup_pedidos()
    clientes = recup_clientes()
    cardapio = recup_cardapio()
    print("-" * 75)
    print(f"{'3. HISTÓRICO DE PEDIDOS':^75}")
    print("-" * 75)
    for num_pedido, dados in pedidos.items():
        cod_item = dados[0]  
        id_cliente = dados[1]           
        data = dados[2]
        status_pedido = "Ativo" if dados[3] else "Cancelado"
        if cod_item in cardapio:
            nome_item = cardapio[cod_item][0] 
        if id_cliente in clientes:
            nome_cliente = clientes[id_cliente][0]
        print(f'nome do item: {nome_item}')
        print(f'nome do cliente: {nome_cliente}')
        print(f'data: {data}')
        print(f'status do pedido: {status_pedido}')

def relatorio_clientes_ativos():
    clientes = recup_clientes()
    print("-" * 75)
    print(f"{'CLIENTES ATIVOS':^75}")
    print("-" * 75)
    for id_clie, dados in clientes.items():
        if dados[3] ==True: 
            print(f'ID do cliente: {id_clie} | email: {dados[0]} | número: {dados[1]}')


def relatorio_cardapio_ativos():
    cardapio = recup_cardapio()
    print("-" * 75)
    print(f"{'ITENS DISPONÍVEIS NO CARDÁPIO':^75}")
    print("-" * 75)
    for cod_item, dados in cardapio.items():
        if dados[2] == True: 
            print(f"còdigo do item: {cod_item} | nome: {dados[0]} | valor: R$ {dados[1]}")

def relatorio_pedidos_ativos():
    pedidos = recup_pedidos()
    cardapio = recup_cardapio()
    clientes = recup_clientes()
    print("-" * 75)
    print(f"{'PEDIDOS EM ANDAMENTO / ATIVOS':^75}")
    print("-" * 75)
    for num_ped, dados in pedidos.items():
        if dados[3] == True: 
            cod_item = dados[0]
            id_clie = dados[1]
            data = dados[2]
            nome_item = cardapio[cod_item][0] 
            nome_clie = clientes[id_clie][0] 
            print(f"número do pedido {num_ped} | nome do item: {nome_item[:10]} | nome do cliente: {nome_clie[:12]} | data: {data}")


def clientes_inativos():
    clientes = recup_clientes()
    print("-" * 75)
    print(f"{'CLIENTES INATIVOS':^75}")
    print("-" * 75)
    for id_clie, dados in clientes.items():
        if not dados[3]: 
            print(f" iD: {id_clie:} | nome: {dados[0]} |e email: {dados[1]}")
    print()

def cardapio_inativos():
    cardapio = recup_cardapio()
    print("-" * 75)
    print(f"{'ITENS INDISPONÍVEIS NO CARDÁPIO':^75}")
    print("-" * 75)
    for cod_item, dados in cardapio.items():
        if not dados[2]: 
            print(f"código do item: {cod_item} | nome do item: {dados[0]} | preço do item R$ {dados[1]}")
    print()

def pedidos_inativos():
    cardapio = recup_cardapio()
    clientes = recup_clientes()
    pedidos = recup_pedidos()
    print("-" * 75)
    print(f"{'PEDIDOS CANCELADOS':^75}")
    print("-" * 75)
    for num_ped, dados in pedidos.items():
        if not dados[3]:
            cod_item = dados[0].strip(',')
            id_clie = dados[1]
            data = dados[2]
            
            nome_item = cardapio[cod_item][0] 
            nome_clie = clientes[id_clie][0] 
            
            print(f"número do pedido: :{num_ped} | nome do item {nome_item} ({cod_item}) | nome do cliente {nome_clie}  | data: {data:}")


