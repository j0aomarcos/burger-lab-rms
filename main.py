from informacoes import *
from relatorios import *
from cardapio import *
from clientes import *
from pedidos import *
from externo import *
from validacao import *
from uteis import *
from funcoes_relatorios import *
import pickle
cardapio = recup_cardapio()
clientes = recup_clientes()
pedidos = recup_pedidos()

resp = ''
limpar_terminal()
titulo_reustarante()

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
        menu_cardapio(cardapio)
    elif resp == '2':
        menu_clientes(clientes)
    elif resp == '3':
        menu_pedidos(pedidos)   
    elif resp == '4':
        menu_relatorios()
    elif resp == '5':
        menu_infor()
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

salvar_cardapio(cardapio)
salvar_clientes(clientes)
salvar_pedidos(pedidos)





    
    


















