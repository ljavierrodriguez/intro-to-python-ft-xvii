from libs import sumar, restar, PI

print(PI)

print(sumar(10, 10))

import random

print(random.randint(10, 20))

import datetime

import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()

#print(users)

nombres = [user["name"] for user in users]
print(nombres)

import os
from pathlib import Path

BASE = os.path.join(Path(__file__).resolve().parent, 'docs')
print(BASE)

#name = input("Ingrese nombre: ")
#print(name)

import json

persona = "{\"name\": \"Luis\",\"lastname\": \"Rodriguez\"}"

#print(persona["name"])

dict_persona = json.loads(persona) # convertir en un diccionario

print(dict_persona["name"])

name = 'Luis "Hittler" Rodriguez'

print(name)

persona = {
    "name": "Jimena",
    "lastname": "Matthies"
}
# {"name": "Jimena", "lastname": "Matthies"}


string_persona = json.dumps(persona)
print(string_persona)
print(string_persona[0])
print(string_persona[10:16])
print(string_persona[:-5])


a = int(input("Ingrese Numero 1"))

b = int(input("Ingrese Numero 2"))

print(a+b)

