
lista = []
pares = []
impares = []



for numero in range(20):
    coisa = int(input("digite o numero:"))
    lista.append(coisa)

for numero in lista:
   
    if numero %2 == 0:
        pares.append(numero)

    else:
        impares.append(numero)

print(f"\n   numero digitados: {lista}")
print(f"\n numeros pares: {pares} ")
print(f"numeros impares: {impares}")
