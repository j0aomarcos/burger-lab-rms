from datetime import datetime
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
        print("Erro: O ID não pode ser vazio.")
        return False
    if not codigo.isdigit():
        print("Erro: O ID deve conter apenas números.")
        return False
    if len(codigo) != 5:
        print(f"Erro: O ID deve ter exatamente 5 dígitos.")
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
                
def validar_preco(valor):
    while True:
        try:
            valor = float(valor)
            return valor
        except:
            valor = input('Resposta Inválida, tente novamente: ')

def validar_fone(telefone):
    apenas_numeros = ""
    for caractere in telefone:
        if caractere.isdigit():
            apenas_numeros = apenas_numeros + caractere
    if len(apenas_numeros) != 11:
        return False
    ddd = apenas_numeros[0]+apenas_numeros[1]
    ddd_validos = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "21", "22", "24", "27", "28", "31", "32", "33", "34", "35", "37", "38", "41", "42", "43", "44", "45", "46", "47", "48", "49", "51", "53", "54", "55", "61", "62", "63", "64", "65", "66", "67", "68", "69", "71", "73", "74", "75", "77", "79", "81", "82", "83", "84", "85", "86", "87", "88", "89", "91", "92", "93", "94", "95", "96", "97", "98", "99"]
    if ddd not in ddd_validos:
        return False
    if apenas_numeros[2] !='9':
        return False
    return True

def completar_email(usuario):
    email_completo = f"{usuario}@gmail.com"
    return email_completo

def validar_data(data_texto, formato="%d/%m/%Y"):
    try:
        data_objeto = datetime.strptime(data_texto, formato).date()
    except ValueError:
        return False  
    hoje = datetime.now().date()
    ano_atual = hoje.year
    
    if data_objeto < hoje:
        print("Erro: A data não pode ser no passado!")
        return False
        
    if data_objeto.year != ano_atual:
        print(f"Erro: A data precisa ser do ano atual ({ano_atual})!")
        return False
        
    return True