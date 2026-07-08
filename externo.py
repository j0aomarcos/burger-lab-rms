import pickle
def recup_cardapio():
    cardapio = {}
    try:
        arquivo_cardapio = open('cardapio.dat','rb')
        cardapio = pickle.load(arquivo_cardapio)
        arquivo_cardapio.close()
    except:
        cardapio = {
            #Codigo: nome, preço, disponibilidade
            '1111':['Hamburguer',15,True],
            '2222':['pizza',30,True],
            '3333':['filé a parmegiano',45,True],
            '4444':['Camarão empanado',60,True]
        }
        arquivo_cardapio = open('cardapio.dat','wb')
        pickle.dump(cardapio, arquivo_cardapio)
        arquivo_cardapio.close()
    return cardapio

def recup_clientes():
    clientes = {}
    try:
        arquivo_clientes = open('clientes.dat','rb')
        clientes = pickle.load(arquivo_clientes)
        arquivo_clientes.close()
    except:
        clientes = {
        #ID: nome, email, número, ativo ou não
        '11111':['João Marcos','joaozinhos@gmai.com','4002-8922',True],
        '22222':['Matheus vinolla','matheuszinho@gmail.com','6767-6767',True],
        '33333':['Ruan Pablo','ruanzinho@gmail.com','4242-4242',True],
        '44444':['Flavius da Luz','flaviuszinho@gmail.com','1234-5678',True]
        }
        arquivo_clientes = open('clientes.dat','wb')
        pickle.dump(clientes, arquivo_clientes)
        arquivo_clientes.close()
    return clientes

def recup_pedidos():
    pedidos = {}
    try:
        arquivo_pedidos = open('pedidos.dat','rb')
        pedidos = pickle.load(arquivo_pedidos)
        arquivo_pedidos.close()
    except:
        pedidos = {
        #número do pedido: codigo do item, ID do cliente, data , se está ativo ou não
        '0001': ['1111', '11111','20/08/2026',True],
        '0002': ['2222','22222','21/09/2026',True],
        '0003': ['3333','33333','22/10/2026',True],
        '0004': ['4444','44444','23/11/2026',True]
        }
        arquivo_pedidos = open('pedidos.dat','wb')
        pickle.dump(pedidos,arquivo_pedidos)
        arquivo_pedidos.close()
    return pedidos

def salvar_cardapio(cardapio):
    arquivo_cardapio = open('cardapio.dat','wb')
    pickle.dump(cardapio, arquivo_cardapio)
    arquivo_cardapio.close()
def salvar_clientes(clientes):
    arquivo_clientes = open('clientes.dat','wb')
    pickle.dump(clientes, arquivo_clientes)
    arquivo_clientes.close()
def salvar_pedidos(pedidos):
    arquivo_pedidos = open('pedidos.dat','wb')
    pickle.dump(pedidos,arquivo_pedidos)
    arquivo_pedidos.close()


