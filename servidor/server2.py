import socket
import os
from threading import Thread

config= {
    "host":"localhost",
    "port":7777,
    "buff":1024,
    "notify":{
        "width":50,
        "flag": "#"
    },
    "path_download":{
        "default": "./download"
    }
}

allClients= []
allMensages = []

def main():
    server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((config['host'], config['port']))
        # @ FICAR OUVINDO A PORTA
        # server.listen(1) # parametro para limitar o número de conexoes
        server.listen()
        notification('Server Online ')       

    except:
        return "\nServer já iniciado, porta ocupada"

    while True:
        # @ AGUARDA CONNEXÃO DE USUARIO
        cliente, addrs = server.accept()

        # @ ADICIONA UM NOVO USUARIO NA LISTA
        allClients.append(cliente)

        # @ CRIA UMA THREAD PARA CADA USUARIO
        trendInit = Thread(target=mensageUser, args=[cliente])
        trendInit.start()
        print(f'USUARIOS CONNECTADOS: {len(allClients)}')


# @ RECEBE A MENSAGEM DOS CLIENTES
def mensageUser(cliente:str)->None:  
    # @ ATUALIZA NOVOS CLIENTES COM AS ULTIMAS MENSAGENS 
    if len(allMensages) != 0:
        for mensagem in allMensages:
            enviar = f"{mensagem} \n".encode('utf-8')
            cliente.send(enviar) 

    while True:
        try:
            msg = cliente.recv(config['buff']).decode("utf-8") 
            # @ ARMAZENA TODAS AS CONVERSAS E ATUALIZA PARA NOVOS USUARIOS
            allMensages.append(msg)          
            brodcast(msg, cliente)
            print(msg)
        except:
            notification("function user msg")
            removeUser(cliente)
            break


def brodcast(msg: str, user:str)->None:
    # @ ENVIA MENSAGEM PARA TODOS OS USUARIOS
    for cliente in allClients:
        if cliente != user:
            try:
                cliente.send(msg.encode('utf-8'))                 
            except:
                notification("function brodcast")
                removeUser(user)


# @ REMOVE USUARIO DA LISTA
def removeUser(user: str)->None:
    notification("function userRemove")
    allClients.remove(user)
    print(f'USUARIOS CONNECTADOS: {len(allClients)}')


# @ NOTIFICAÇÃO PERSONALIZADA
def notification(msg:str)->None:
    tamanho = config['notify']['width']
    flag = config['notify']['flag']

    print(f' {msg} '.center(tamanho,flag))

def systemParams():
    download = config['path_download']['default']
    if not os.path.exists(download):
        os.mkdir(download)


if __name__ == "__main__":
    systemParams()
    main()

