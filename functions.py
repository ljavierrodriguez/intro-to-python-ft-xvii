""" 

def nombre_funcion():
    sentences


nombre_funcion = lambda a, b: a + b


"""

def suma(a, b = 5):
    return a + b


suma = lambda a, b: a + b


suma(10, 10)

notas = [1, 2, 3, 4, 5]

resultado = list(map(lambda x: x * x, notas))

print(resultado)

resultado = notas.copy()
resultado.sort(reverse=True)
print(resultado)