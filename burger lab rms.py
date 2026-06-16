#burguer-lab-rms-v2
#Nota de Atualizações: manipulação e criação de arquivos externos.
import pickle
cardapio = {}
try:
    arquivo_cardapio = open('cardapio.dat','rb')
    cardapio = pickle.load(arquivo_cardapio)
    arquivo_cardapio.close()
except:
    cardapio = {
        #Codigo: nome, preço, disponibilidade
        '1111':['Hamburguer',15,'dísponivel'],
        '2222':['pizza',30,'dísponivel'],
        '3333':['filé a parmegiano',45,'disponivel'],
        '4444':['Camarão empanado',60,'disponivel']
    }
    arquivo_cardapio = open('cardapio.dat','wb')
    pickle.dump(cardapio, arquivo_cardapio)
    arquivo_cardapio.close()
clientes = {}
try:
    arquivo_clientes = open('clientes.dat','rb')
    clientes = pickle.load(arquivo_clientes)
    arquivo_clientes.close()
except:
    clientes = {
    #ID: nome, email, número
    '11111':['João Marcos','joaozinhos@gmai.com','4002-8922'],
    '22222':['Matheus vinolla','matheuszinho@gmail.com','6767-6767'],
    '33333':['Ruan Pablo','ruanzinho@gmail.com','4242-4242'],
    '44444':['Flavius da Luz','flaviuszinho@gmail.com','1234-5678']
    }
    arquivo_clientes = open('clientes.dat','wb')
    pickle.dump(clientes, arquivo_clientes)
    arquivo_clientes.close()

pedidos = {}
try:
    arquivo_pedidos = open('pedidos.dat','rb')
    clientes = pickle.load(arquivo_pedidos)
    arquivo_pedidos.close()
except:
    pedidos = {
    #número do pedido: codigo do item, hora do pedido, quantidade
    '0001': ['1111', '19:20', '1'],
    '0002': ['2222','20:30','2'],
    '0003': ['3333','21:40','3'],
    '0004': ['4444,','22:50','4']
    }
    arquivo_pedidos = open('pedidos.dat','wb')
    pickle.dump(pedidos,arquivo_pedidos)
    arquivo_pedidos.close()


resp = ''
def limpar_terminal():
    #comando que utilizo para limpar o terminal invés do import os.
    print("\033[H\033[J", end="")
def titulo_reustarante():
    #Função para não precisar colocando o título toda hora,geraria linhas demais.
    print('''
████╗   ██╗  ██╗██████╗  ██████╗ ███████╗██████╗     ██╗      █████╗ ██████╗ 
██╔═██╗ ██║  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗    ██║     ██╔══██╗██╔══██╗
██████╔╝██║  ██║██████╔╝██║  ███╗█████╗  ██████╔╝    ██║     ███████║██████╔╝
██╔══██╗██║  ██║██╔══██╗██║   ██║██╔══╝  ██╔══██╗    ██║     ██╔══██║██╔══██╗
██████╔╝╚█████╔╝██║  ██║╚██████╔╝███████╗██║  ██║    ███████╗██║  ██║██████╔╝
╚═════╝  ╚════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═════╝
        ''')

while resp != '0':
    #menu principal
    limpar_terminal()
    titulo_reustarante()
    print("================================================")
    print(f" Bem-vindo ao sistema de gestão do restaurante ")
    print("================================================")
    print(" [1] 📜  gerenciar cardápio")
    print(" [2] 👥  gerenciar lista de clientes ")
    print(" [3] 🍳  gerenciar pedidos")
    print(" [4] 📦  relatório")
    print(" [5] ⚙️  sobre o sistemas")
    print(" [0] ❌  sair do sistema")
    resp = input("escolha uma das opções: ")
    if resp == '1':
        resp2 = ''
        while resp2 != '0':
            #menu do modulo 1
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"        📜 menu do cardapio ")
            print("================================================")
            print()
            print("  [1] Cadastrar novo Prato")
            print("  [2] procurar prato")
            print("  [3] alterar prato")
            print("  [4] excluir prato")
            print("  [0] sair")
            resp2 = input("escolha uma das opções: ")
            if resp2 == '1':
                limpar_terminal()
                titulo_reustarante()
                print("================================================")
                print(f"        🍽️ cadastre um novo prato! ")
                print("================================================")
                print()
                nome_prato = input("🍽️ digite o nome do prato: ")
                print()
                codigo_prato = input("🔢 digite o código do prato: ")
                print()
                preco_prato = input("💵 digite o preço do prato: ")
                print()
                disponibilidade_prato = input("✅ digite se o prato está disponivel ou não: ")
                cardapio[codigo_prato] = [nome_prato, preco_prato, disponibilidade_prato ]
                print()
                print(f'pratos: {cardapio}')  #verificar se entrou ou não no dicionario.
                print('prato registrado com sucesso!')
                print()
                input("Tecle <ENTER> para continuar...")
            if resp2 == '2':
                limpar_terminal()
                titulo_reustarante()
                print("================================================")
                print(f"         🔍 procure um prato!                  ")
                print("================================================")
                print()
                busca_prato = input("digite o codigo do prato para busca-lo: ")
                if busca_prato in cardapio:
                    print("🍽️ Nome do prato     :", cardapio[busca_prato][0])
                    print("💵 Preço do prato    :", cardapio[busca_prato][1])
                    print("✅ Disponibilidade  :", cardapio[busca_prato][2])
                else:
                    print('prato não encontrado')
                print()
                input("Tecle <ENTER> para continuar...")
            if resp2 == '3':
                limpar_terminal()
                titulo_reustarante()
                print("================================================")
                print(f"        🍽️ altere um prato! ")
                print("================================================")
                print()
                alterar_prato = input("🔢 digite o código do prato: ")
                if alterar_prato in cardapio:
                    print("🍽️ Nome do prato     :", cardapio[alterar_prato][0])
                    print("💵 Preço do prato    :", cardapio[alterar_prato][1])
                    print("✅ Disponibilidade  :", cardapio[alterar_prato][2])
                    print()
                    print('digite as modificações que deseje fazer: ')
                    alterar_nome1 = input('digite o novo nome: ')
                    alterar_preco = input('digite o novo preço: ')
                    alterar_disponibilidade = input('digite a nova disponibilidade do prato: ')
                    cardapio[alterar_prato] = [alterar_nome1, alterar_preco, alterar_disponibilidade]
                    print()
                    print("prato alterado no cardapio com sucesso!")
                    print()
                    print(f'cardapio: {cardapio}')    # Apenas para conferir alteração
                    print()
                else:
                    print('prato não encontrado!')
                print()
                input("Tecle <ENTER> para continuar...")
            if resp2 == '4':
                limpar_terminal()
                titulo_reustarante()
                print("================================================")
                print(f"         ❌ exclua um prato!                   ")
                print("================================================")
                print()
                excluir_prato = input("🔢 digite o código do prato: ")
                if excluir_prato in cardapio:
                    print("🍽️ Nome do prato:", cardapio[excluir_prato][0])
                    print("💵 Preço do prato:", cardapio[excluir_prato][1])
                    print("✅ Disponibilidade:", cardapio[excluir_prato][2])
                    print()
                    confirmar = input('aperte "s" para confirmar a exclusão:  ')
                    if confirmar.lower() == "s":
                        del cardapio[excluir_prato]
                        print('prato excluido!')
                        print()
                        print(f'cardapio {cardapio}')
                    else:
                        print('exclusão cancelada!')
                        input("Tecle <ENTER> para continuar...")
                else:
                    print('prato não encontrado')
                print()
                input("Tecle <ENTER> para continuar...")
    elif resp == '2':
        resp3 = ''
        #menu modulo 2
        while resp3 != '0':
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
                titulo_reustarante()
                print("================================================")
                print(f"      ❌ delete um cliente do sistema!         ")
                print("================================================")
                print()
                excluir_cliente = input("📇 digite o CPF do cliente:  ")
                if excluir_cliente in clientes:
                    print("👤 Nome do cliente    :", clientes[excluir_cliente][0])
                    print("✉️ E-mail do cliente  :", clientes[excluir_cliente][1])
                    print("📞 Número do cliente  :", clientes[excluir_cliente][2])
                    print()
                    confirmar = input('aperte "s" para confirmar a exclusão:  ')
                    if confirmar.lower() == "s":
                        del clientes[excluir_cliente]
                        print('cliente excluido!')
                        print()
                        print(f'clientes: {clientes}')
                    else:
                        print('exclusão cancelada!')
                else:
                    print('cliente não encontrado')
                print()
                input("Tecle <ENTER> para continuar...")
    elif resp == '3':
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
                pedido_nome = input("🧾 digite o nome do item: ")
                print()
                pedido_hora = input("🕐 digite a hora do pedido: ")
                print()
                pedido_quantidade = input("🍟 digite a quantidade: ")
                print()
                pedido_numero = input("🗃️ digite o número de pedido:  ")
                pedidos[pedido_numero] = [pedido_nome, pedido_hora , pedido_quantidade ]
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
                titulo_reustarante()
                print("================================================")
                print(f"      ❌ delete um pedido do sistema!         ")
                print("================================================")
                print()
                excluir_pedido = input("📇 digite o número de pedido:  ")
                if excluir_pedido in pedidos:
                    print("🧾 Nome do item    :", pedidos[excluir_pedido][0])
                    print("🕐 hora do pedido  :", pedidos[excluir_pedido][1])
                    print("🍟 quantidade do pedido  :", pedidos[excluir_pedido][2])
                    print()
                    confirmar = input('aperte "s" para confirmar a exclusão:  ')
                    if confirmar.lower() == "s":
                        del pedidos[excluir_pedido]
                        print('pedido excluido!')
                        print()
                        print(f'pedidos: {pedidos}')
                    else:
                        print('exclusão cancelada!')
                else:
                    print('pedido não encontrado')
                input("Tecle <ENTER> para continuar...")
            print()
    elif resp == '4':
        limpar_terminal()
        titulo_reustarante()
        print("================================================")
        print(f"         menu dos relatorios ")
        print("================================================")
        print("  [1] lista do cardapio completa")
        print("  [2] lista de clientes completa")
        print("  [3] lista de pedidos completa")
        print("  [4] lista de lucros completa")
        print("  [5] sair")
        resp2 = input("Escolha sua opção: ")
        print()
        print("############################################")
        print("#####                                   ####")
        print("#####      Este módulo ainda está       ####")
        print("#####        em desenvolvimento         ####")
        print("#####                                   ####")
        print("############################################")
        print()
        input("Tecle <ENTER> para continuar...")
    elif resp == '5':
        limpar_terminal()
        titulo_reustarante()
        print("================================================")
        print(f"      ⚙️ Você está no Módulo Informações ")
        print("================================================")
        print("================================================================================================")
        print("  Projeto de Gestão de um restaurante para a máteria de Algoritmos e Lógica de Programação")
        print("=============lecionada pelo professor Flavius Gorgonio da Luz===================================")
        print("===================(desenvolvido por: João Marcos Santos Soares)================================")
        print("================================================================================================")
        print("===================  Licença Pública Geral GNU   ===============================================")
        print("===================  www.gnu.org/licenses/gpl.html =============================================")
        print()
        input("Tecle <ENTER> para continuar...")
    elif resp == '0':
        print('''
 █████╗ ██████╗ ███████╗██╗   ██╗███████╗
██╔══██╗██╔══██╗██╔════╝██║   ██║██╔════╝
███████║██║  ██║█████╗  ██║   ██║███████╗
██╔══██║██║  ██║██╔══╝  ██║   ██║╚════██║
██║  ██║██████╔╝███████╗╚██████╔╝███████║
╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝           
              
              ''')
        print()
        print("############################################")
        print("#####  Você encerrou o programa, até logo! #")
        print("############################################")
        print()
        input("Tecle <ENTER> para continuar...")
    else:
        limpar_terminal()
        print()
        print("############################################")
        print("#####   Você digitou uma opção inválida ####")
        print("############################################")
        print("#####                                   ####")
        print("#####      Retorne ao menu anterior     ####")
        print("#####         e tente novamente         ####")
        print("#####                                   ####")
        print("############################################")
        print()
        input("Tecle <ENTER> para continuar...")

arquivo_cardapio = open('cardapio.dat','wb')
pickle.dump(cardapio, arquivo_cardapio)
arquivo_cardapio.close()

arquivo_clientes = open('clientes.dat','wb')
pickle.dump(clientes, arquivo_clientes)
arquivo_clientes.close()

arquivo_pedidos = open('pedidos.dat','wb')
pickle.dump(pedidos,arquivo_pedidos)
arquivo_pedidos.close()



    
    


















