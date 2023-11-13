import socket
import threading
import time

# Função para configurar o cliente
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))

    send_thread = threading.Thread(target=send_message, args=(client,))
    receive_thread = threading.Thread(target=receive_response, args=(client,))

    send_thread.start()
    receive_thread.start()

if __name__ == "__main__":
    main()

# função para enviar mensagens de um cliente para um servidor usando um socket em Python.
def send_message(client_socket):
    while True:
        message = input("Cliente pergunta: ")
        client_socket.send(message.encode('utf-8'))
        #Após enviar a mensagem, há uma pausa de 2 segundos antes de repetir o loop
        time.sleep(2)

# função receber e imprimir respostas do servidor em um cliente 
def receive_response(client_socket):
    while True:
        response = client_socket.recv(1024)
        print(response.decode('utf-8'))
