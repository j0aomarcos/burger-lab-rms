from uteis import *
from validacao import *
from externo import *
def printar_cardapio(cardapio):
    print(cardapio)
def menu_cardapio():
    cardapio = recup_cardapio()
    resp2 = ''
    while resp2 !='0':
        limpar_terminal()
        titulo_reustarante
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
            validade_do_preco = False
            while validade_do_preco is False:
                preco_prato = input("💵 digite o preço do prato: ")
                if validar_preco(preco_prato):
                    validade_do_preco = False
                else:
                    print('tente de novo')
            print()
            codigo_prato = ''
            validade = False
            while not validade:
                codigo_prato = input('digite um código de 4 digitos: ')
                validade = validacao_codigo(codigo_prato)
                if not validade:
                    print('tente novamente colocar o código')
                cardapio[codigo_prato] = [nome_prato,preco_prato,True]
                salvar_cardapio(cardapio)
                print()
                print(f'nome do prato: {cardapio[codigo_prato][0]}')
                print(f'preço do prato: {cardapio[codigo_prato][1]}')
                print('disponibilidade do prato: disponivel')
                print()
                printar_cardapio(cardapio)
            print()
            input("Tecle <ENTER> para continuar...")
        if resp2 == '2':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"         🔍 procure um prato!                  ")
            print("================================================")
            print()
            busca = input("Digite o código ou o nome do prato para buscá-lo: ").strip()
            if busca in cardapio and cardapio[busca][2] == True:
                print("🍽️ Nome do prato     :", cardapio[busca][0])
                print("💵 Preço do prato    :", cardapio[busca][1])
                print("✅ Disponibilidade  :", 'disponivel')
            else:
                nomes_no_cardapio = []
                for infos in cardapio.values():
                    pratos_minusculo = infos[0].lower()
                    nomes_no_cardapio.append(pratos_minusculo)
                if busca.lower() in nomes_no_cardapio:
                    for codigo, infos in cardapio.items():
                        if infos[0].lower() == busca.lower():
                            if infos[2] == True:
                                print("🍽️ Nome do prato     :", infos[0])
                                print("💵 Preço do prato    :", infos[1])
                                print("✅ Disponibilidade  :", 'disponivel')                             
                else:
                    print('Prato não encontrado por código ou nome ou o prato está indisponivel.')
            print()
            input("Tecle <ENTER> para continuar...")
        if resp2 == '3':
            limpar_terminal()
            titulo_reustarante()
            print("================================================")
            print(f"        🍽️ altere um prato! ")
            print("================================================")
            print()
            alterar_prato = input("🔢 digite o código do prato ou o nome: ").strip()
            codigo_nome = None
            if alterar_prato in cardapio:
                codigo_nome = alterar_prato
            else:
                nomes_cardapio = []
                for infos in cardapio.values():
                    nome_prato = infos[0]
                    minu = nome_prato.lower()
                    nomes_cardapio.append(minu)
                    if alterar_prato.lower() in nomes_cardapio:
                        for codigos, infos in cardapio.items():
                            if infos[0].lower() == alterar_prato.lower():
                                codigo_nome = codigos
            if codigo_nome is not None:
                print('antigas informações: ')
                print("🍽️ Nome do prato     :", cardapio[codigo_nome][0])
                print("💵 Preço do prato    :", cardapio[codigo_nome][1])
                if cardapio[codigo_nome][2] == True:
                    print("✅ Disponibilidade  :", 'disponivel')
                else:
                    print("✅ Disponibilidade  :", 'indisponivel')
                print('digite as modificações que deseje fazer: ')
                alterar_nome1 = input('digite o novo nome: ')
                alterar_preco_novo = False
                while alterar_preco_novo is False:
                    alterar_preco = input('digite o novo preço: ')
                    if validar_preco(alterar_preco):
                        alterar_preco_novo is True
                    else:
                        print('tente de novo: ')

                alterar_disponibilidade = input('o prato está disponivel: ')
                if alterar_disponibilidade.lower() == 's' or alterar_disponibilidade.lower() == 'sim':
                    disponibilidade = True
                else:
                    disponibilidade = False
                cardapio[codigo_nome] = [alterar_nome1,alterar_preco,disponibilidade]
                salvar_cardapio(cardapio)
                print()
                print('prato alterado com sucesso')
                print(f'verifique a alteração:')
                print(f'nome: {cardapio[codigo_nome][0]}')
                print(f'preço:{cardapio[codigo_nome][1]}')
                if cardapio[codigo_nome][2] == True:
                    print('disponibilidade: disponivel')
                else:
                    print('disponibilidade: inativo')
                cardapio = recup_cardapio()
            else:
                print('prato não encontrado.')

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
                if cardapio[excluir_prato][2] == True:
                    print("🍽️ Nome do prato:", cardapio[excluir_prato][0])
                    print("💵 Preço do prato:", cardapio[excluir_prato][1])
                    print("✅ Disponibilidade:",'dísponivel')
                    print()
                    confirmar = input('aperte "s" para confirmar a exclusão:  ')
                    if confirmar.lower() == "s":
                        cardapio[excluir_prato][2] = False
                        salvar_cardapio(cardapio)
                        print('prato excluido!')
                        print()
                        print(f'nome: {cardapio[excluir_prato][0]}')
                        print(f'Preço: {cardapio[excluir_prato][1]}')
                        print(f'disponibilidade: {cardapio[excluir_prato][2]}')
                    else:
                        print('exclusão cancelada!')
                        input("Tecle <ENTER> para continuar...")
                else:
                    print('prato não disponivel')
            else:
                print('prato não encontrado!')
            print()
            input("Tecle <ENTER> para continuar...")
            salvar_cardapio(cardapio)

