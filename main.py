#Jason Misael Gutierrez de Leon 1624622
#Abel Alexander de Leon Lima 1572322
#Miguel Alfonso Macario Velasquez 1597421


def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read().lower()
        palabras = contenido.split()
        return palabras
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}.")
        return []


def generar_tabla(lista1, lista2):
    coincidencias = {}

    for palabra in lista1:
        if palabra in lista2:
            if palabra not in coincidencias:
                coincidencias[palabra] = [1, 2]

    return coincidencias


def escribir_tabla(archivo_salida, coincidencias):
    with open(archivo_salida, 'w', encoding='utf-8') as archivo:
        for palabra, lista in coincidencias.items():
            archivo.write(f"La palabra {palabra}  Aparece en ambas listas")


def mostrar_menu():
    print("____Menú de opciones____")
    print("1. Mostrar todas las coincidencias")
    print("2. Buscar una palabra en particular")
    print("3. Salir")

def main():
    lista1 = leer_archivo('archivo1.txt')
    lista2 = leer_archivo('archivo2.txt')

    coincidencias = generar_tabla(lista1, lista2)
    escribir_tabla('tabla_indice.txt', coincidencias)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            print("Coincidencias encontradas")
            for palabra, listas in coincidencias.items():
                print(f"La palabra {palabra}  Aparece en ambas listas")

        elif opcion == '2':
            palabra_buscada = input("Introduce la palabra que deseas buscar: ").lower()
            if palabra_buscada in coincidencias:
                print(f"La palabra '{palabra_buscada}' aparece en las listas: {coincidencias[palabra_buscada]}")
            else:
                if palabra_buscada in lista1:
                    print(f"La palabra '{palabra_buscada}' aparece en la lista 1")
                elif palabra_buscada in lista2:
                    print(f"La palabra '{palabra_buscada}' aparece en la lista 2")
                else:
                    print(f"La palabra '{palabra_buscada}' no se encontró en ningua listas.")


        elif opcion == '3':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor elige nuevamente.")

if __name__ == "__main__":
    main()
