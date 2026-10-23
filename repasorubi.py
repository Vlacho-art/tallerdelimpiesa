# Estructura de tipo de datos
# Listas

# Lista1= [1, 2, 3, 4, 5]
# ListaNombres= ["Juan", "Pedro", "Maria", "Ana"]
# ListaMixta= [2, "Juan", 4.5, False]
# print(Lista1)
# print(ListaNombres)
# print(ListaMixta)
# name= input("Ingrese su nombre: ")
# number= int(input("Ingrese un numero: "))

# Operaciones con listas
# A= [1, 2, 3]
# B= [4, 5, 6]
# C= A + B
# resta= A - B
# resta = [a - b for a, b in zip(A, B)]
# print(f"Lista: {A}, Lista B: {B}, Resta: {resta}")

# ListaEdades= [10, 15, 20, 25, 18]
# for edad in ListaEdades:
#     if edad >= 18:
#         print(f"{edad} es mayor de edad")
#     else:
#         print(f"{edad} es menor de edad")

Lista3= [1, 2, 3, 4, 5]
for q in Lista3:
    if q % 2 == 0:
        print(f"{q} es par")
    else:
        print(f"{q} es impar")