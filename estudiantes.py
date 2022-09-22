from tkinter import W


estudiantes = {}
opcion = None


def titulo(titulo: str):
    print(f"""########################
#{titulo}#
# """)


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
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "curso": curso
    }
    estudiantes.update({id:estudiante})

def mostrar(id):
    print("########################")
    print(f"#       id: {id}        #")
    print("########################\n")
    print("Nombre:", estudiantes[id]["nombre"])
    print("Apellido:", estudiantes[id]["apellido"])
    print("Teléfono:", estudiantes[id]["telefono"], "\n")
    print("Curso:", estudiantes[id]["curso"])

    print("########################")
    print("////////////////////////")


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
            input("Digite el Nombre\n"),
            input("Digite el Apellido\n"),
            input("Digite el Teléfono\n"),
            int(input("Digite el Curso\n"))
        )
    if opcion == "2":
        titulo("Mostrar Estudiantes")

        sub=None
        while sub!="3":
            print("1. Listar todos.")
            print("2. Buscar por documento.")
            print("3. Volver")
            if sub=="1":
                

        for estudiante in estudiantes:
            mostrar(estudiante)



