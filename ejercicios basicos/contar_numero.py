numero = input('ingrese un numero de 1 a 3 digitos: ')
if ( len(numero)>0 and len(numero)<3 ):
    print(f'El numero tiene {len(numero)} caracteres')
else:
    print('el numero no cumple con las condiciones')