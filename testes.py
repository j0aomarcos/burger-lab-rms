import os
import pickle

########################################
##### Sistema BitScola - Versão 10 #####
########################################

###
### Funções para manipulação dos dados dos alunos, professores e turmas
###

def recupera_alunos():
    try:
        alunos = {}
        arq_alunos = open("alunos.dat", "rb")
        alunos = pickle.load(arq_alunos)
        arq_alunos.close()
    except:
        alunos = {
            '123': ["Homer Simpson", "homer@springfield.com", "99999-9999"],
            '234': ["Marge Simpson", "marge@springfield.com", "88888-8888"],
            '345': ["Bart Simpson", "bart@springfield.com", "77777-7777"],
            '456': ["Lisa Simpson", "lisa@springfield.com", "66666-6666"],
            '678': ["Maggie Simpson", "maggie@springfield.com", "55555-5555"]
        }
        arq_alunos = open("alunos.dat", "wb")
        pickle.dump(alunos, arq_alunos)
        arq_alunos.close()
    return alunos



def recupera_professores():
    try:
        professores = {}
        arq_profs = open("professores.dat", "rb")
        professores = pickle.load(arq_profs)
        arq_profs.close()
    except:
        professores = {
            '11111111111': ['Edna Krabappel', 'krabappel@springfield.com', '(84) 99988-8777'],
            '22222222222': ['Elizabeth Hoover', 'hoover@springfield.com', '(83) 99900-0111'],
            '33333333333': ['Seymour Skinner', 'skinner@springfield.com', '(81) 98889-8888'],
            '44444444444': ['Dewey Largo', 'largo@springfield.com', '(84) 98789-7777'],
            '55555555555': ['Pompeii Krupt', 'krupt@springfield.com', '(82) 98765-4321']
        }
        arq_profs = open("professores.dat", "wb")
        pickle.dump(professores, arq_profs)
        arq_profs.close()
    return professores


def recupera_turmas():
    try:
        turmas = {}
        arq_turmas = open("turmas.dat", "rb")
        turmas = pickle.load(arq_turmas)
        arq_turmas.close()
    except:
        turmas = {
            'FOX1111': ['Matemática', '234T34', 'Sala 3', '11111111111'],
            'FOX2222': ['Ciências', '34T12', 'Sala 2', '33333333333'],
            'FOX3333': ['Música', '35T56', 'Auditório', '44444444444'],
            'FOX4444': ['Educação Física', '6T56', 'Quadra', '55555555555'],
            'FOX5555': ['Artes', '5N1234', 'Sala 1', '22222222222']
        } 
        arq_turmas = open("turmas.dat", "wb")
        pickle.dump(turmas, arq_turmas)
        arq_turmas.close()
    return turmas



def grava_alunos(alunos):
    arq_alunos = open("alunos.dat", "wb")
    pickle.dump(alunos, arq_alunos)
    arq_alunos.close()



def grava_professores(professores):
    arq_profs = open("professores.dat", "wb")
    pickle.dump(professores, arq_profs)
    arq_profs.close()



def grava_turmas(turmas):
    arq_turmas = open("turmas.dat", "wb")
    pickle.dump(turmas, arq_turmas)
    arq_turmas.close()



###################################################
###                                             ###
###     P R O G R A M A   P R I N C I P A L     ###
###                                             ###
###################################################



###
### Recupera os dados do arquivo, caso existam dados armazenados
### Caso contrário, cria os arquivos e preenche com dados de exemplo
###
 
alunos = recupera_alunos()
professores = recupera_professores()
turmas = recupera_turmas()

op_princ = ''
while op_princ != '0':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("############################################")
    print("######       Sistema BitScola       ######")
    print("############################################")
    print("#####      1 - Módulo Aluno            #####")
    print("#####      2 - Módulo Professor        #####")
    print("#####      3 - Módulo Turma            #####")
    print("#####      4 - Módulo Relatório        #####")
    print("#####      5 - Módulo Informações      #####")
    print("#####      0 - Sair                    #####")
    op_princ = input("##### Escolha sua opção: ")

    if op_princ == '1':
        op_aluno = ''
        while op_aluno != '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
            print("############################################")
            print("#####           Módulo Aluno           #####")
            print("############################################")
            print("##### 1 - Cadastrar Aluno              #####")
            print("##### 2 - Exibir Dados do Aluno        #####")
            print("##### 3 - Alterar Dados do Aluno       #####")
            print("##### 4 - Excluir Aluno                #####")
            print("##### 0 - Retornar ao Menu Principal   #####")
            op_aluno = input("##### Escolha sua opção: ")
            print()
            if op_aluno == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("############################################")
                print("#####           Cadastra Aluno         #####")
                print("############################################")
                print()
                nome = input("##### Nome: ")
                print()
                matr = input("##### Matrícula: ")
                print()
                email = input("##### Email: ")
                print()
                fone = input("##### Celular: ")
                print()
                alunos[matr] = [nome, email, fone]
                print("Alunos:", alunos)    # Apenas para conferir inclusão
                print("Aluno cadastrado com sucesso!")
                print()
                input("Tecle <ENTER> para continuar...")
            elif op_aluno == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("############################################")
                print("#####        Exibe Dados do Aluno      #####")
                print("############################################")
                print()
                matr = input("##### Matrícula: ")
                print()
                if matr in alunos:
                    print("##### Nome     :", alunos[matr][0])
                    print("##### Email    :", alunos[matr][1])
                    print("##### Celular  :", alunos[matr][2])
                else:
                    print("Aluno não encontrado!")
                print()
                input("Tecle <ENTER> para continuar...")
            elif op_aluno == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("############################################")
                print("#####       Altera Dados do Aluno      #####")
                print("############################################")
                print()
                matr = input("##### Matrícula: ")
                print()
                if matr in alunos:
                    print("##### Dados atuais do aluno:")
                    print("##### Nome     :", alunos[matr][0])
                    print("##### Email    :", alunos[matr][1])
                    print("##### Celular  :", alunos[matr][2])
                    print()
                    print("##### Digite os novos dados do aluno:")
                    nome = input("##### Novo nome   : ")
                    email = input("##### Novo email  : ")
                    fone = input("##### Novo celular: ")
                    alunos[matr] = [nome, email, fone]
                    print()
                    print("Aluno alterado com sucesso!")
                    print()
                    print("Alunos:", alunos)    # Apenas para conferir alteração
                    print()
                else:
                    print("Aluno não encontrado!")
                print()
                input("Tecle <ENTER> para continuar...")
            elif op_aluno == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("############################################")
                print("#####         Exclui Aluno             #####")
                print("############################################")
                print()
                matr = input("##### Matrícula: ")
                print()
                if matr in alunos:
                    print("##### Aluno encontrado:")
                    print("##### Nome     :", alunos[matr][0])
                    print("##### Email    :", alunos[matr][1])
                    print("##### Celular  :", alunos[matr][2])
                    print()
                    confirma = input("Tecle 's' para confirmar exclusão...")
                    if confirma.lower() == 's':
                        del alunos[matr]
                        print("Aluno excluído com sucesso!")
                        print()
                        print("Alunos:", alunos)    # Apenas para conferir exclusão
                    else:
                        print("Exclusão cancelada!")
                else:
                    print("Aluno não encontrado!")
                print()
                input("Tecle <ENTER> para continuar...")
    
    elif op_princ == '2':
        op_prof = ''
        while op_prof != '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
            print("############################################")
            print("#####         Módulo Professor         #####")
            print("############################################")
            print("##### 1 - Cadastrar Professor          #####")
            print("##### 2 - Exibir Dados do Professor    #####")
            print("##### 3 - Alterar Dados do Professor   #####")
            print("##### 4 - Excluir Professor            #####")
            print("##### 0 - Retornar ao Menu Principal   #####")
            op_prof = input("##### Escolha sua opção: ")
            print()
            if op_prof == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("############################################")
                print("#####         Cadastra Professor       #####")
                print("############################################")
                print()
                nome = input("##### Nome: ")
                print()
                cpf = input("##### CPF: ")
                print()
                email = input("##### Email: ")
                print()
                fone = input("##### Celular: ")
                print()
                professores[cpf] = [nome, email, fone]
                print("Professores:", professores)    # Apenas para conferir inclusão
                print("Professor cadastrado com sucesso!")
                print()
                input("Tecle <ENTER> para continuar...")
            elif op_prof == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("############################################")
                print("#####      Exibe Dados do Professor    #####")
                print("############################################")
                print()
                cpf = input("##### CPF: ")
                print()
                if cpf in professores:
                    print("##### Nome   :", professores[cpf][0])
                    print("##### Email  :", professores[cpf][1])
                    print("##### Celular:", professores[cpf][2])
                else:
                    print("Professor não encontrado!")
                print()
                input("Tecle <ENTER> para continuar...")
            elif op_prof == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("############################################")
                print("#####     Altera Dados do Professor    #####")
                print("############################################")
                print()
                cpf = input("##### CPF: ")
                print()
                if cpf in professores:
                    print("##### Dados atuais do professor:")
                    print("##### Nome   :", professores[cpf][0])
                    print("##### Email  :", professores[cpf][1])
                    print("##### Celular:", professores[cpf][2])
                    print()
                    print("##### Digite os novos dados do professor:")
                    nome = input("##### Novo nome   : ")
                    email = input("##### Novo email  : ")
                    fone = input("##### Novo celular: ")
                    professores[cpf] = [nome, email, fone]
                    print()
                    print("Professor alterado com sucesso!")
                    print()
                    print("Professores:", professores)    # Apenas para conferir alteração
                    print()
                else:
                    print("Professor não encontrado!")
                print()
                input("Tecle <ENTER> para continuar...")
            elif op_prof == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("############################################")
                print("#####       Exclui Professor           #####")
                print("############################################")
                print()
                cpf = input("##### CPF: ")
                print()
                if cpf in professores:
                    print("##### Professor encontrado:")
                    print("##### Nome   :", professores[cpf][0])
                    print("##### Email  :", professores[cpf][1])
                    print("##### Celular:", professores[cpf][2])
                    print()
                    confirma = input("Tecle 's' para confirmar exclusão...")
                    if confirma.lower() == 's':
                        del professores[cpf]
                        print("Professor excluído com sucesso!")
                        print()
                        print("Professores:", professores)    # Apenas para conferir exclusão
                    else:
                        print("Exclusão cancelada!")
                else:
                    print("Professor não encontrado!")
                print()
                input("Tecle <ENTER> para continuar...")
    
    elif op_princ == '3':
        op_turma = ''
        while op_turma != '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
            print("############################################")
            print("#####           Módulo Turma           #####")
            print("############################################")
            print("##### 1 - Cadastrar Turma              #####")
            print("##### 2 - Exibir Dados da Turma        #####")
            print("##### 3 - Alterar Dados da Turma       #####")
            print("##### 4 - Excluir Turma                #####")
            print("##### 0 - Retornar ao Menu Principal   #####")
            op_turma = input("##### Escolha sua opção: ")
            print()
            if op_turma == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("############################################")
                print("#####           Cadastra Turma         #####")
                print("############################################")
                print()
                nome_turma = input("##### Nome da Turma: ")
                print()
                cod_turma = input("##### Código da Turma: ")
                print()
                horario = input("##### Horário das Aulas: ")
                print()
                local = input("##### Local das Aulas: ")
                print()
                cpf_prof = input("##### CPF do Professor: ")
                print()
                turmas[cod_turma] = [nome_turma, horario, local, cpf_prof]
                print("Turmas:", turmas)    # Apenas para conferir inclusão
                print("Turma cadastrada com sucesso!")
                print()
                input("Tecle <ENTER> para continuar...")
            elif op_turma == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("############################################")
                print("#####        Exibe Dados da Turma      #####")
                print("############################################")
                print()
                cod_turma = input("##### Código da Turma: ")
                print()
                if cod_turma in turmas:
                    print("##### Nome     :", turmas[cod_turma][0])
                    print("##### Horário  :", turmas[cod_turma][1])
                    print("##### Local    :", turmas[cod_turma][2])
                    print("##### Professor:", turmas[cod_turma][3])
                else:
                    print("Turma não encontrada!")
                print()
                input("Tecle <ENTER> para continuar...")
            elif op_turma == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("############################################")
                print("#####       Altera Dados da Turma      #####")
                print("############################################")
                print()
                cod_turma = input("##### Código da Turma: ")
                print()
                if cod_turma in turmas:
                    print("##### Dados atuais da turma:")
                    print("##### Nome     :", turmas[cod_turma][0])
                    print("##### Horário  :", turmas[cod_turma][1])
                    print("##### Local    :", turmas[cod_turma][2])
                    print("##### Professor:", turmas[cod_turma][3])
                    print()
                    print("##### Digite os novos dados da turma:")
                    nome_turma = input("##### Novo nome da turma: ")
                    horario = input("##### Novo horário: ")
                    local = input("##### Novo local: ")
                    cpf_prof = input("##### Novo CPF do professor: ")
                    turmas[cod_turma] = [nome_turma, horario, local, cpf_prof]
                    print()
                    print("Turma alterada com sucesso!")
                    print()
                    print("Turmas:", turmas)    # Apenas para conferir alteração
                else:
                    print("Turma não encontrada!")
                print()
                input("Tecle <ENTER> para continuar...")
            elif op_turma == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("############################################")
                print("#####         Exclui Turma             #####")
                print("############################################")
                print()
                cod_turma = input("##### Código da Turma: ")
                print()
                if cod_turma in turmas:
                    print("##### Turma encontrada:")
                    print("##### Nome     :", turmas[cod_turma][0])
                    print("##### Horário  :", turmas[cod_turma][1])
                    print("##### Local    :", turmas[cod_turma][2])
                    print("##### Professor:", turmas[cod_turma][3])
                    print()
                    confirma = input("Tecle 's' para confirmar exclusão...")
                    if confirma.lower() == 's':
                        del turmas[cod_turma]
                        print("Turma excluída com sucesso!")
                        print()
                        print("Turmas:", turmas)    # Apenas para conferir exclusão
                    else:
                        print("Exclusão cancelada!")
                else:
                    print("Turma não encontrada!")
                print()
                input("Tecle <ENTER> para continuar...")
    
    elif op_princ == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print("############################################")
        print("#####         Módulo Relatório         #####")
        print("############################################")
        print("##### 1 - Lista Geral de Alunos        #####")
        print("##### 2 - Lista Geral de Professores   #####")
        print("##### 3 - Lista Geral de Turmas        #####")
        print("##### 4 - Lista de Alunos por Turma    #####")
        print("##### 5 - Lista de Turmas p/ Professor #####")
        print("##### 0 - Retornar ao Menu Principal   #####")
        op_aluno = input("##### Escolha sua opção: ")
        print()
        input("Tecle <ENTER> para continuar...")
    
    elif op_princ == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print("############################################")
        print("#####  Você está no Módulo Informações  ####")
        print("############################################")
        print()
        print("#####  Sistema de Gestão de uma Escola  ####")
        print("#####  Equipe de desenvolvimento:       ####")
        print("#####  * Flavius Gorgônio @flgorgonio   ####")
        print("#####  Licença Pública Geral GNU        ####")
        print("#####  www.gnu.org/licenses/gpl.html    ####")
        print()
        input("Tecle <ENTER> para continuar...")
    
    elif op_princ == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print("############################################")
        print("#####  Você encerrou o programa, até logo! #")
        print("############################################")
        print()
        input("Tecle <ENTER> para continuar...")
    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
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

print("Obrigado por usar o Sistema BitScola")



###
### Grava os dados no arquivo após o encerramento do programa
###

grava_alunos(alunos)
grava_professores(professores)
grava_turmas(turmas)
