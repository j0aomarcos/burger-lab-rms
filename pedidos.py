from uteis import *
from validacao import *
def menu_pedidos(pedidos,cardapio, clientes):
    resp4 = ''
    while resp4 != '0':
        limpar_terminal()
        titulo_reustarante()
        print("================================================")
        print(f"        🍳 menu dos pedidos ")
        print("================================================")
        print("  [1] Cadastrar novo pedido")
        print("  [2] procurar pedido")
        print("  [3] Alterar dados de um pedido")
        print("  [4] excluir pedido")
        print("  [0] sair")
        resp4 = input("Escolha sua opção: ")
        if resp4 == '1':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"        📝 cadastre um novo pedido! ")
            print("================================================")
            print()
            pedido_prato = ''
            validade_prato_pedido = False
            while validade_prato_pedido is False:
                pedido_prato = input("🧾 digite o código do item: ")
                if pedido_prato in cardapio:
                    validade_prato_pedido = True
            print()
            pedido_cliente = ''
            validade_ID_pedido = False
            while validade_ID_pedido is False:
                pedido_cliente = input("🕐 digite o ID do cliente:  ")
                if pedido_cliente in clientes:
                    validade_ID_pedido = True

            validade_data = False
            while validade_data is False:
                pedido_data = input("🍟 digite a data: ")
                if validar_data(pedido_data):
                    validade_data = True


            print()
            pedido_codigo = input('digite o código do pedido: ')
            pedidos[pedido_codigo] = [pedido_prato, pedido_cliente , pedido_data, True ]
            print()
            nome_item = cardapio[pedido_prato][0] 
            nome_clie = clientes[pedido_cliente][0]
            print(f'nome do item: {nome_item}')
            print(f'nome do cliente: {nome_clie}')
            print(f'data: {pedido_data} ')
            print('estado: ativo')
            print
            print('pedidos registrado com sucesso!')
            print()
            input("Tecle <ENTER> para continuar...")
        elif resp4 == '2':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"         🔍 procure um pedido!                 ")
            print("================================================")
            print()
            busca_pedido = input("🗃️ digite o número de pedido para busca-lo: ")
            if busca_pedido in pedidos and pedidos[busca_pedido][3] == True:
                item_codigo_nome = pedidos[busca_pedido][0]
                cli_id_nome = pedidos[busca_pedido][1]
                nome_do_cliente = clientes[cli_id_nome][0]
                nome_do_prato = cardapio[item_codigo_nome][0]
                print(f'nome do prato: {nome_do_prato}')
                print(f'nome do cliente: {nome_do_cliente}')
                print(f'data: {pedidos[busca_pedido][2]}')
            else:
                'pedido não encontrado!'
                
            input("Tecle <ENTER> para continuar...")
        elif resp4 == '3':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"        📝altere um pedido!                    ")
            print("================================================")
            print()
            alterar_pedido = input("🗃️ digite o número do pedido: ")
            if alterar_pedido in pedidos:
                item_codigo_nome = pedidos[alterar_pedido][0]
                cli_id_nome = pedidos[alterar_pedido][1]
                nome_do_cliente = clientes[cli_id_nome][0]
                nome_do_prato = cardapio[item_codigo_nome][0]
                print(f'nome do prato: {nome_do_prato}')
                print(f'nome do cliente: {nome_do_cliente}')
                print(f'data: {pedidos[alterar_pedido][2]}')
                print('estado do pedido: ativo')
                print('selecione as novas modificações que deseja fazer: ')
                pedido_prato_alterar = ''
                validade_prato_pedido = False
                while validade_prato_pedido is False:
                    pedido_prato_alterar = input("🧾 digite o novo código do item: ")
                    if pedido_prato_alterar in cardapio:
                        validade_prato_pedido = True
            
                pedido_cliente_alterar = ''
                validade_ID_pedido = False
                while validade_ID_pedido is False:
                    pedido_cliente_alterar = input("🕐 digite o novo ID do cliente:  ")
                    if pedido_cliente_alterar in clientes:
                        validade_ID_pedido = True

        
                data_valida = False
                while data_valida is False:
                    pedido_data_alterar = input("🍟 digite a data: ")
                    if validar_data(pedido_data_alterar):
                        data_valida = True


                estado_pedido = input('digite o estado do pedido(ativo/inativo): ')
                if estado_pedido.lower() == 'ativo':
                    estado_pedido = True
                else:
                    estado_pedido = False 

                pedidos[alterar_pedido] = [pedido_prato_alterar, pedido_cliente_alterar , pedido_data_alterar, estado_pedido]

                item_codigo_nome = pedidos[alterar_pedido][0]

                cli_id_nome = pedidos[alterar_pedido][1]
                nome_do_cliente = clientes[cli_id_nome][0]
                nome_do_prato = cardapio[item_codigo_nome][0]
                print(f'nome do prato: {nome_do_prato}')
                print(f'nome do cliente: {nome_do_cliente}')
                print(f'data: {pedidos[alterar_pedido][2]}')
                if estado_pedido == True:
                    estado_atual = 'ativo'
                else:
                    estado_atual = 'inativo'
                print(f'estado do pedido: {estado_atual}')
            else:
                print('pedido não encontrado!')
            input("Tecle <ENTER> para continuar...")
        elif resp4 == '4':
            limpar_terminal()
            titulo_reustarante
            print("================================================")
            print(f"      ❌ delete um pedido do sistema!         ")
            print("================================================")
            print()
            excluir_pedido = input("📇 digite o número de pedido:  ")
            if excluir_pedido in pedidos:
                if pedidos[excluir_pedido][3] == True:
                    item_codigo_nome = pedidos[excluir_pedido][0]
                    cli_id_nome = pedidos[excluir_pedido][1]
                    nome_do_cliente = clientes[cli_id_nome][0]
                    nome_do_prato = cardapio[item_codigo_nome][0]
                    print(f'nome do prato: {nome_do_prato}')
                    print(f'nome do cliente: {nome_do_cliente}')
                    print(f'data: {pedidos[excluir_pedido][2]}')
                    print('estado do pedido: ativo')
                    confirmar = input('aperte "s" para confirmar a exclusão:  ')
                    if confirmar.lower() == "s":
                        pedidos[excluir_pedido][3] = False
                        print('pedido excluido!')
                        print()
                        item_codigo_nome = pedidos[excluir_pedido][0]
                        cli_id_nome = pedidos[excluir_pedido][1]
                        nome_do_cliente = clientes[cli_id_nome][0]
                        nome_do_prato = cardapio[item_codigo_nome][0]
                        print(f'nome do prato: {nome_do_prato}')
                        print(f'nome do cliente: {nome_do_cliente}')
                        print(f'data: {pedidos[excluir_pedido][2]}')
                        print('pedido desativado')
                    else:
                        print('exclusão cancelada!')
            else:
                print('pedido não achado, tente novamente')
            input("Tecle <ENTER> para continuar...")
        print()