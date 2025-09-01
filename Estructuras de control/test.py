#autor: Andrés Felipe Núñez Otálora
#Fecha: 2023-09-01

A = int("4")

print(type(A), "y la variable valor", A)


#Estructuras de control

#if verdadero
if(A>5):
    print("este es el valor del If verdadero")
    print(f"A es mayor que 5 y su valor es {A}")
else:
    print("La condicion es falsa")

#Lista de condiciones
if(A<5):
    print(f"A es menor que 5 y su valor es {A}")

if(A==5):
    print(f"A es igual que 5 y su valor es {A}")

if(A>=5):
    print(f"A es mayor o igual que 5 y su valor es {A}")

if(A<=5):
    print(f"A es menor o igual que 5 y su valor es {A}")