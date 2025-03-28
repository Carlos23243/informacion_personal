# Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}
# ciudad
informacion_personal["ciudad"] = "Quito"
# profecion
informacion_personal["profesion"] = "Desarrollador de Software"
# telefono
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"
# edad
del informacion_personal["edad"]
# impresion
print(informacion_personal)



