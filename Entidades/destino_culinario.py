import json
class DestinoCulinario:
    def __init__(self, id:int, nombre:str, tipo_cocina:str, ingredientes:list, precio_minimo:float, precio_maximo:float, popularidad:float, disponibilidad:bool, id_ubicacion:int, imagen:str):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

    def __str__(self):
        return f'''Nombre: {self.nombre}
                Tipo de Cocina: {self.tipo_cocina}
                Ingredientes: {self.ingredientes}
                Precio Mínimo: {self.precio_minimo}
                Precio Máximo: {self.precio_maximo}
                Popularidad: {self.popularidad}
                Disponibilidad: {self.disponibilidad}
                Ubicación: {self.id_ubicacion}
                Imagen: {self.imagen}'''

    def a_json(self):
        return {'ID': self.id,
                'Nombre': self.nombre,
                'Tipo de Cocina': self.tipo_cocina,
                'Ingredientes': self.ingredientes,
                'Precio Minimo': self.precio_minimo,
                'Precio Maximo': self.precio_maximo,
                'Popularidad': self.popularidad,
                'Disponibilidad': self.disponibilidad,
                'Ubicacion': self.id_ubicacion,
                'Imagen': self.imagen}
    
    @classmethod   
    def from_json(cls, data):
        id = data['ID']
        nombre = data['Nombre']
        tipo_cocina = data['Tipo de Cocina']
        ingredientes = data['Ingredientes']
        precio_minimo = data['Precio Minimo']
        precio_maximo = data['Precio Maximo']
        popularidad = data['Popularidad']
        disponibilidad = data['Disponibilidad']
        id_ubicacion = data['Ubicacion']
        imagen = data['Imagen']
        return DestinoCulinario(id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen)
    