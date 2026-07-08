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

def adeus():
    print()
    print("############################################")
    print("#####  Você encerrou o programa, até logo! #")
    print("############################################")
    print()
    input("Tecle <ENTER> para continuar...")

def resp_errada():
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