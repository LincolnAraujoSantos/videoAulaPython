def perguntar():
    return input("O que deseja realizar?\n" +
              "<I> - Para Inserir usuário\n"+
              "<P> - Para Pesquisar usuário\n"+
              "<E> - Para Excluir usuário\n"+
              "<L> - Para Listar usuário:\n").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite a última data de acesso: "),
                                                   input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))

def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome............:\n"+lista[0])
        print("Último acesso...:\n"+lista[1])
        print("Útilma estação..:\n"+lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.......")
        print("Login:", chave)
        print("Dados:", valor)

