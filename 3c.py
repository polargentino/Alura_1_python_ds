'''
4 - Escribe un programa que lea valores promedio de 
precios de un modelo de automóvil durante 3 años 
consecutivos y muestre el valor más alto y más bajo 
entre esos tres años.
'''
# 4 - Comparamos cada valor con los otros dos valores 
# correspondientes a los otros dos años y determinamos 
# el valor más alto y el más bajo. Lo hacemos asignando 
# inicialmente el valor de precio_año1 como el valor 
# máximo y, si encontramos un valor mayor, actualizamos 
# la variable mayor. Utilizamos una lógica similar para 
# encontrar el valor mínimo.

# Recolectamos los precios de los 3 años
precio_año1 = float(input('Ingrese el precio promedio del automóvil en el primer año: '))
precio_año2 = float(input('Ingrese el precio promedio del automóvil en el segundo año: '))
precio_año3 = float(input('Ingrese el precio promedio del automóvil en el tercer año: '))
# Determinamos el valor más alto mediante comparaciones
mayor = precio_año1
if precio_año2 > mayor:
  mayor = precio_año2
if precio_año3 > mayor:
  mayor = precio_año3
# Determinamos el valor más bajo mediante comparaciones
menor = precio_año1
if precio_año2 < menor:
  menor = precio_año2
if precio_año3 < menor:
  menor = precio_año3
# Mostramos los resultados
print(f'El precio más alto fue de R$ {mayor}.')
print(f'El precio más bajo fue de R$ {menor}.')