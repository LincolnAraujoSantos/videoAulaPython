from ftplib import*

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

usuario = input("DIGITE O USUARIO: ")
senha = input("DIGITE A SENHA: ")

ftp.login(usuario,senha)

print("DIRETÓRIO ATUAL DE TRABALHO: ", ftp.pwd())

ftp.cwd('pub')

print("DIRETÓRIO CORRENTE:", ftp.pwd())

print(ftp.retrlines('LIST'))
ftp.quit()