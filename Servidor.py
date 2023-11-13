import socket
import threading
import random
import time

# Lógica principal de um servidor usando a biblioteca socket em Python.
def main():
    # Cria um novo objeto de socket, especificando o o endereço e a comunicação(TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Associa o socket a um endereço IP e porta
    server.bind(('0.0.0.0', 8888))
    # Coloca o socket em modo de escuta, permitindo que ele aceite conexões de entrada. 
    server.listen(5)
    print("[*] Servidor ouvindo na porta 8888")

     # LOOP para aceitar continuamente conexões de clientes
    while True:
        client, addr = server.accept()
        print(f"[*] Conexão aceita de {addr[0]}:{addr[1]}")

        # A função handle_client será executada em paralelo com o loop principal, permitindo
        # que o servidor atenda a múltiplos clientes simultaneamente.
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

# se o script estiver sendo executado como o programa principal, a função (main()) é chamada
if __name__ == "__main__":
    main()


# A função representa a conexão com um cliente específico que opera em um loop infinito.
def handle_client(client_socket):
    while True:
        # O servidor tenta receber dados do cliente; configurado para receber até 1024 bytes de dados em cada chamada.
        request = client_socket.recv(1024)
        if not request:
            break        
        #Se dados foram recebidos, o servidor cria uma resposta usando esses dados. 
        response = f"\nServidor responde: {request.decode('utf-8')}\n"
        
        # Simula um atraso aleatório na resposta
        delay = random.uniform(0.1, 1.0)
        time.sleep(delay)
        client_socket.send(response.encode('utf-8'))
    client_socket.close()


