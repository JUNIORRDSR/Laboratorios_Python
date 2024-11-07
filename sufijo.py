palabra = input('Ingrese una palabra: ')
sufijo = input('Ingrese el sufijo: ')
num_pal_sufijo = len(sufijo)
respuesta = ''
for i in range(num_pal_sufijo):
    respuesta += palabra[-num_pal_sufijo+i]
if (respuesta == sufijo):
    print(f'{sufijo} si es sufijo de {palabra}')
else:
    print(f'{sufijo} no es sufijo de {palabra}')