#autor: Andrés Felipe Núñez Otálora
#Fecha: 2023-09-01

A = int("4")

print(type(A), "y la variable valor", A)


#Estructuras de control

#Condicional if para "mayor que" y valor verdadero

if(A>1):
    print("este es el valor del If verdadero")
    print(f"A es mayor que 1 y su valor es {A}")
else:
    print("este es el valor del If falso")
    print(f"A es menor que 1 y su valor es {A}")

#Condicional if con "menor que"

if(A<1):
    print("este es el valor del If verdadero")
    print(f"A es menor que 1 y su valor es {A}")
else:
    print("este es el valor del If falso")
    print(f"A es mayor que 1 y su valor es {A}")

#Condicional if con "igual que"

if(A==1):
    print("este es el valor del If verdadero")
    print(f"A es igual que 1 y su valor es {A}")
else:
    print("este es el valor del If falso")
    print(f"A no es igual que 1 y su valor es {A}")

#Condicional if con "desigual que"

if(A!=1):
    print("este es el valor del If verdadero")
    print(f"A no es igual que 1 y su valor es {A}")
else:
    print("este es el valor del If falso")
    print(f"A es igual que 1 y su valor es {A}")

#Condicional if con "igual o mayor que"

if(A>=1):
    print("este es el valor del If verdadero")
    print(f"A es igual o mayor que 1 y su valor es {A}")
else:
    print("este es el valor del If falso")
    print(f"A no es igual o mayor que 1 y su valor es {A}")

#Condicional if con "igual o menor que"

if(A<=1):
    print("este es el valor del If verdadero")
    print(f"A es igual o menor que 1 y su valor es {A}")
else:
    print("este es el valor del If falso")
    print(f"A no es igual o menor que 1 y su valor es {A}")