import socket
import os

config= {
    "host":"localhost",
    "port":7777,
}

# @ ESCOLHE O TIPO DE CONNEXÃO VAI SER ACEITA  [IPV4, TCP]  [IPV4, DGRAM] UDP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# @ CONFIGURAÇÃO DE SERVIDOR E PORTA  ['']  HOST VAZIO ACEITA QUALQUER CONEXÃO
server.bind((config['host'], config['port']))

while True:
    # @ FICAR OUVINDO A PORTA
    # server.listen(1) # parametro para limitar o número de conexoes
    server.listen()
    print('Servidor Online')

    # @ PRIMEIRO PARAMETRO MOSTRA OQUE E RECEBIDO PELO USUARIO
    # @ SEGUNDO E O ENDEREÇO DO USUARIO QUE ESTA CONNETANDO NO SERVER
    connection, endereco = server.accept()

    # @ TRANSFORMA EM STRING , COM BUFFER DE 1024B E ARMAZENA NA VARIAVEL
    arquivo_user = connection.recv(1024).decode()

    if os.path.exists(arquivo_user):
        with open(arquivo_user, "rb") as file:
            for data in file.readlines():
                connection.send(data) 
            
            # @ FECHA CONNEXÃO APÓS O ENVIO DO ARQUIVO
            connection.close()
            print('arquivo enviado com sucesso')
    else:
        print('O Arquivo Não Existe ')


























