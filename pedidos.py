from uteis import *
def menu_pedidos(pedidos):
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
            titulo_reustarante
            print("================================================")
            print(f"        📝 cadastre um novo pedido! ")
            print("================================================")
            print()
            pedido_prato = input("🧾 digite o código do item: ")
            print()
            pedido_cliente = input("🕐 digite o ID do cliente:  ")
            print()
            pedido_data = input("🍟 digite a data: ")
            print()
            pedido_estado = input("🗃️ o pedido está disponivel?(S/N):  ")
            pedido_codigo = input('digite o código do pedido: ')
            pedidos[pedido_codigo] = [pedido_prato, pedido_cliente , pedido_data, pedido_estado ]
            print()
            print(f'pedidos: {pedidos}')  #verificar se entrou ou não no dicionario.
            print('pedidos registrado com sucesso!')
            print()
            input("Tecle <ENTER> para continuar...")
        elif resp4 == '2':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"         🔍 procure um pedido!                  ")
            print("================================================")
            print()
            busca_pedido = input("🗃️ digite o número de pedido para busca-lo: ")
            if busca_pedido in pedidos:
                print("🧾 Nome do item       :", pedidos[busca_pedido][0])
                print("🕐 hora do pedido  :", pedidos[busca_pedido][1])
                print("🍟 quantidade do pedido  :", pedidos[busca_pedido][2])
            else:
                print('pedido não encontrado')
            input("Tecle <ENTER> para continuar...")
        elif resp4 == '3':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"        📝altere um pedido!       ")
            print("================================================")
            print()
            alterar_pedido = input("🗃️ digite o número do pedido: ")
            if alterar_pedido in pedidos:
                print("🧾 Nome do item       :", pedidos[alterar_pedido][0])
                print("🕐 hora do pedido  :", pedidos[alterar_pedido][1])
                print("🍟 quantidade do pedido  :", pedidos[alterar_pedido][2])
                print()
                print('digite as modificações que deseje fazer: ')
                alterar_nome3 = input('🧾 digite o novo nome: ')
                nova_hora = input('🕐 digite a nova hora: ')
                nova_quantidade = input('🍟 digite a nova quantidade: ')
                pedidos[alterar_pedido] = [alterar_nome3, nova_hora, nova_quantidade]
                print()
                print("pedido alterado no sistema com sucesso!")
                print()
                print(f'pedidos: {pedidos}')    # Apenas para conferir alteração
                print()
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
            if pedidos[excluir_pedido][3] == True:
                print("🧾 Nome do item    :", pedidos[excluir_pedido][0])
                print("🕐 hora do pedido  :", pedidos[excluir_pedido][1])
                print("🍟 quantidade do pedido  :", pedidos[excluir_pedido][2])
                print()
                confirmar = input('aperte "s" para confirmar a exclusão:  ')
                if confirmar.lower() == "s":
                    pedidos[excluir_pedido][3] = False
                    print('pedido excluido!')
                    print()
                    print(f'pedidos: {pedidos}')
                else:
                    print('exclusão cancelada!')
            else:
                print('pedido não encontrado')
            input("Tecle <ENTER> para continuar...")
        print()