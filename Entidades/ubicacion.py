class Ubicacion:
    def __init__(self, id:int, direccion:str, coordenadas: list):
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas

    def __str__(self):
        return f'''Dirección: {self.direccion}
        Coordenadas: {self.coordenadas}'''

    def a_json(self):
        return {'ID': self.id,
                'Direccion': self.direccion,
                'Coordenadas': self.coordenadas
                }
    
    @classmethod
    def from_json(cls, data):
        id = data['ID']
        direccion = data['Direccion']
        coordenadas = data['Coordenadas']
        return Ubicacion(id, direccion, coordenadas)
    