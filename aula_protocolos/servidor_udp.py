from socket import*

servidor = "127.0.0.1"
porta = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((servidor,porta))
print("SERVIDOR PRONTO...")

while True:
    dados, origem = obj_socket.recvfrom(65535)
    print("ORIGEM:..........:", origem)
    print("DADOS RECEBIDOS..:", dados.decode())
    resposta = input("DIGITE A RESPOSTA: ")
    obj_socket.sendto(resposta.encode(),origem)

obj_socket.close()