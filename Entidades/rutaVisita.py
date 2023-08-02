import json
class RutaVisita:
    def __init__(self, id:int, nombre:str, destinos = None):
        self.id = id
        self.nombre = nombre
        if destinos is None:
            self.destinos = []
        else:
            self.destinos = destinos

    def __str__(self):
        return f'''Nombre: {self.nombre}
Destinos: {self.destinos}'''

    def a_json(self):
        return {'ID': self.id,
                'Nombre': self.nombre,
                'Destinos': self.destinos
                }
    
    @classmethod
    def from_json(cls, data):
        id = data['ID']
        nombre = data['Nombre']
        destinos = data['Destinos']
        return RutaVisita(id, nombre, destinos)
