import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

clientes = []

def broadcast(mensagem, cliente):
    for c in clientes:
        if c != cliente:
            try:
                c.send(mensagem)
            except:
                c.close()
                clientes.remove(c)

def lidar_com_cliente(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            print(f"Mensagem recebida: {mensagem.decode()}")
            broadcast(mensagem, cliente)
        except:
            if cliente in clientes:
                clientes.remove(cliente)
            cliente.close()
            break

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print(f"Servidor ouvindo em {HOST}:{PORT}")

while True:
    cliente, endereco = servidor.accept()
    print(f"Conectado a {endereco}")
    clientes.append(cliente)
    thread = threading.Thread(target=lidar_com_cliente, args=(cliente,))
    thread.start()
