from Entidades.ubicacion import Ubicacion
import json
class ABM_Ubicacion:
    def __init__ (self):
        ubiLista = []
        with open("DatosJson/ubicacion.json", "r") as archivo:
            ubicaciones_json = json.load(archivo)
        for data in ubicaciones_json:
            ubiLista.append(Ubicacion.from_json(data))
        self.ubicaciones = ubiLista

    def agregar_ubicacion(self):
        id = len(self.ubicaciones) + 1
        direccion = input('Ingrese la Dirección: ').title()
        coordenadas = []
        coordenadas.append(float(input('Ingrese latitud: ')))
        coordenadas.append(float(input('Ingrese longitud: ')))
        ubicacion = Ubicacion(id, direccion, coordenadas)
        self.ubicaciones.append(ubicacion)
        

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
            direccion = input('Ingrese la Dirección: ').title()
            coordenadas = []
            coordenadas.append(float(input('Ingrese latitud: ')))
            coordenadas.append(float(input('Ingrese longitud: ')))
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
