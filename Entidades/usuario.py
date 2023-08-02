import json
class Usuario:
    def __init__(self, id:str, nombre:str, apellido:str, historial_rutas:list):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        if historial_rutas is None:
            self.historial_rutas = []
        else:
            self.historial_rutas = historial_rutas

    def __str__(self):
        return f'''ID: {self.id}
Nombre: {self.nombre}
Apellido: {self.apellido}
Historial de Rutas: {self.historial_rutas}'''

    def a_json(self):
        return {'ID': self.id,
                'Nombre': self.nombre,
                'Apellido': self.apellido,
                'Historial de Rutas':self.historial_rutas
                }
    
    @classmethod
    def from_json(cls, data):
        id = data['ID']
        nombre = data['Nombre']
        apellido = data['Apellido']
        historial_rutas = data['Historial de Rutas']
        return Usuario(id, nombre, apellido, historial_rutas)