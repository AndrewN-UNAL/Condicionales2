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

S = int(S)

#Operaciones

print("seguimos con las operaciones básicas")

#suma

print("Esta es la suma", S+5)

#resta

print("Esta es la resta", S-5)

#multiplicación

print("Esta es la multiplicación", S*5)

#división
S = float(S)
print("Esta es la divisón", S/5)
S = int(S)
#potencia

print("Esta es la potencia", S**5)

#Raiz
S = float(S)
print("Y Esta es la Raiz", S**(1/2))