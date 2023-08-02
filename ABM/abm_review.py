from Entidades.review import Review
import json
class ABM_Review:
    def __init__ (self):
        revLista = []
        with open("DatosJson/review.json", "r") as archivo:
            reviews_json = json.load(archivo)
        for data in reviews_json:
            revLista.append(Review.from_json(data))
        self.reviews = revLista

    def agregar_review(self):
        id = len(self.reviews) + 1
        id_destino = int(input('Ingrese el ID del destino: '))
        id_usuario = int(input('Ingrese el ID del usuario: '))
        while True:
            calificacion = input('Ingrese la Calificación: ')
            if calificacion > 0 and calificacion < 6:
                break
            else:
                print('La calificación debe ser entre 1 y 5')
        comentario = input('Ingrese comentario: ').capitalize()
        animo = input
        coordenadas = []
        coordenadas.append(float(input('Ingrese latitud: ')))
        coordenadas.append(float(input('Ingrese longitud: ')))
        review = Review(id, nombre, direccion, coordenadas)
        self.reviews.append(review)
        

    def buscar_ubicacion(self, id_ubicacion):
        for ubicacion in self.ubicaciones:
            if ubicacion.id == id_ubicacion:
                return ubicacion
        return f'Ubicación no encontrada'
    
    def eliminar_ubicacion(self, id_ubicacion):
        ubicacion = self.buscar_ubicacion(id_ubicacion)
        self.ubicaciones.remove(ubicacion)

    def modificar_ubicacion(self, id_ubicacion):
        ubicacion = self.buscar_ubicacion(id_ubicacion)
        if ubicacion is not None:
            nombre = input('Ingrese el Nombre: ').title()
            direccion = input('Ingrese la Dirección: ').title()
            coordenadas = []
            coordenadas.append(float(input('Ingrese latitud: ')))
            coordenadas.append(float(input('Ingrese longitud: ')))
            ubicacion.nombre = nombre
            ubicacion.direccion = direccion
            ubicacion.coordendas = coordenadas
        else:
            print('No se encontró la ubicación')
    
    def cargar_json(self):
        with open("DatosJson/ubicacion.json", "w") as archivo:
            lista = []
            for ubicacion in self.ubicaciones:
                lista.append(ubicacion.a_json())
            json.dump(lista, archivo, indent =3)
