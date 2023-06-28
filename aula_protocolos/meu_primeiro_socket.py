import socket

resp="S"
while(resp=="S"):
    url = input("DIGITE UMA URL:")
    ip = socket.gethostbyname(url)
    print("O IP REFERENTE A URL INFORMADA É: ", ip)
    resp = input("DIGITE <S> PARA CONTINUAR: ").upper()
