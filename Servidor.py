import socket
import threading
import random
import time

def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024)
        if not request:
            break
        response = f"\nServidor responde: {request.decode('utf-8')}\n"
        
        # Simula um atraso aleatório na resposta
        delay = random.uniform(0.1, 1.0)
        time.sleep(delay)
        client_socket.send(response.encode('utf-8'))
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8888))
    server.listen(5)

    print("[*] Servidor ouvindo na porta 8888")

    while True:
        client, addr = server.accept()
        print(f"[*] Conexão aceita de {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    main()

