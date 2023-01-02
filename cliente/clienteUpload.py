import socket

config= {
    "host":"localhost",
    "port":7777,
}

while True:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((config['host'], config['port']))
    print('CONNECTADO ! \n')
    arquivo = str(input('Envie seu arquivo: '))

    cliente.send(arquivo.encode())

    with open(arquivo, "wb") as file:        
        while True:
            dataclient = cliente.recv(100000)
            if  dataclient:
                file.write(dataclient)
            else:
                break
            print(dataclient)

    print('DOWNLOAD CONCLUIDO')












