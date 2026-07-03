def validacao_codigo(codigo):
    codigo = codigo.strip()
    if not codigo:
        print("Erro: O código não pode ser vazio.")
        return False
    if not codigo.isdigit():
        print("Erro: O código deve conter apenas números.")
        return False
    if len(codigo) != 4:
        print(f"Erro: O código deve ter exatamente 4 dígitos.")
        return False
    return True
                


def validacao_ID(codigo):
    codigo = codigo.strip()
    if not codigo:
        print("Erro: O código não pode ser vazio.")
        return False
    if not codigo.isdigit():
        print("Erro: O código deve conter apenas números.")
        return False
    if len(codigo) != 5:
        print(f"Erro: O código deve ter exatamente 5 dígitos.")
        return False
    return True

def validacao_pedido(codigo):
    codigo = codigo.strip()
    if not codigo:
        print("Erro: O código não pode ser vazio.")
        return False
    if not codigo.isdigit():
        print("Erro: O código deve conter apenas números.")
        return False
    if len(codigo) != 6:
        print(f"Erro: O código deve ter exatamente 6 dígitos.")
        return False
    return True
                

def validar_preco(preco):
    while True:
        try:
            preco = str(preco)
            preco = preco.replace(","    ,   ".")

            preco = float(preco)
            return preco
        except:
            preco = input("Preço Inválido, digite novamente: ")
    