import socket
from threading import Thread


config= {
    "host":"localhost",
    "port":7777,
    "buff":1024,
    "notify":{
        "width":50,
        "flag": "#"
    },
}

def main():
    cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((config['host'], config['port']))

    nome_usuario= input('Digite seu Nome: ')    

    thread_1= Thread(target=mensagEnv, args=[cliente, nome_usuario]) 
    thread_2= Thread(target=mensagRecebida, args=[cliente])
    
    thread_1.start()
    thread_2.start()
    

def mensagEnv(client, name):
    msg_init = f"Esta Online: {name}"
    mensagePrepare(client, msg_init)

    while True:
        try:
            mensagem = input('-> ')
            msg_prepare = f"{name}-> {mensagem} \n"                       
            mensagePrepare(client, msg_prepare)
            
        
        except:
            return

# @ RECEBIMENTO DAS MENSAGENS DE USUARIOS
def mensagRecebida(cliente):
    while True:
        try:
            msg = cliente.recv(config['buff']).decode("utf-8")
            print(msg)
        except:
            cliente.close()
            break

# @ PREPARA E ENVIA MENSAGEM PARA SERVIDOR
def mensagePrepare(client:str, msg:str)->None:
    client.send(msg.encode("utf-8"))


# @ NOTIFICAÇÃO PERSONALIZADA
def notification(msg:str)->None:
    tamanho = config['notify']['width']
    flag = config['notify']['flag']

    print(f' {msg} '.center(tamanho,flag))

if __name__ == "__main__":
    main()

