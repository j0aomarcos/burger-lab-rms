from uteis import *
from validacao import validacao_codigo,validar_preco
def menu_cardapio(cardapio):
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
            preco_prato = input("💵 digite o preço do prato: ")
            validar_preco(preco_prato)
            print()
            disponibilidade_prato = input("✅ digite se o prato está disponivel ou não: ")
            print()
            codigo_prato = ''
            validade = False
            while not validade:
                codigo_prato = input('digite um código de 4 digitos: ')
                validade = validacao_codigo(codigo_prato)
                if not validade:
                    print('tente novamente colocar o código')
            if validade:
                if disponibilidade_prato.lower() == 's' or disponibilidade_prato.lower() == 'sim':
                    disponivel = True
                else:
                    disponivel = False
                cardapio[codigo_prato] = [nome_prato,preco_prato,disponivel]
                print()
                print(f'nome do prato: {cardapio[codigo_prato][0]}')
                print(f'preço do prato: {cardapio[codigo_prato][1]}')
                if cardapio[codigo_prato][2] == True:
                    print('disponibilidade do prato: disponivel')
                else:
                    print('disponibilidade: indisponivel')
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
            if busca in cardapio:
                print("🍽️ Nome do prato     :", cardapio[busca][0])
                print("💵 Preço do prato    :", cardapio[busca][1])
                print("✅ Disponibilidade  :", 'disponivel')
            else:
                nomes_no_cardapio = []
                for infos in cardapio.values():
                    pratos_minusculo = infos[0].lower()
                    nomes_no_cardapio.append(pratos_minusculo)
                if busca.lower() in nomes_no_cardapio:
                    # Se o nome existe, rodamos o laço para exibir os dados daquele prato específico
                    for codigo, infos in cardapio.items():
                        if infos[0].lower() == busca.lower():
                            print("🍽️ Nome do prato     :", infos[0])
                            print("💵 Preço do prato    :", infos[1])
                            if infos[2] == True:
                                print("✅ Disponibilidade  :", 'disponivel')
                            else:
                                print('disponibilidade: indisponivel')
                else:
                    print('Prato não encontrado por código ou nome.')
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
                codigo_nome == alterar_prato
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
                print("🍽️ Nome do prato     :", cardapio[codigo_nome][0])
                print("💵 Preço do prato    :", cardapio[codigo_nome][1])
                if cardapio[codigo_nome][2] == True:
                    print("✅ Disponibilidade  :", 'disponivel')
                else:
                    print("✅ Disponibilidade  :", 'indisponivel')
                print('digite as modificações que deseje fazer: ')
                alterar_nome1 = input('digite o novo nome: ')
                alterar_preco = input('digite o novo preço: ')
                validar_preco(alterar_preco)
                alterar_disponibilidade = input('o prato está disponivel: ')
                if alterar_disponibilidade.lower() == 's' or alterar_disponibilidade.lower() == 'sim':
                    disponibilidade = True
                else:
                    disponibilidade = False
                cardapio[codigo_nome] = [alterar_nome1,alterar_preco,disponibilidade]
                print()
                print('prato alterado com sucesso')
                print(f'verifique a alteração:')
                print(f'nome: {cardapio[codigo_nome][0]}')
                print(f'preço:{cardapio[codigo_nome][1]}')
                if cardapio[codigo_nome][2] == True:
                    print('disponibilidade: disponivel')
                else:
                    print('disponibilidade: indisponivel')
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
            if cardapio[excluir_prato][2] == True:
                print("🍽️ Nome do prato:", cardapio[excluir_prato][0])
                print("💵 Preço do prato:", cardapio[excluir_prato][1])
                print("✅ Disponibilidade:",'dísponivel')
                print()
                confirmar = input('aperte "s" para confirmar a exclusão:  ')
                if confirmar.lower() == "s":
                    cardapio[excluir_prato][2] = False
                    print('prato excluido!')
                    print()
                    print(f'cardapio {cardapio}')
                else:
                    print('exclusão cancelada!')
                    input("Tecle <ENTER> para continuar...")
            else:
                print('prato não disponivel')
            print()
            input("Tecle <ENTER> para continuar...")