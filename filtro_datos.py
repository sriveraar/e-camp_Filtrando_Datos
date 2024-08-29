# Lista de nombres
lista = ['Harry Houdini', 'David Blaine', 'Teller', 'Newton', 'Hawking', 'Einstein', 'Messi', 'Pele', 'Juanes']
magos = ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = ['Messi', 'Pele', 'Juanes']

# Modificación a magos grandicoso
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "EL gran " + magos[i]

# Función para imprimir        
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

# Imprimir todos los nombre de la lista
print("Lista completa de nombres: ")
imprimir_nombres(magos + cientificos + otros)

# Aplicando para hacer grandiosos magos
hacer_grandioso(magos)

print("\nNombre de los magos grandiosos")
imprimir_nombres(magos)

print("\nNombre de los cientificos")
imprimir_nombres(cientificos)

print("\nNombre de los otros")
imprimir_nombres(otros)