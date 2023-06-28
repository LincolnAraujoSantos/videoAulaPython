from socket import*

servidor = "127.0.0.1"
porta = 43210

obj_socket = socket(AF_INET,SOCK_DGRAM)
obj_socket.connect((servidor,porta))
saida = ""

while saida!="X":
    msg = input("SUA MENSAGEM: ")
    obj_socket.sendto(msg.encode(),(servidor,porta))
    dados,origem = obj_socket.recvfrom(65535)
    print("RESPOSTA DO SERVIDOR: ",dados.decode())
    saida = input("DIGITE <X> PARA SAIR OU <ENTER> PARA CONTINUAR: ").upper()

obj_socket.close()