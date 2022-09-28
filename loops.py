""" 

for valor in datos:
    sentences

while condition:
    sentences


"""

for i in range(1, 11): # start=0, step=1 
    print("Hola " + str(i))

nombres = ["Hugo", "Paco", "Luis"]

for nombre in nombres:
    print(nombre)

for i in range(len(nombres)):
    print(nombres[i])

i = 0
while i < len(nombres):
    print(nombres[i])
    i+=1


users = [
    {"id": 1, "name": "Hugo"},
    {"id": 2, "name": "Paco"},
    {"id": 3, "name": "Luis"},
]

resultado = [ user["id"] for user in users ]
print(resultado)