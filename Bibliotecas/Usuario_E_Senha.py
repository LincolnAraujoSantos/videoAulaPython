import getpass

#getpass
usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:...")

if usuario=="usertricaster" and senha == "123":
    print("Bem vindo!!!")
else:
    print("Acesso Negado")
