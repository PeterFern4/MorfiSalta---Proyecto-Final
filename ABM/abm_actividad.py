from Entidades.actividades import Actividad
import json
from datetime import *
class ABM_Actividad:
    def __init__ (self):
        actLista = []
        with open("DatosJson/actividades.json", "r") as archivo:
            actividades_json = json.load(archivo)
        for data in actividades_json:
            actLista.append(Actividad.from_json(data))
        self.actividades = actLista

    def agregar_actividad(self):
        id = len(self.actividades) + 1
        nombre = input('Ingrese actividad: ').title()
        destinos = []
        #hora_inicio = input('Ingrese fecha y hora: ')
        año = input('Año: ')
        mes = input('Mes: ')
        dia = input('Día: ')
        hora = input('Horas: ')
        minutos = input('Minutos: ')
        hora_inicio = año+"/"+mes+"/"+dia+"  "+hora+":"+minutos
        actividad = Actividad(id, nombre, destinos, hora_inicio)
        self.actividades.append(actividad)
        

    def buscar_actividad(self, id_actividad):
        for actividad in self.actividades:
            if actividad.id == id_actividad:
                return actividad
        return f'Actividad no encontrada'
    
    def eliminar_actividad(self, id_actividad):
        actividades = self.buscar_actividad(id_actividad)
        self.actividades.remove(actividades)

    def modificar_actividad(self, id_actividad):
        actividad = self.buscar_actividad(id_actividad)
        if actividad is not None:
            nombre = input('Ingrese actividad: ').title()
            destinos = []
            #hora_inicio = input('Ingrese fecha y hora: ')
            año = input('Año: ')
            mes = input('Mes: ')
            dia = input('Día: ')
            hora = input('Horas: ')
            minutos = input('Minutos: ')
            hora_inicio = año+"/"+mes+"/"+dia+"  "+hora+":"+minutos
            actividad.nombre = nombre
            actividad.destinos = destinos
            actividad.hora_inicio = (datetime.strptime(hora_inicio, "%d/%m/%Y  %H:%M"))
        else:
            print('No se encontró la actividad')
    
    def cargar_json(self):
        with open("DatosJson/actividades.json", "w") as archivo:
            lista = []
            for actividad in self.actividades:
                lista.append(actividad.a_json())
            json.dump(lista, archivo, indent =3)
