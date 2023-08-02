from Entidades.idU_temp import IdUsuario
import json
class ABM_DestinoCulinario:
    def __init__ (self):
        id_Lista = []
        with open("DatosJson\idU_Temp.json", "r") as archivo:
            id_temp_json = json.load(archivo)
        for data in id_temp_json:
            id_Lista.append(IdUsuario.from_json(data))
        self.id_usuario = id_Lista

    def agregar_id(self, id_temp):
        id = id_temp
        nuevo_id_temp=IdUsuario(id)
        self.id_usuario.append(nuevo_id_temp)

    #def buscar_destino_culinario(self, id_temp):
        #for destinos_culinarios in self.destinos_culinarios:
            #if destinos_culinarios.id == id_destino_culinario:
                #return destinos_culinarios
        #return f'Destino culinario no encontrado'
    
    def eliminar_id_temp(self, id_temp):
        self.id_usuario.remove(id_temp)

    def cargar_json(self):
        with open("DatosJson\idU_Temp.json", "w") as archivo:
            lista = []
            for id in self.id_usuario:
                lista.append(id.a_json())
            json.dump(lista, archivo)