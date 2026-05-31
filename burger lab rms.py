#restaurante, bar
#crud para cardapio, clientes, pedidos, relatorio, sobre o sistema
resp = ''
def limpar_terminal():
    print("\033[H\033[J", end="")
def titulo_reustarante():
    print('''
████╗ ██╗  ██╗██████╗  ██████╗ ███████╗██████╗     ██╗      █████╗ ██████╗ 
██╔═██╗██║  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗    ██║     ██╔══██╗██╔══██╗
██████╔╝██║  ██║██████╔╝██║  ███╗█████╗  ██████╔╝    ██║     ███████║██████╔╝
██╔══██╗██║  ██║██╔══██╗██║   ██║██╔══╝  ██╔══██╗    ██║     ██╔══██║██╔══██╗
██████╔╝╚█████╔╝██║  ██║╚██████╔╝███████╗██║  ██║    ███████╗██║  ██║██████╔╝
╚═════╝  ╚════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═════╝
        ''')

while resp != '0':
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
        while resp2 != '5':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"        📜 menu do cardapio ")
            print("================================================")
            print("  [1] Cadastrar novo Prato")
            print("  [2] excluir prato")
            print("  [3] alterar prato")
            print("  [4] procurar prato")
            print("  [5] sair")
            resp2 = input("escolha uma das opções: ")
            if resp2 == '1':
                limpar_terminal()
                titulo_reustarante()
                print("================================================")
                print(f"        🍽️ cadastre um novo prato! ")
                print("================================================")
                prato = input("🍽️ digite o nome do prato: ")
                preco = input("💵 digite o preço do prato: ")
                codigo = input("🔢 digite o código do prato ")
                disponibilidade = input("✅ digite se o prato está disponivel ou não: ")
                print("novo prato cadastrado!")
                print("\t=============================")
                print("\t=          ATENÇÃO          =")
                print("\t=   Isso é uma simulação!   =")
                print("\t= Esta funcionalidade ainda =")
                print("\t=  está sendo implementada. =")
                print("\t=============================")
                cont = input("Tecle <ENTER> para continuar...")
            if resp2 == '2':
                limpar_terminal()
                titulo_reustarante()
                print("================================================")
                print(f"        ❌ exclua um prato! ")
                print("================================================")
                codigo = input("digite o codigo do prato a ser excluido: ")
                print(f"o prato {codigo} foi excluido! ")
                print("\t=============================")
                print("\t=          ATENÇÃO          =")
                print("\t=   Isso é uma simulação!   =")
                print("\t= Esta funcionalidade ainda =")
                print("\t=  está sendo implementada. =")
                print("\t=============================")
                cont = input("Tecle <ENTER> para continuar...")
            if resp2 == '3':
                limpar_terminal()
                titulo_reustarante()
                print("================================================")
                print(f"        🍽️ altere um prato! ")
                print("================================================")
                codigo = input("🔢 digite o código do prato ")
                prato = input("🍽️ digite o nome do prato: ")
                preco = input("💵 digite o preço do prato: ")
                disponibilidade = input("✅ digite se o prato está disponivel ou não: ")
                print("prato alterado!")
                print("\t=============================")
                print("\t=          ATENÇÃO          =")
                print("\t=   Isso é uma simulação!   =")
                print("\t= Esta funcionalidade ainda =")
                print("\t=  está sendo implementada. =")
                print("\t=============================")
                cont = input("Tecle <ENTER> para continuar...")
            if resp2 == '4':
                limpar_terminal()
                titulo_reustarante()
                print("================================================")
                print(f"        🔍 procure um prato! ")
                print("================================================")
                codigo = input("🔢 digite o código do prato ")
                print("nome do prato 🍽️ : lagrima dos alunos")
                print("preço 💵 : tudo")
                print(f"codigo 🔢: {codigo}")
                print("disponibilidade ✅: disponivel ")
                cont = input("Tecle <ENTER> para continuar...")
    elif resp == '2':
        limpar_terminal()
        titulo_reustarante()
        print("================================================")
        print(f"        👥 menu dos clientes ")
        print("================================================")
        print("  [1] Cadastrar novo cliente")
        print("  [2] excluir cliente")
        print("  [3] Alterar dados de um cliente")
        print("  [4] procurar cliente")
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
        cont = input("Tecle <ENTER> para continuar...")
    elif resp == '3':
        limpar_terminal()
        titulo_reustarante()
        print("================================================")
        print(f"        🍳 menu dos pedidos ")
        print("================================================")
        print("  [1] Cadastrar novo pedido")
        print("  [2] excluir pedido")
        print("  [3] Alterar dados de um pedido")
        print("  [4] procurar pedido")
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
        cont = input("Tecle <ENTER> para continuar...")
    elif resp == '4':
        limpar_terminal()
        titulo_reustarante()
        print("================================================")
        print(f"        🍳 menu dos relatorios ")
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
        cont = input("Tecle <ENTER> para continuar...")
    elif resp == '5':
        limpar_terminal()
        titulo_reustarante()
        print("================================================")
        print(f"      ⚙️ Você está no Módulo Informações ")
        print("================================================")
        print("================================================================================================")
        print("  Projeto de Gestão de um restaurante para a máteria de Algoritmos e Lógica de Programação")
        print("================================================================================================")
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
    
    


















