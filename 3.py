'''
Estructuras condicinales:
------------------------
Vamos practicar el uso de estructuras condicionales como 
el if, else y elif a través de algunas actividades. 
Ahora que estamos avanzando en los contenidos, podemos 
hacer los desafíos más interesantes: ¡trabajaremos en 
proyectos de código! Resuelve los problemas iniciales 
para prepararte para los proyectos:

Entrenando la programación

1 - Escribe un programa que pida a la persona usuaria que 
proporcione dos números y muestre el número más grande.
'''
#1 -

# Recolectamos los números
num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
# Comparamos ambos números y determinamos cuál es el mayor
if num1 > num2:
    print(f'El primer número es mayor: {num1}')
elif num2 > num1:
    print(f'El segundo número es mayor: {num2}')
else: # En caso de que los números sean iguales
    print('Ambos números son iguales.')
