'''

if condition:
    sentences

if condition:
    sentences
else: 
    sentences

if condition:
    sentences
elif condition:
    sentences
else: 
    sentences

&& => and
|| => or
! => not

'''
a = 5
b = 10
c = 6

if a == b:
    print(a==b)


if a > b:
    print("Verdadero")
else:
    print("Falso")


if a > b and a > c:
    print("A es mayor")
elif b > c:
    print("B es mayor")
else:
    print("C es mayor")
