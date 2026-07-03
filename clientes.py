from uteis import *
def menu_clientes(clientes):
    resp3 = ''
    while resp3 !='0':
        limpar_terminal()
        titulo_reustarante()
        print("================================================")
        print(f"        👥 menu dos clientes ")
        print("================================================")
        print("  [1] Cadastrar novo cliente")
        print("  [2] procurar cliente")
        print("  [3] Alterar dados de um cliente")
        print("  [4] excluir cliente")
        print("  [0] sair")
        resp3 = input("Escolha sua opção: ")
        if resp3 == '1':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"        👥 cadastre um novo cliente! ")
            print("================================================")
            print()
            cliente_nome = input("👤 digite o nome do cliente: ")
            print()
            cliente_cpf = input("📇 digite o CPF do cliente: ")
            print()
            cliente_email = input("✉️ digite o E-mail do cliente: ")
            print()
            cliente_numero = input("📞 digite o número do cliente:  ")
            clientes[cliente_cpf] = [cliente_nome, cliente_email , cliente_numero ]
            print()
            print(f'clientes: {clientes}')  #verificar se entrou ou não no dicionario.
            print('cliente registrado com sucesso!')
            print()
            input("Tecle <ENTER> para continuar...")
        elif resp3 == '2':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"         🔍 procure um cliente!                  ")
            print("================================================")
            print()
            busca_cliente = input("📇 digite o CPF do cliente para busca-lo: ")
            if busca_cliente in clientes:
                print("👤 Nome do cliente:", clientes[busca_cliente][0])
                print("✉️ E-mail do cliente:", clientes[busca_cliente][1])
                print("📞 Número do cliente:", clientes[busca_cliente][2])
            else:
                print('cliente não encontrado')
            print()
            input("Tecle <ENTER> para continuar...")
        elif resp3 == '3':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"        👤altere os dados de um cliente!       ")
            print("================================================")
            print()
            alterar_cliente = input("📇 digite o CPF do cliente: ")
            if alterar_cliente in clientes:
                print("👤 Nome do cliente:", clientes[alterar_cliente][0])
                print("✉️ E-mail do cliente:", clientes[alterar_cliente][1])
                print("📞 Número do cliente:", clientes[alterar_cliente][2])
                print()
                print('digite as modificações que deseje fazer: ')
                alterar_nome2 = input('👤 digite o novo nome: ')
                novo_email = input('✉️ digite o novo E-mail: ')
                novo_numero = input('📞 digite o novo número: ')
                clientes[alterar_cliente] = [alterar_nome2, novo_email, novo_numero]
                print()
                print("cliente alterado no sistema com sucesso!")
                print()
                print(f'clientes: {clientes}')    # Apenas para conferir alteração
                print()
            else:
                print('cliente não encontrado!')
            input("Tecle <ENTER> para continuar...")
        elif resp3 == '4':
            limpar_terminal()
            titulo_reustarante
            print("================================================")
            print(f"      ❌ delete um cliente do sistema!         ")
            print("================================================")
            print()
            excluir_cliente = input("📇 digite o CPF do cliente:  ")
            if clientes[excluir_cliente][3] == True:
                print("👤 Nome do cliente    :", clientes[excluir_cliente][0])
                print("✉️ E-mail do cliente  :", clientes[excluir_cliente][1])
                print("📞 Número do cliente  :", clientes[excluir_cliente][2])
                print()
                confirmar = input('aperte "s" para confirmar a exclusão:  ')
                if confirmar.lower() == "s":
                    clientes[excluir_cliente][3] == False
                    print('cliente excluido!')
                    print()
                    print(f'clientes: {clientes}')
                else:
                    print('exclusão cancelada!')
            else:
                print('cliente não encontrado')
            print()
            input("Tecle <ENTER> para continuar...")
