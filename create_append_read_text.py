import os

def read():
    with open("./prueba.txt", "r", encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)


def append(text):
    with open("./prueba.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

def write(text):
    with open("./prueba.txt", "w", encoding="utf-8") as f:
        f.write(text)

def run():
    os.system("cls")
    conditional = True
    while conditional:
        try:
            print("""  
----------------------------------------------------------------------
            Seleccione un numero:
            1. Crear un texto
            2. Agregar un texto
            3. Leer documento
            4. Salir del programa
----------------------------------------------------------------------
            """)
            selection = int(input())
            match selection:
                case 1:
                    os.system("cls")
                    texto = input("""
__________________________________
Escriba el texto que desea agregar:
__________________________________
""")
                    write(texto)
                    print("Tu texto ha sido agregado")
                    break
                case 2:
                    os.system("cls")
                    print("""
_____________________________________________________
Este es el texto que ya se encuentra en su documento:
_____________________________________________________
""")
                    read()
                    texto = input("""
__________________________________________________
Escriba el texto que desea agregar a continuación:
__________________________________________________
""")
                    append(texto)
                    print("Tu texto ha sido agregado")
                    break
                case 3:
                    os.system("cls")
                    print("""
_________________________
Su texto es el siguiente:
_________________________
""")
                    read()
                    break
                case 4:
                    conditional = False
                    print(""""
                    
---Programa terminado---""")
        except ValueError:
            print("Error seleccione una opcion correcta")

if __name__ == "__main__":
    run()