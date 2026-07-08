from informacoes import *
from relatorios import *
from cardapio import *
from clientes import *
from pedidos import *
from externo import *
from validacao import *
from uteis import *
from datetime import datetime, timedelta
from funcoes_relatorios import *
import pickle
cardapio = recup_cardapio()
clientes = recup_clientes()
pedidos = recup_pedidos()

opcao_menu = ''
limpar_terminal()
titulo_reustarante()

while opcao_menu != '0':
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
    opcao_menu = input("escolha uma das opções: ")
    if opcao_menu == '1':
        menu_cardapio(cardapio)
    elif opcao_menu == '2':
        menu_clientes(clientes)
    elif opcao_menu == '3':
        menu_pedidos(pedidos,cardapio,clientes)   
    elif opcao_menu == '4':
        menu_relatorios()
    elif opcao_menu == '5':
        menu_infor()
    elif opcao_menu == '0':
        adeus()
    else:
        resp_errada()
salvar_cardapio(cardapio)
salvar_clientes(clientes)
salvar_pedidos(pedidos)





    
    


















