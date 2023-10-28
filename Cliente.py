import socket
import threading
import time

def send_message(client_socket):
    while True:
        message = input("Cliente pergunta: ")
        client_socket.send(message.encode('utf-8'))
        time.sleep(2)

def receive_response(client_socket):
    while True:
        response = client_socket.recv(1024)
        print(response.decode('utf-8'))

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))

    send_thread = threading.Thread(target=send_message, args=(client,))
    receive_thread = threading.Thread(target=receive_response, args=(client,))

    send_thread.start()
    receive_thread.start()

if __name__ == "__main__":
    main()
