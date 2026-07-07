from uteis import *
from funcoes_relatorios import *
from externo import *
cardapio = recup_cardapio()
clientes = recup_clientes()
pedidos = recup_pedidos()
def menu_relatorios():
        resp2 = ''
        while resp2 != '0':
                limpar_terminal()
                titulo_reustarante()
                print("================================================")
                print(f"         menu dos relatorios ")
                print("================================================")
                print("  [1] lista do cardapio completa")
                print("  [2] lista de clientes completa")
                print("  [3] lista de pedidos completa")
                print("  [4] lista de relatorios ativos/inativos")
                print("  [5] pensando")
                print("  [0] sair")
                resp2 = input("Escolha sua opção: ")
                if resp2 == '1':
                        relatorio_cardapio(cardapio)
                        input("Tecle <ENTER> para continuar...")
                elif resp2 == '2':
                        relatorio_clientes(clientes)
                        input("Tecle <ENTER> para continuar...")
                elif resp2 == '3':
                        relatorio_pedidos(pedidos,cardapio,clientes)
                        input("Tecle <ENTER> para continuar...")
                elif resp2 == '4':
                        resp3 = ''
                        while resp3 != '0':
                                limpar_terminal()
                                print('escolha uma das opções abaixo: ')
                                print('[1] cardapio')
                                print('[2] clientes')
                                print('[3] pedidos')
                                print('[0] sair')
                                resp3 = input('escolha uma opção: ')
                                if resp3 == '1':
                                        escolha = input('escolha entre itens ativos(1) ou inativos(0): ')
                                        if escolha == '1':
                                                relatorio_cardapio_ativos(cardapio)
                                        else:
                                                cardapio_inativos(cardapio)
                                        input("Tecle <ENTER> para continuar...")
                                elif resp3 == '2':
                                        escolha = input('escolha entre clientes ativos(1) ou inativos(0): ')
                                        if escolha == '1':
                                                relatorio_clientes_ativos(clientes)
                                        else:
                                                clientes_inativos(clientes)
                                        input("Tecle <ENTER> para continuar...")
                                elif resp3 == '3':
                                        escolha = input('escolha entre pedidos ativos(1) ou inativos(0): ')
                                        if escolha == '1':
                                                relatorio_pedidos_ativos(pedidos,cardapio,clientes)
                                        else:
                                                pedidos_inativos(pedidos,cardapio,clientes)
                                        input("Tecle <ENTER> para continuar...")

                
                        
