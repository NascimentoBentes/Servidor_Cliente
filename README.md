# Servidor_Cliente
Um servidor que será responsável por escutar as mensagens dos clientes em uma determinada porta e devolver uma resposta para esse cliente.

TEM:

- Um delay aleatório no servidor para simular o atraso na resposta das mensagens.
	* Sockets
	* Arquitetura cliente/servidor
	* Cliente com duas threads, uma thread para enviar a mensagem com a intenção de liberar o terminal para que outra mensagem possa ser enviada em seguida;
	utra thread para receber a resposta do servidor e imprimir na tela a resposta.
	* Comunicação via TCP
