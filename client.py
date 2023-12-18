import socket
import pymysql
from encriptar import encriptar_contrasena 


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = '127.0.0.1'
server_port = 12345

client_socket.connect((server_host, server_port))
welcome_msg = client_socket.recv(1024).decode()
print(welcome_msg)
while True:
    command = input("\n1 -> agregar_usuario\n2 -> crear_carpeta\n3 -> subir_archivo\n4 -> borrar_archivo\n5 -> exit\nIngrese un comando : ")
    client_socket.send(command.encode())

    if command == 'exit':
        print('\n<--- Saliendo de la sesison --->')
        client_socket.close()
        break
    
    elif command == 'agregar_usuario':
        
        user_name = input('¿Cual es tu nombre de usuario? ')
        user_email = input('¿Cual es tu correo electrónico? ')
        user_pass = input('¿Cual es tu contraseña? ')
        user_msg = input('¿Cual es tu mensaje? ')
        
        user_pass = encriptar_contrasena(user_pass)
        
        user_data = f"{user_name}|{user_email}|{user_pass}|{user_msg}"
        client_socket.send(user_data.encode())
        
        response = client_socket.recv(1024).decode()
        print(response)
    
    elif command == 'crear_carpeta':
        user_file_name = input('Agrega tu nombre de usuario: ')
        client_socket.send(user_file_name.encode())
        new_file = input('Agregar el nombre de la carpeta: ')
        client_socket.send(new_file.encode())
        
        
        msg_si = client_socket.recv(1024).decode()
        print(msg_si)
       
        msg_no = client_socket.recv(1024).decode()
        print(msg_no)

    elif command == 'subir_archivo':
        user_file_name = input('Agrega tu nombre de usuario: ')
        client_socket.send(user_file_name.encode())
        file_name = "file.txt"
        with open(file_name, "rb") as file:
            content = file.read(1024)
            client_socket.send(content)
        print("Archivo enviado con éxito.")
    
    elif command == 'borrar_archivo':
        file_name = input('Ingresa el nombre del archivo que quieres borrar :')
        client_socket.send(file_name.encode())

        response = client_socket.recv(1024).decode()
        print(response)

    