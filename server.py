import socket
import os
import logging
from sql import agregar_usuario
from import_achivos import basic, crear_carpeta, subir_archivo

logging.basicConfig(filename="historial.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

users = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = '127.0.0.1'
server_port = 12345

server_socket.bind((server_host, server_port))
server_socket.listen(10)

print(f"Servidor escuchando en {server_host}:{server_port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexión entrante desde {addr}")
    welcome_msg = '''
    
    BIENVENIDO USUARIO!
    '''
    client_socket.send(welcome_msg.encode())

    while True:
        command = client_socket.recv(1024).decode()

        if command == 'exit':
            log_message = f'Los usuarios cerraron la sesión'
            server_socket.close()
            break

        elif command == 'agregar_usuario':
            user_data = client_socket.recv(1024).decode()
            user_name, user_email, user_pass, user_msg = user_data.split('|')
            agregar_usuario(user_name, user_email, user_pass, user_msg)
            basic(users, user_name)

            response = '\nUsuario agregado con éxito.'
            client_socket.send(response.encode())

            log_message = f"Se ha agregado un usuario: {user_name}, Correo electrónico: {user_email}"
            logging.info(log_message)

        elif command == 'crear_carpeta':
            user_file_name = client_socket.recv(1024).decode()
            new_file = client_socket.recv(1024).decode()
            
            if user_file_name in users:
                crear_carpeta(new_file,user_file_name)
                msg_si = f'\nCreando carpeta {new_file} en el usuario {user_file_name}'
                client_socket.send(msg_si.encode())
                

                log_message = f"Se ha creado una carpeta {new_file} para el usuario {user_file_name}"
                logging.info(log_message)
            else:
                msg_no = f'\nEl usuario {user_file_name} no existe, por favor cree el usuario primero.'
                client_socket.send(msg_no.encode())

        elif command == 'subir_archivo':
            user_file_name = client_socket.recv(1024).decode()
            content = client_socket.recv(1024)
            subir_archivo(user_file_name,content)

            log_message = f'El usuario {user_file_name} ha subido un archivo'
            logging.info(log_message)

        elif command == 'borrar_archivo':
            file_name = client_socket.recv(1024).decode()
            os.remove(file_name)
            
            log_message = f'El usuario {user_file_name} ha borrado el archivo {file_name}'
            logging.info(log_message)
            
            response = '\nArchivo borrado con éxito.'
            client_socket.send(response.encode())
