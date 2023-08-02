import json
from datetime import *

class Actividad:
    def __init__(self, id:int, nombre:str, destino_id:int, hora_inicio):
        self.id = id
        self.nombre = nombre
        self.destino = destino_id
        self.inicio = datetime.strptime(hora_inicio, "%Y/%m/%d  %H:%M")
        
    def __str__(self):
        return f'''Nombre': {self.nombre}
                Destino': {self.destino}
                Fecha y hora: {self.inicio}'''
                               
    def a_json(self):
        return {'ID': self.id,
                'Nombre': self.nombre,
                'Destino': self.destino,
                'Fecha y hora': str(self.inicio)
                }
    
    @classmethod   
    def from_json(cls, data):
        id = data['ID']
        nombre = data['Nombre']
        destino_id = data['Destino']
        hora_inicio = data['Fecha y hora']
        return Actividad(id, nombre, destino_id, hora_inicio)

#dt = "28/01/23  08:20:00"

#act = Actividad(1, 'Comidas', [1,2], dt)
#print(act)

#print(datetime(2000,1,1,18,30).strftime('%A %d %B %Y %H:%M'))
#hora=2000,1,1,18,30
#act1= Actividad(1, 'prueba',[1,2], hora)
#act1.a_json()
#print(act1)