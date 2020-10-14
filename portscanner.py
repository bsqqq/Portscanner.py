import socket

portas = [21,23,80,443,8443]

for porta in portas: 
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.1)
    codigo = cliente.connect_ex(('siteparascan.com', porta))
    if codigo == 0:
        print(porta, "OPEN")
    else:
        print(porta, "timed out || unavailable")