
AGENDA = {}

from time import sleep


def escreva(contato):
    tam = len(contato) + 4
    print('~' * tam)
    print(f'  {contato}  ')
    print('~' * tam)


def mostrar_contato():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            #print('~' * 20)
    else:
        print('Agenda vazia')


def buscar_contato(contato):
    try:
        print('\033[36m~\033[m' * 50)
        print("Nome: ", contato)
        print("Telefone: ", AGENDA[contato]['telefone'])
        print("Email: ", AGENDA[contato]['email'])
        print("Endereço: ", AGENDA[contato]['endereco'])
    except KeyError:
        print('\033[31m>> Contato inexistente <<\033[m')
    except Exception as erro:
        print('\033[mUm erro inesperado ocorreu\033[m')
        #print(erro)


def ler_detalhes():
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    endereco = input('Digite o endereço: ')
    return telefone, email, endereco


def incluir_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print(f">>> Contato {contato} adicionado com sucesso <<<")


def excluir_contato(contato):
    try:
        confirm = int(input('\033[31mRealmente deseja excluir o contato?\033[m\nDigite 1 - Sim.\nDigite 2 - Para voltar ao menu principal. '))
        if confirm == 1:
            AGENDA.pop(contato)
            salvar()
        else:
            imprimir_menu()
        print(f'O contato {contato}, foi excluido com sucesso.')
    except KeyError:
        print('>>. Contato inexistente')
    except Exception as erro:
        print('\033[31mUm erro inesperado ocorreu\033[m')
        #print(erro)


def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("{},{},{},{}\n".format(contato, telefone, email, endereco))
        print('>>> Agenda atualizada com sucesso <<<')
    except Exception as error:
        print('\033[31mUm erro inesperado ocorreu\033[m')
        #print(error)


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('>>> Arquivo não encontrado <<<')
    except Exception as error:
        print('\033[31mUm erro inesperado ocorreu\033[m')
        #print(error)


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print('Dados carregados com sucesso')
        print(f'{len(AGENDA)} Contatos com sucesso')
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado')
    except Exception as error:
        print('\033[31mUm erro inesperado ocorreu\033[m')
        #print(error)


def imprimir_menu():
    print('\033[36m~\033[m' * 50)
    print('     1 \033[36m-\033[m Exibir todos os contatos da agenda')
    print('     2 \033[36m-\033[m Buscar contato na agenda')
    print('     3 \033[36m-\033[m Adicionar contato na agenda')
    print('     4 \033[36m-\033[m Editar contato na agenda')
    print('     5 \033[36m-\033[m Excluir contato na agenda')
    print('     6 \033[36m-\033[m Exportar a agenda')
    print('     7 \033[36m-\033[m Importar contatos.csv')
    print('     0 \033[36m-\033[m Sair da agenda')
    print('\033[36m~\033[m' * 50)


# Inicio do Programa

carregar()

while True:
    imprimir_menu()
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_contato()
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        print('Analisando...')
        sleep(1)
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')
        while contato.isalpha() is False:
            print('Informe apenas letras')
            contato = input('Digite o nome do contato: ')
            if contato.isalpha() is True:
                break
        try:
            AGENDA[contato]
            print('>>> Contato já existente <<<')
        except KeyError:
            telefone, email, endereco = ler_detalhes()
            incluir_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print(' Editando contato', contato)
            telefone, email, endereco = ler_detalhes()
            incluir_contato(contato, telefone, email, endereco)
        except KeyError:
            print('>>> Contato inexistente <<<')
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        print('Finalizando...')
        sleep(1)
        break
    else:
        print('>>> Opção inválida<<<')