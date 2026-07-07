def relatorio_clientes(clientes):
    print(f"{'2. CLIENTES CADASTRADOS':^75}")
    print("-" * 75)
    print(f"{'ID':<7} | {'Nome':<20} | {'E-mail':<25} | {'Status':<10}")
    print("-" * 75)
    for id_cliente, dados in clientes.items():
        nome = dados[0]
        email = dados[1]
        status = "Ativo" if dados[3] else "Inativo"
        print(f"{id_cliente:<7} | {nome:<20} | {email:<25} | {status:<10}")
    print()


def relatorio_cardapio(cardapio):
    print("-" * 75)
    print(f"{'1. ITENS DO CARDÁPIO':^75}")
    print("-" * 75)
    print(f"{'Código':<8} | {'Nome do Item':<25} | {'Preço':<12} | {'Disponibilidade':<15}")
    print("-" * 75)
    
    for codigo_item, dados in cardapio.items():
        nome_item = dados[0]
        preco = dados[1]
        disponivel = "Disponível" if dados[2] else "Indisponível"
        print(f"{codigo_item:<8} | {nome_item:<25} | R$ {preco:<9.2f} | {disponivel:<15}")
    print()

def relatorio_pedidos(pedidos,cardapio,clientes):
    print("-" * 75)
    print(f"{'3. HISTÓRICO DE PEDIDOS':^75}")
    print("-" * 75)
    print(f"{'Nº Ped':<7} | {'Item (Cód)':<18} | {'Cliente (ID)':<22} | {'Data':<12} | {'Status':<8}")
    print("-" * 75)
    for num_pedido, dados in pedidos.items():
        cod_item = dados[0]  
        id_cliente = dados[1]           
        data = dados[2]
        status_pedido = "Ativo" if dados[3] else "Cancelado"
        
        # Cruzando dados: Busca o nome do item no cardápio
        nome_item = cardapio[cod_item][0] 
        
        # Cruzando dados: Busca o nome do cliente no dicionário de clientes
        nome_cliente = clientes[id_cliente][0]
        
        # Formatando os textos para caberem perfeitamente na tabela
        item_formatado = f"{nome_item[:10]} ({cod_item})"
        cliente_formatado = f"{nome_cliente[:12]} ({id_cliente})"
        
        print(f"{num_pedido:<7} | {item_formatado:<18} | {cliente_formatado:<22} | {data:<12} | {status_pedido:<8}")

def relatorio_clientes_ativos(clientes):
    # 1. CLIENTES ATIVOS
    print("-" * 75)
    print(f"{'CLIENTES ATIVOS':^75}")
    print("-" * 75)
    print(f"{'ID':<7} | {'Nome':<20} | {'E-mail':<25}")
    print("-" * 75)
    for id_clie, dados in clientes.items():
        if dados[3]: # Se o cliente estiver Ativo (True)
            print(f"{id_clie:<7} | {dados[0]:<20} | {dados[1]:<25}")


def relatorio_cardapio_ativos(cardapio):
    print("-" * 75)
    print(f"{'ITENS DISPONÍVEIS NO CARDÁPIO':^75}")
    print("-" * 75)
    print(f"{'Código':<8} | {'Nome do Item':<25} | {'Preço':<12}")
    print("-" * 75)
    for cod_item, dados in cardapio.items():
        if dados[2]: # Se o item estiver Disponível (True)
            print(f"{cod_item:<8} | {dados[0]:<25} | R$ {dados[1]:<9.2f}")

def relatorio_pedidos_ativos(pedidos,cardapio,clientes):
    print("-" * 75)
    print(f"{'PEDIDOS EM ANDAMENTO / ATIVOS':^75}")
    print("-" * 75)
    print(f"{'Nº Ped':<7} | {'Item (Cód)':<18} | {'Cliente (ID)':<22} | {'Data':<12}")
    print("-" * 75)
    for num_ped, dados in pedidos.items():
        if dados[3]: # Se o pedido estiver Ativo (True)
            cod_item = dados[0].strip(',')
            id_clie = dados[1]
            data = dados[2]
            
            nome_item = cardapio[cod_item][0] 
            nome_clie = clientes[id_clie][0] 
            print(f"{num_ped:<7} | {nome_item[:10]} ({cod_item}) | {nome_clie[:12]} ({id_clie}) | {data:<12}")

def clientes_inativos(clientes):
    print("-" * 75)
    print(f"{'CLIENTES INATIVOS':^75}")
    print("-" * 75)
    print(f"{'ID':<7} | {'Nome':<20} | {'E-mail':<25}")
    print("-" * 75)
    for id_clie, dados in clientes.items():
        if not dados[3]: # Se NÃO estiver ativo (False)
            print(f"{id_clie:<7} | {dados[0]:<20} | {dados[1]:<25}")
    print()

def cardapio_inativos(cardapio):
    print("-" * 75)
    print(f"{'ITENS INDISPONÍVEIS NO CARDÁPIO':^75}")
    print("-" * 75)
    print(f"{'Código':<8} | {'Nome do Item':<25} | {'Preço':<12}")
    print("-" * 75)
    for cod_item, dados in cardapio.items():
        if not dados[2]: # Se NÃO estiver disponível (False)
            print(f"{cod_item:<8} | {dados[0]:<25} | R$ {dados[1]:<9.2f}")
    print()

def pedidos_inativos(pedidos,cardapio,clientes):
    print("-" * 75)
    print(f"{'PEDIDOS CANCELADOS':^75}")
    print("-" * 75)
    print(f"{'Nº Ped':<7} | {'Item (Cód)':<18} | {'Cliente (ID)':<22} | {'Data':<12}")
    print("-" * 75)
    for num_ped, dados in pedidos.items():
        if not dados[3]: # Se NÃO estiver ativo (False)
            cod_item = dados[0].strip(',')
            id_clie = dados[1]
            data = dados[2]
            
            nome_item = cardapio[cod_item][0] 
            nome_clie = clientes[id_clie][0] 
            
            print(f"{num_ped:<7} | {nome_item[:10]} ({cod_item}) | {nome_clie[:12]} ({id_clie}) | {data:<12}")


            


