import json
class Review:
    def __init__(self, id:int, id_destino:int, id_usuario:int, calificacion:int, comentario:str, animo:str):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def __str__(self):
        return f'''Destino: {self.id_destino}
Ususario: {self.id_usuario}
Calificación: {self.calificacion}
Comentario: {self.comentario}
Estado de ánimo: {self.animo}'''
    
    def a_json(self):
        return {'ID': self.id,
                'Destino': self.id_destino,
                'Ususario': self.id_usuario,
                'Calificación': self.calificacion,
                'Comentario': self.comentario,
                'Estado de ánimo': self.animo}
    
    @classmethod
    def from_json(cls, data):
        id = data['id']
        id_destino = data['Destino']
        id_usuario = data['Ususario']
        calificacion = data['Calificación']
        comentario = data['Comentario']
        animo = data['Estado de ánimo']
        return Review(id, id_destino, id_usuario, calificacion, comentario, animo)