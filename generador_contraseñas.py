import hashlib

if __name__ == "__main__":
    # cifrado de la clave utilizando md5
    clave = '25978634'
    result = hashlib.md5(bytes(clave, encoding='utf-8'))
    # muestra la clave cifrada en hexadecimal, esta es la que se debe guardar en base de datos
    print(result.hexdigest())