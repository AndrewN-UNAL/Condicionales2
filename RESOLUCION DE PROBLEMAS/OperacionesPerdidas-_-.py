#autor: Andrés Felipe Núñez Otálora
#Fecha: 2023-09-01

#Operaciones simples y print

print("hola, ya puedo imprimir frases")

S = 6

#concersiones entre int, float y str

print("te doy un entero",type(S), int(S))

S = float(S)

print("ahora es un decimal",type(S), S)

S = str(S)

print("y ahora es un texto",type(S), S)

#Operaciones
A = 6
print("seguimos con las operaciones básicas")

#suma

print("Esta es la suma", A+5)

#resta

print("Esta es la resta", A-5)

#multiplicación

print("Esta es la multiplicación", A*5)

#división
A = float(A)
print("Esta es la divisón", A/5)
A = int(A)
#potencia

print("Esta es la potencia", A**5)

#Raiz
A = float(A)
print("Y Esta es la Raiz", A**(1/2))