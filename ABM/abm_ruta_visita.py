from Entidades.rutaVisita import RutaVisita
import json
class ABM_RutaVisita:
    def __init__ (self):
        rutLista = []
        with open("DatosJson/ruta_visita.json", "r") as archivo:
            rutas_json = json.load(archivo)
        for data in rutas_json:
            rutLista.append(RutaVisita.from_json(data))
        self.rutas = rutLista

    def agregar_ruta(self):
        id = len(self.rutas) + 1
        nombre = input('Ingrese el Nombre: ').title()
        destinos = []
        ruta_visita = RutaVisita(id, nombre, destinos)
        self.rutas.append(ruta_visita)
        

    def buscar_ruta(self, id_ruta):
        for ruta_visita in self.rutas:
            if ruta_visita.id == id_ruta:
                return ruta_visita
            else:
                return f'Ruta no encontrada'
        
    
    def eliminar_ruta(self, id_ruta):
        ruta_visita = self.buscar_ruta(id_ruta)
        self.rutas.remove(ruta_visita)

    def modificar_ruta(self, id_ruta):
        ruta_visita = self.buscar_ruta(id_ruta)
        if ruta_visita is not None:
            nombre = input('Ingrese el Nombre: ').title()
            destinos = []
            ruta_visita.nombre = nombre
            ruta_visita.destinos = destinos
        else:
            print('No se encontró la ruta')
    
    def cargar_json(self):
        with open("DatosJson/ruta_visita.json", "w") as archivo:
            lista = []
            for ruta_visita in self.rutas:
                lista.append(ruta_visita.a_json())
            json.dump(lista, archivo, indent =3)
