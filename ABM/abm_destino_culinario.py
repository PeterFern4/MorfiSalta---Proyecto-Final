from Entidades.destino_culinario import DestinoCulinario
import json
class ABM_DestinoCulinario:
    def __init__ (self):
        descuLista = []
        with open("DatosJson/destinos_culinarios.json", "r") as archivo:
            destino_culinario_json = json.load(archivo)
        for data in destino_culinario_json:
            descuLista.append(DestinoCulinario.from_json(data))
        self.destinos_culinarios = descuLista

    def agregar_destino_culinario(self):
        id = len(self.destinos_culinarios) + 1
        nombre = input('Ingrese el nombre: ').title()
        tipo_cocina = input('Ingrese el tipo de cocina: ').title()
        ingredientes = []
        while True:
            ingrediente = input('Ingrese ingrediente: ').title()
            if ingrediente == "" or ingrediente == " ":
                break
            else:
                ingredientes.append(ingrediente)
        precio_minimo = float(input('Ingrese el precio mínimo: $'))
        precio_maximo = float(input('Ingrese el precio máximo: $'))
        popularidad = "popularidad"
        disponibilidad = True
        id_ubicacion = int(input('Ingrese ID de la ubicación: '))
        imagen = "imagen1!"
        destino_culinario=DestinoCulinario(id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen)
        self.destinos_culinarios.append(destino_culinario)


    def buscar_destino_culinario(self, id_destino_culinario):
        for destinos_culinarios in self.destinos_culinarios:
            if destinos_culinarios.id == id_destino_culinario:
                return destinos_culinarios
        return f'Destino culinario no encontrado'
    
    def eliminar_destino_culinario(self, id_destino_culinario):
        destino_culinario = self.buscar_destino_culinario(id_destino_culinario)
        self.destinos_culinarios.remove(destino_culinario)

    def modificar_destino_culinario(self, id_destino_culinario):
        destino_culinario = self.buscar_destino_culinario(id_destino_culinario)
        if destino_culinario is not None:
            nombre = input('Ingrese el destino: ').title()
            tipo_cocina = input('Ingrese el tipo de cocina: ').title()
            ingredientes = []
            while True:
                ingrediente = input('Ingrese ingrediente: ').title()
                if ingrediente == "" or ingrediente == " ":
                    break
                else:
                    ingredientes.append(ingrediente)
            precio_minimo = float(input('Ingrese el precio mínimo: $'))
            precio_maximo = float(input('Ingrese el precio máximo: $'))
            popularidad = "popularidad"
            disponibilidad = True
            id_ubicacion = int(input('Ingrese ID de la ubicación: '))
            imagen = "imagen1!"
            destino_culinario.nombre = nombre
            destino_culinario.tipo_cocina = tipo_cocina
            destino_culinario.ingredientes = ingredientes
            destino_culinario.precio_minimo = precio_minimo
            destino_culinario.precio_maximo = precio_maximo
            destino_culinario.popularidad = popularidad
            destino_culinario.disponibilidad = disponibilidad
            destino_culinario.id_ubicacion = id_ubicacion
            destino_culinario.imagen = imagen
        else:
            print('No se encontró el destino culinario')
    
    def cargar_json(self):
        with open("DatosJson/destinos_culinarios.json", "w", encoding='utf-8') as archivo:
            lista = []
            for destino_culinario in self.destinos_culinarios:
                lista.append(destino_culinario.a_json())
            json.dump(lista, archivo, ensure_ascii= False, indent =3)