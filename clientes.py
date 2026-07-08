from uteis import *
from validacao import *
from externo import *
def menu_clientes():
    clientes = recup_clientes()
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
            validade_fone = False
            while validade_fone is False:
                cliente_fone = input('digite seu número com DDD: ')
                if validar_fone(cliente_fone):
                    validade_fone = True
                if not validade_fone:
                    print('tente de novo, número invalido.')
            print()
            cliente_email = input("✉️ digite o username do seu e-mail(não precisa completar, o sistema completará): ")
            cliente_email = completar_email(cliente_email)
            print()
            validade_id = False
            while validade_id == False:
                cliente_ID = input("📞 digite o ID do cliente:  ")
                if validacao_ID(cliente_ID):
                    validade_id = True
                else:
                    print('tente de novo, ID invalido.')
            clientes[cliente_ID] = [cliente_nome, cliente_email , cliente_fone, True]
            print()
            print(f'nome: {clientes[cliente_ID][0]}')
            print(f'E-mail: {clientes[cliente_ID][1]}')
            print(f'telefone: {clientes[cliente_ID][2]}')
            print('estado do cliente: ativo')
            print('cliente registrado com sucesso!')
            print()
            salvar_clientes(clientes)
            input("Tecle <ENTER> para continuar...")
        elif resp3 == '2':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"         🔍 procure um cliente!                  ")
            print("================================================")
            print()
            busca_cliente = input("📇 digite o ID ou o nome do cliente para busca-lo: ")
            if busca_cliente in clientes:
                print("👤 Nome do cliente:", clientes[busca_cliente][0])
                print("✉️ E-mail do cliente:", clientes[busca_cliente][1])
                print("📞 Número do cliente:", clientes[busca_cliente][2])
                print('estado do cliente: ativo')
            else:
                nomes_clientes = []
                for infos in clientes.values():
                    clientes_mini = infos[0].lower()
                    nomes_clientes.append(clientes_mini)
                if busca_cliente.lower() in nomes_clientes:
                    for codigo, infos in clientes.items():
                        if infos[0].lower() == busca_cliente.lower():
                            if infos[3] == True:
                                print('nome do cliente:', infos[0])
                                print('E-email do cliente:', infos[1])
                                print('número do cliente', infos[2])
                                print('estado do cliente: ativo')
                else:
                    print('cliente não encontrado ou inativo.')
            print()
            input("Tecle <ENTER> para continuar...")
        elif resp3 == '3':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"        👤altere os dados de um cliente!       ")
            print("================================================")
            print()
            alterar_cliente = input("📇 digite o ID ou o nome do cliente: ")
            id_nome = None
            if alterar_cliente in clientes:
                id_nome = alterar_cliente
            else:
                nomes_clientes = []
                for infos in clientes.values():
                    clientes_mini = infos[0].lower()
                    nomes_clientes.append(clientes_mini)
                if alterar_cliente.lower() in nomes_clientes:
                    for codigo, infos in clientes.items():
                        if infos[0].lower() == alterar_cliente.lower():
                            id_nome = codigo
            if id_nome is not None:
                print('antigas informações: ')
                print('nome do cliente:', clientes[id_nome][0])
                print('E-email do cliente:', clientes[id_nome][1])
                print('número do cliente', clientes[id_nome][2])
                if clientes[id_nome][3] == True:
                    print('estado do cliente: ativo')
                else:
                    print('estado do cliente: inativo')
                print('digite as modificações que deseje fazer: ')
                alterar_cliente_nome = input('digite o novo nome: ')
                alterar_email = input('digite o E-mail novo(só o username): ')
                alterar_email = completar_email(alterar_email)
                novo_fone = ''
                validar_novo_fone = False
                while validar_novo_fone is False:
                    novo_fone = input('digite seu número com DDD: ')
                    if validar_fone(novo_fone):
                        validar_novo_fone = True
                    if not validade_fone:
                        print('tente de novo, número invalido.')
                alterar_disponibilidade = input("este cliente estará ativo ou inativo?: ")
                if alterar_disponibilidade.lower() == 'ativo':
                    alterar_disponibilidade = True
                else:
                    alterar_disponibilidade = False
                clientes[id_nome] = [alterar_cliente_nome,alterar_email,novo_fone,alterar_disponibilidade]
                print(f'nome: {clientes[id_nome][0]}  ')
                print(f'E-mail: {clientes[id_nome][1]}  ')
                print(f"telefone: {clientes[id_nome][2]}  ")
                if alterar_disponibilidade == True:
                     print(f"estado do cliente: disponivel ")
                else:
                     print(f"estado do cliente: indisponivel ")

                print('alterado com sucesso!')
                salvar_clientes(clientes)
            input("Tecle <ENTER> para continuar...")
        elif resp3 == '4':
            limpar_terminal()
            titulo_reustarante
            print("================================================")
            print(f"      ❌ delete um cliente do sistema!         ")
            print("================================================")
            print()
            excluir_cliente = input("📇 digite o ID do cliente:  ")
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
                    print(f'nome: {clientes[excluir_cliente][0]}')
                    print(f'E-mail: {clientes[excluir_cliente][1]}')
                    print(f'telfone: {clientes[excluir_cliente][2]}')
                    print(f'estado do cliente: {clientes[excluir_cliente][3]} ')
                else:
                    print('exclusão cancelada!')
            else:
                print('cliente não encontrado')
            print()
            salvar_clientes(clientes)
            input("Tecle <ENTER> para continuar...")
            salvar_clientes(clientes)

