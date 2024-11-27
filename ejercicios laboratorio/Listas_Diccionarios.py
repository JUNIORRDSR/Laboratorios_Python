# Crear una lista de elementos y mostrar cada uno utilizando un bucle
estudiantes = ["Ana", "Luis", "Carlos", "Marta"]
for estudiante in estudiantes:
    print(estudiante)

# Crear un diccionario simple que almacene información de contacto y mostrar sus claves y valores
contactos = {
    "Ana": "ana@example.com",
    "Luis": "luis@example.com"
}
for nombre, correo in contactos.items():
    print(f"Nombre: {nombre}, Correo: {correo}")

# Agregar elementos a una lista o actualizar valores en un diccionario
estudiantes.append("Pedro")
print(estudiantes)
contactos["Marta"] = "marta@example.com"
print(contactos)
