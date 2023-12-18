import os
def basic(users, user_name):
    users.append(user_name)
    
    if len(users) == 1:
        os.mkdir('USERS')
        os.chdir('./USERS')
        os.mkdir(user_name)
        os.chdir(f'./{user_name}')
        os.mkdir('Documents')
    else:
        os.chdir('../')  
        os.mkdir(user_name)
        os.chdir(f'./{user_name}')
        os.mkdir('Documents')

def crear_carpeta(file_name,user_file_name):
    os.chdir(f'/Users/monfas/Desktop/Ejer6_DWES/USERS/{user_file_name}')
    os.mkdir(file_name)

def subir_archivo(user_file_name,content):
    print(user_file_name)
    os.chdir(f'/Users/monfas/Desktop/Ejer6_DWES/USERS/{user_file_name}/Documents')
            
    with open("file.txt", "wb") as file:
        file.write(content)
