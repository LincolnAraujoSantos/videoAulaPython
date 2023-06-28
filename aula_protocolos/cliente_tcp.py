from socket import*

servidor = "127.0.0.1"
porta = 43210

msg = bytes(input("DIGITE ALGO: "), 'utf-8')
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor,porta))
obj_socket.send(msg)
resposta = obj_socket.recv(1024)
print("RECEBEMOS: ", resposta)
obj_socket.close()