from tkinter import W


estudiantes = {"123": {"Nombre": "Antony",
                       "Apellido": "Botello", "Telefono": "3135279210", "Curso": 5}}
opcion = None


def titulo(titulo: str):
    print(f"""########################
#{titulo}#
######################## """)


def agregar(id: str, nombre: str, apellido: str, telefono: str,  curso: int):
    """Función para agregar estudiantes
    Args:
        id (str): _description_
        nombre (str): _description_
        apellido (str): _description_
        telefono (str): _description_
        curso (int): _description_
    """
    estudiante = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Telefono": telefono,
        "Curso": curso
    }
    estudiantes.update({id: estudiante})


def mostrar(id):
    titulo(f"Estudiante {id}")
    print("Nombre:", estudiantes[id]["Nombre"])
    print("Apellido:", estudiantes[id]["Apellido"])
    print("Teléfono:", estudiantes[id]["Telefono"])
    print("Curso:", estudiantes[id]["Curso"], "\n")

    print("########################")
    print("////////////////////////")


def actualizar(id, campo, info):
    if campo in estudiantes[id]:
        estudiantes[id][campo] = info
    else:
        print("El campo no existe.")

def eliminar(id):
    seguro=input("Esta seguro de eliminar (Y/N)\n")
    if seguro == "Y" or seguro == "y":
        aux= estudiantes.pop(id)
        nombre= aux["Nombre"]
        print(f"El estudiante {nombre} se eliminó correctamente.")
    else:
        print(f"Eliminación cancelada.")


while opcion != "5":

    titulo("Menú Estudiantes")
    print("1. Ingresar nuevo Estudiante.")
    print("2. Consultar estudiantes registrados.")
    print("3. Editar estudiantes registrados.")
    print("4. Eliminar un Estudiante.")
    print("5. Salir")

    opcion = input("Digite la opción:\n")

    if opcion == "1":
        titulo("Agregar Estudiantes")

        agregar(
            input("Digite el documento\n"),
            input("Digite el Nombre\n").capitalize,
            input("Digite el Apellido\n").capitalize,
            input("Digite el Teléfono\n"),
            int(input("Digite el Curso\n"))
        )
    if opcion == "2":
        titulo("Mostrar Estudiantes")

        sub = None
        while sub != "3":
            print("1. Listar todos.")
            print("2. Buscar por documento.")
            print("3. Volver")
            sub = input("Digite la opción:\n")
            if sub == "1":
                for estudiante in estudiantes:
                    mostrar(estudiante)
            elif sub == "2":
                mostrar(input("Digite el documento\n"))
    if opcion == "3":
        titulo("Actualizar Estudiantes")
        actualizar(input("Digite el estudiante.\n"),
                   input("Digite el nombre del campo.\n").capitalize,
                   input("Digite la actualización.\n").capitalize)
    if opcion == "4":
        titulo("Eliminar Estudiantes")
        eliminar(input("Digite el estudiante.\n"))
else:
    print("Hasta la proxima!")