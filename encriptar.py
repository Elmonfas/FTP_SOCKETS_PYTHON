def encriptar_contrasena(contrasena):
    contrasena_encriptada = ""
    
    for letra in contrasena:
        if letra.isalpha():
            if letra.islower():
                contrasena_encriptada += chr(((ord(letra) - ord('a') + 1) % 20) + ord('a'))
            elif letra.isupper():
                contrasena_encriptada += chr(((ord(letra) - ord('A') + 1) % 20) + ord('A'))
        else:
            contrasena_encriptada += letra
    
    return contrasena_encriptada

# contrasena = input("Ingresa tu contraseña: ")


# contrasena_encriptada = encriptar_contrasena(contrasena)

# print("Contraseña encriptada:", contrasena_encriptada)

def desencriptar_contrasena(encriptada):
    contrasena_desencriptada = ""
    
    for letra in encriptada:
        if letra.isalpha():
            if letra.islower():
                contrasena_desencriptada += chr(((ord(letra) - ord('a') - 1) % 20) + ord('a'))
            elif letra.isupper():
                contrasena_desencriptada += chr(((ord(letra) - ord('A') - 1) % 20) + ord('A'))
        else:
            contrasena_desencriptada += letra
    
    return contrasena_desencriptada
# contrasena_encriptada = input("Ingresa la contraseña encriptada: ")


# contrasena_desencriptada = desencriptar_contrasena(contrasena_encriptada)

# print("Contraseña desencriptada:", contrasena_desencriptada)