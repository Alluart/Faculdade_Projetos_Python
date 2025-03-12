lista_livro = []
id_global = 1

print('Bem-vindo à biblioteca do Thiago Agostinho!')

#Cadastro dos livros
def cadastrar_livros(id):
    global id_global
    nome_livro = input('Qual o nome do livro?\n')
    autor = input('Qual é o autor?\n')
    editora = input('Qual é a editora?\n')

    livro_cadastro = {'id' : id , 
                    'nome_livro': nome_livro, 
                    'autor': autor, 
                    'editora': editora}
#Adiciona a lista de livros
    lista_livro.append(livro_cadastro)
    id_global += 1  # Incrementa o id_global

def consultar_livros():
#Consulta os livros a escolha do usuario
    while True:
        opcoes = int(input('Qual das opcões você de seja seguir :\n 1. Consultar Todos \n 2. Consultar por Id \n 3. Consultar por Autor \n 4. Retornar ao menu\n'))
        if opcoes == 1:
            for livro_cadastro in lista_livro:
                print(f"Id: {livro_cadastro['id']} | Nome: {livro_cadastro['nome_livro']} | Autor: {livro_cadastro['autor']} | Editora: {livro_cadastro['editora']}")

        elif opcoes == 2:
            id_consulta = int(input('Qual a id do livro?\n'))
            for livro_cadastro in lista_livro:
                if livro_cadastro['id'] == id_consulta:
                    print(f"Id: {livro_cadastro['id']} | Nome: {livro_cadastro['nome_livro']} | Autor: {livro_cadastro['autor']} | Editora: {livro_cadastro['editora']}")
                    break
                else:
                    print('Id invalido')

        elif opcoes == 3:
            autor_consulta = input('Qual autor você gostaria de ver o livros?\n')
            for livro_cadastro in lista_livro:
                if livro_cadastro['autor'] == autor_consulta:
                    print(f"Id: {livro_cadastro['id']} | Nome: {livro_cadastro['nome_livro']} | Autor: {livro_cadastro['autor']} | Editora: {livro_cadastro['editora']}")   

        elif opcoes == 4:
            return
        
        else:
            print('Opção inválida')

def remover_livro():
#Remove o livro pela id
    while True:
        remover_id = int(input('Qual a id do livro que você gostaria de remover?\n'))
        for livro_cadastro in lista_livro:
            if livro_cadastro['id'] == remover_id:
                lista_livro.remove(livro_cadastro)
                return
        print('Id inválido')


while True:
#Chama as funçoes baseado na escolha do usuario
    opcoes = int(input('Qual das opcões você de seja seguir :\n 1. Cadastrar Livro \n 2. Consultar Livro \n 3. Remover Livro \n 4. Encerrar Programa'))
    if opcoes == 1:
        cadastrar_livros(id_global)

    elif opcoes == 2:
        consultar_livros()

    elif opcoes == 3:
        remover_livro()

    elif opcoes == 4:
        print('Programa encerrado.')
        break

    else:
        print('Opção inválida')
        continue