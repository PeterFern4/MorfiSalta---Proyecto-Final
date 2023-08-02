from Entidades.usuario import Usuario
import json
class ABM_Usuario:
    def __init__ (self):
        usuLista = []
        with open("DatosJson/usuarios.json", "r") as archivo:
            usuarios_json = json.load(archivo)
        for data in usuarios_json:
            usuLista.append(Usuario.from_json(data))
        self.usuarios = usuLista

    def agregar_usuario(self):
        id = int(input('Ingrese DNI: '))
        nombre = input('Ingrese el Nombre: ').title()
        apellido = input('Ingrese el Apellido: ').title()
        historial_rutas = []
        usuario = Usuario(id, nombre, apellido, historial_rutas)
        self.usuarios.append(usuario)
        

    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        return f'Usuario no encontrado'
    
    def eliminar_usuario(self, id_usuario):
        usuario = self.buscar_usuario(id_usuario)
        self.usuarios.remove(usuario)

    def modificar_usuario(self, id_usuario):
        usuario = self.buscar_usuario(id_usuario)
        if usuario is not None:
            id = int(input('Ingrese DNI: '))
            nombre = input('Ingrese el Nombre: ').title()
            apellido = input('Ingrese el Apellido: ').title()
            historial_rutas = []
            usuario.id = id
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.historial_rutas = historial_rutas
        else:
            print('No se encontró el usuario')
    
    def cargar_json(self):
        with open("DatosJson/usuarios.json", "w") as archivo:
            lista = []
            for usuario in self.usuarios:
                lista.append(usuario.a_json())
            json.dump(lista, archivo, indent =3)
