import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

nome = input("Digite seu nome: ")

def receber():
    while True:
        try:
            mensagem = cliente.recv(1024).decode()
            print("\n" + mensagem)
        except:
            print("Erro ao receber mensagem do servidor.")
            cliente.close()
            break

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

cliente.send(nome.encode())

thread = threading.Thread(target=receber)
thread.start()

while True:
    msg = input()
    mensagem_completa = f"{nome}: {msg}"  # Incluir o nome na mensagem
    cliente.send(mensagem_completa.encode())
