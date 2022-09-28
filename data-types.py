""" 

String
Number (int, float, decimal)
Boolean
None

Dictionaries

Array
    Listas
    Tuples
    Sets

"""

# Comentario Simple

nombre = "Luis"
apellido = 'Rodriguez'
direccion = '''

Esto es un texto largo

'''

edad = 40
ingreso = 10.6
degree = -10

flag = True # False  

nota = None

resultado = None

# Array
# Listas
notas = [1, 2, 3]
notas = list(1, 2, 3)

# tuples
status = ('active', 'inactive', 'canceled', 'suspended')
status = tuple('active', 'inactive', 'canceled', 'suspended')

# Sets
frutas = { "manzana", "Pera", "Uvas", "Bananas" }
frutas = set("manzana", "Pera", "Uvas", "Bananas")


# Dictionaries
persona = {
    "nombre": "Luis",
    "apellido": "Rodriguez",
    "saludo": lambda : print("Hola Mundo"),
    "obj": {
        "a": "",
        "b": ""
    }
}

persona = dict()
persona["nombre"] = ""

persona["nombre"]
