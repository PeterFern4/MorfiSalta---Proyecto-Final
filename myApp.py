import tkinter
import customtkinter
import json
from tkinter import messagebox
from Entidades.usuario import Usuario
from Entidades.idU_temp import IdUsuario
from Entidades.ubicacion import Ubicacion
from Entidades.destino_culinario import DestinoCulinario
from customtkinter import CTkFrame, CTkImage, CTkCanvas
from PIL import ImageTk, Image
import customtkinter as ctk
from tkintermapview import TkinterMapView
import webbrowser

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')



#===============================================VENTANA
class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('MORFI Salta - versión 1.0')
        self.iconbitmap("Imagenes\icono.ico")
        self.geometry('700x500+350+120')
        self.resizable(False, False)
        self.iniciar()
        self.id_usuario_comp = None
        
    def iniciar(self):    
            self.frame_titulo = FrameTitulo(self)
            self.frame_principal = FramePrincipal(self)
            self.frame_usuario = FrameUsuario(self)

            self.frame_titulo.pack(fill="both", expand=False)
            self.frame_principal.pack(fill="both", expand=True)
            self.frame_usuario.pack(fill="both", expand=True)

#===============================================FRAME SUPERIOR
class FrameTitulo(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=100)
        
        imagen_fondo = Image.open("Imagenes\Titulo.jpg")
        fondo_titulo = CTkImage(imagen_fondo, size=(700, 100))
        self.label_fondo = customtkinter.CTkLabel(self, text="", image=fondo_titulo, anchor="nw")
        self.label_fondo.pack(fill="both", expand=True)



#===============================================FRAME INFERIOR PRINCIPAL
class FramePrincipal(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=400)
        self.master = master

        self.canvas = customtkinter.CTkCanvas(self, width=700, height=400, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        imagen_frameP = Image.open(r"Imagenes\fondo_frameP.jpg")
        self.fondo_frameP = ImageTk.PhotoImage(imagen_frameP)

        self.canvas.create_image(0, 0, anchor="nw", image=self.fondo_frameP)

        
        #------------------------INICIAR SESION
        def iniciar_sesion():
            iniciarSesion = customtkinter.CTkToplevel()
            iniciarSesion.title("Ingreso de Usuario")
            iniciarSesion.geometry("300x150+550+295")

            iniciarSesion.grab_set()

            label_id = customtkinter.CTkLabel(iniciarSesion, text="Ingrese DNI")
            label_id.pack(pady=10)

            entry_id = customtkinter.CTkEntry(iniciarSesion, placeholder_text='Sin puntos')
            entry_id.pack(pady=10)

            boton_validar = customtkinter.CTkButton(iniciarSesion, text="Aceptar", command=lambda: validar_ingreso(entry_id.get()),fg_color='orange',hover_color ='orange3', text_color='black')
            boton_validar.pack(pady=10)

            def validar_ingreso(id_usuario):
                with open(r"DatosJson\usuarios.json", "r") as archivo:
                    usuarios = json.load(archivo)

                for usuario in usuarios:
                    if usuario["ID"] == id_usuario:
                        idLista = []
                        with open("DatosJson\idU_Temp.json", "r") as archivo:
                            id_temp_json = json.load(archivo)
                        for id in id_temp_json:
                            idLista.append(IdUsuario.from_json(id))
                        nuevoID = IdUsuario(entry_id.get())
                        idLista.append(nuevoID)
                        with open("DatosJson\idU_Temp.json", "w") as archivo:
                            lista = []
                            for id in idLista:
                                lista.append(id.a_json())
                            json.dump(lista, archivo)
                        iniciarSesion.after(0, iniciarSesion.destroy)
                        FramePrincipal.pack_forget(self)
                        FrameUsuario.pack(self, fill="both", expand=True)
                        break
                else:
                    messagebox.showerror("Error", "No estás registrado.")
                    iniciarSesion.after(0, iniciarSesion.destroy)

        boton_ingresar = customtkinter.CTkButton(self, text='Ingresar', command= iniciar_sesion, fg_color='orange',hover_color ='orange3', text_color='black')
        boton_ingresar.place(relx=0.2, rely=0.8, anchor=tkinter.CENTER)
        #------------------------REGISTRO DE USUARIOS
        def registro_usuario():
            registrarUsuario = customtkinter.CTkToplevel()
            registrarUsuario.title("Alta de Usuario")
            registrarUsuario.geometry("300x225+550+295")

            registrarUsuario.grab_set()

            id_entry_reg = customtkinter.CTkEntry(registrarUsuario, placeholder_text='Ingrese DNI sin puntos')
            id_entry_reg.pack(pady=10)
    
            nombre_entry_reg = customtkinter.CTkEntry(registrarUsuario, placeholder_text='Nombre')
            nombre_entry_reg.pack(pady=10)

            apellido_entry_reg = customtkinter.CTkEntry(registrarUsuario, placeholder_text='Apellido')
            apellido_entry_reg.pack(pady=10)

            boton_validar = customtkinter.CTkButton(registrarUsuario, text="Aceptar", command=lambda: alta_usuario(id_entry_reg.get(), nombre_entry_reg.get(), apellido_entry_reg.get()),fg_color='orange',hover_color ='orange3', text_color='black')
            boton_validar.pack(pady=10)

            def alta_usuario(id, nombre, apellido):
                usuLista = []
                with open("DatosJson/usuarios.json", "r") as archivo:
                    usuarios_json = json.load(archivo)
                    for usuario in usuarios_json:
                        usuLista.append(Usuario.from_json(usuario))

                nuevoUsuario = Usuario(id, nombre.title(), apellido.title(), historial_rutas=[])
                usuLista.append(nuevoUsuario)

                with open("DatosJson/usuarios.json", "w") as archivo:
                    lista = []
                    for usuario in usuLista:
                        lista.append(usuario.a_json())
                    json.dump(lista, archivo, indent =3)
                messagebox.showinfo("EUREKA!","¡Registro exitoso!")
                registrarUsuario.after(0, registrarUsuario.destroy)
    
        boton_ingresar = customtkinter.CTkButton(self, text='Registrarse', command= registro_usuario, fg_color='orange',hover_color ='orange3', text_color='black')
        boton_ingresar.place(relx=0.8, rely=0.8, anchor=tkinter.CENTER)

        #------------------------REDES SOCIALES
        def ir_facebook(self):
            url_f = "https://www.facebook.com/morfitelefe?mibextid=ZbWKwL"
            webbrowser.open(url_f)

        imagen_f = Image.open(r"Imagenes\redes_face.jpg")
        imagen_face = CTkImage(imagen_f, size=(30, 30))
        reds_f_label=customtkinter.CTkLabel(self, text="", image=imagen_face, width=30, height=30, bg_color="transparent")
        reds_f_label.place(relx=0.03, rely=0.92, anchor="w")
        reds_f_label.bind("<Button-1>", ir_facebook)
        
        
        def ir_instagram(self):
            url_i = "https://instagram.com/morfiitelefe?igshid=MzRlODBiNWFlZA=="
            webbrowser.open(url_i)

        imagen_i = Image.open(r"Imagenes\redes_insta.png")
        imagen_insta = CTkImage(imagen_i, size=(30, 30))
        reds_i_label=customtkinter.CTkLabel(self, text="", image=imagen_insta, width=30, height=30, bg_color="transparent")
        reds_i_label.place(relx=0.09, rely=0.92, anchor="w")
        reds_i_label.bind("<Button-1>", ir_instagram)


#===============================================FRAME INFERIOR USUARIOS
class FrameUsuario(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=400)
        self.master = master

        self.canvas = customtkinter.CTkCanvas(self, width=700, height=400, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        imagen_frameP = Image.open(r"Imagenes\fondo_frameU.jpg")
        self.fondo_frameP = ImageTk.PhotoImage(imagen_frameP)
        self.canvas.create_image(0, 0, anchor="nw", image=self.fondo_frameP)       
        
        #------------------------MOSTRAR DESTINOS EN LISTA
        with open("DatosJson/destinos_culinarios.json", "r") as archivo:
            destinos = json.load(archivo)
            lista_destinos = []
            for destino in destinos:
                lista_destinos.append(destino["Nombre"])       

     
        def mostrar_informacion(self):
            destino_seleccionado = opcion_seleccionada.get()
            if destino_seleccionado != 'Elegir Destino':
                informacionDestino = customtkinter.CTkToplevel()
                informacionDestino.title("Información del Lugar")
                informacionDestino.geometry("600x300+430+180")
                informacionDestino.grab_set()
                
                frame_info = customtkinter.CTkFrame(informacionDestino, width=600, height=300, fg_color="transparent")
                frame_info.pack(padx=0, pady=0)

                fondo_info = Image.open(r"Imagenes\fondo_infoD.jpg")
                fondo_info_destino = CTkImage(fondo_info, size=(600, 300))
                
                with open (r'DatosJson\ubicacion.json', 'r') as file:
                    ubicaciones_j = json.load(file)
                
                for destino in destinos:
                    
                    if destino['Nombre'] == destino_seleccionado:
                        
                        for ub in ubicaciones_j:
                            if ub['ID']==destino['Ubicacion']:
                                Direccion = ub['Direccion']
                                latitud = ub['Coordenadas'][0]
                                longitud = ub['Coordenadas'][1]
                                
                        
                        info = f"Nombre: {destino['Nombre']}\nTipo de Cocina:{destino['Tipo de Cocina']}\nIngredientes: {destino['Ingredientes']}\nRango de Precios: ${destino['Precio Minimo']} - ${destino['Precio Maximo']}\nPopularidad: {destino['Popularidad']}\nDisponibilidad: {destino['Disponibilidad']}\nDirección: {Direccion}"
                        
                        fondo_label=customtkinter.CTkLabel(frame_info, text="", image=fondo_info_destino, width=600, height=300, fg_color="transparent")
                        fondo_label.pack(fill="both", expand=True, padx=0, pady=0)
                        
                        info_label = customtkinter.CTkLabel(fondo_label, text=info, justify="left", wraplength=250, font=("Comic Sans MS",13, "bold"), width=200, height=200, text_color="white", anchor="w", fg_color="transparent")
                        info_label.place(relx=0.05, rely=0.4, anchor="w")

                        foto_info = Image.open(destino['Imagen'])
                        foto_info_destino = CTkImage(foto_info, size=(200, 200))
                        imagen_destino_label=customtkinter.CTkLabel(fondo_label, text="", image=foto_info_destino, width=200, height=200, bg_color="transparent")
                        imagen_destino_label.place(relx=0.6, rely=0.4, anchor="w")

                        opcion_seleccionada.set("Elegir Destino")
                        id_para_ruta=destino['ID']

                
                #------------------------VER EN MAPA
                def ver_en_mapa():
                    informacionDestino.title(f"Ver en mapa: {Direccion}")
                    fondo_VerMapa = Image.open(r"Imagenes\fondo_ModificarDatos.jpg")
                    fondo_ver_en_mapa = CTkImage(fondo_VerMapa, size=(600, 300))

                    frame_ver_en_mapa = customtkinter.CTkFrame(informacionDestino, width=600, height=300, fg_color="transparent")
                    frame_info.pack_forget()
                    frame_ver_en_mapa.pack(padx=0, pady=0)
                    
                    label_ver_en_mapa = customtkinter.CTkLabel(frame_ver_en_mapa, width=600, height=300, text="", image=fondo_ver_en_mapa, fg_color="transparent")
                    label_ver_en_mapa.pack(padx=0, pady=0)

                    ver_mapa = TkinterMapView(frame_ver_en_mapa, width=600, height=250, corner_radius=0)
                    ver_mapa.place(relx=0, rely=0, anchor = "nw")
                    ver_mapa.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
                    ver_mapa.set_position(latitud, longitud)
                    ver_mapa.set_marker(latitud, longitud, text=Direccion)
                    ver_mapa.set_zoom(15)


                    #------------------------CERRAR VENTANA VER EN MAPA
                    def cerrar_ventana():
                        informacionDestino.after(0, informacionDestino.destroy)

                    boton_cerrar = customtkinter.CTkButton(frame_ver_en_mapa, text="Cerrar", command= cerrar_ventana, fg_color='red2',hover_color ='red4', text_color='black')
                    boton_cerrar.place(relx=0.76, rely=0.88)

                boton_mapa = customtkinter.CTkButton(frame_info, text="Ver en Mapa", fg_color='orange',hover_color ='orange3', text_color='black', command = ver_en_mapa)
                boton_mapa.place(relx=0.01, rely=0.88)

                #------------------------AGREGAR A MI RUTA
                def agregar_ruta():
                    with open("DatosJson\idU_Temp.json", "r") as archivo:
                        id_temp_json = json.load(archivo)
                    listaUser=[]
                    with open(r"DatosJson\usuarios.json", "r") as arc:
                        us = json.load(arc)
                        for i in us:
                            listaUser.append(Usuario.from_json(i))
                    for id in id_temp_json:
                        for user in us:
                            if id['DNI'] == user['ID']:
                                print(destino['ID'])
                                user['Historial de Rutas'].append(id_para_ruta)
                                with open("DatosJson/usuarios.json", "w") as arq:
                                    lista = []
                                    for use in listaUser:
                                        lista.append(use.a_json())
                                    json.dump(lista, arq, indent =3)
                    messagebox.showinfo("Ruta Agregada","Ruta agregada con éxito.")

                boton_agregar_ruta = customtkinter.CTkButton(frame_info, command=agregar_ruta, text="Agregar a Mi Ruta", fg_color='orange',hover_color ='orange3', text_color='black')
                boton_agregar_ruta.place(relx=0.26, rely=0.88)

                #------------------------CALIFICAR DESTINO
                def calificar():
                    informacionDestino.title(f"Review")
                    fondo_Review = Image.open(r"Imagenes\fondo_ModificarDatos.jpg")
                    fondo_review_destinos = CTkImage(fondo_Review, size=(600, 300))

                    frame_review_destinos = customtkinter.CTkFrame(informacionDestino, width=600, height=300, fg_color="transparent")
                    frame_info.pack_forget()
                    frame_review_destinos.pack(padx=0, pady=0)
                    
                    label_review = customtkinter.CTkLabel(frame_review_destinos, width=600, height=300, text="", image=fondo_review_destinos, fg_color="transparent")
                    label_review.pack(padx=0, pady=0)
                    comentario = customtkinter.CTkEntry()

                    #------------------------CERRAR VENTANA VER EN MAPA
                    def cerrar_ventana():
                        informacionDestino.after(0, informacionDestino.destroy)

                    boton_cerrar = customtkinter.CTkButton(frame_review_destinos, text="Cerrar", command= cerrar_ventana, fg_color='red2',hover_color ='red4', text_color='black')
                    boton_cerrar.place(relx=0.76, rely=0.88)


                boton_calificar = customtkinter.CTkButton(frame_info, text="Calificar Lugar", fg_color='orange',hover_color ='orange3', text_color='black')
                boton_calificar.place(relx=0.51, rely=0.88)

                #------------------------CERRAR VENTANA
                def cerrar_ventana():
                    informacionDestino.after(0, informacionDestino.destroy)

                boton_cerrar = customtkinter.CTkButton(frame_info, text="Cerrar", command= cerrar_ventana, fg_color='red2',hover_color ='red4', text_color='black')
                boton_cerrar.place(relx=0.76, rely=0.88)


        opcion_seleccionada = customtkinter.StringVar()
        opciones_destinos = customtkinter.CTkOptionMenu(self, values=lista_destinos, command=mostrar_informacion, variable=opcion_seleccionada, fg_color='orange', text_color='black')
        opciones_destinos.set("Elegir Destino")
        opciones_destinos.place(relx=0.055, rely=0.045, anchor='nw')
        opciones_destinos.bind("<Button-1>", mostrar_informacion)
                
        
        #------------------------EXPLORAR MAPA        
        def explorar_mapa():
            exp_mapa = TkinterMapView(self, width=490, height=320, corner_radius=0)
            exp_mapa.place(relx=0.04, rely=0.15, anchor = "nw")
            exp_mapa.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
            exp_mapa.set_address("Salta, Salta")
            exp_mapa.set_zoom(13)
            with open (r'DatosJson\destinos_culinarios.json', 'r') as archivo:
                destinos_json = json.load(archivo)
                for destino in destinos_json:
                    detalle = DestinoCulinario.from_json(destino)
                    with open (r'DatosJson\ubicacion.json', 'r') as archi:
                        ubicaciones_json = json.load(archi)
                        for ubicacion in ubicaciones_json:
                            marcador = Ubicacion.from_json(ubicacion)
                            if detalle.id_ubicacion == marcador.id:
                                exp_mapa.set_marker(marcador.coordenadas[0], marcador.coordenadas[1], text=detalle.nombre, font=("Times New Roman", 10))

        boton_explorar = customtkinter.CTkButton(self, text='Explorar Mapa', command= explorar_mapa, fg_color='orange',hover_color ='orange3', text_color='black')
        boton_explorar.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)
        
        #------------------------MI CUENTA
        def mi_cuenta():
            with open("DatosJson\idU_Temp.json", "r") as archivo:
                id_temp_json = json.load(archivo)
            
            with open(r"DatosJson\usuarios.json", "r") as arc:
                us = json.load(arc)
            
            for id in id_temp_json:
                for user in us:
                    if id['DNI'] == user['ID']:
                        dni = user['ID']
                        nombre = user['Nombre']
                        apellido = user['Apellido']
                        rutas = user['Historial de Rutas']
            
            info_usuario = f"DNI: {dni}\nNombre: {nombre}\nApellido: {apellido}\nMis Rutas: {rutas}"

            miCuenta = customtkinter.CTkToplevel()
            miCuenta.title(f"Cuenta de {nombre}")
            miCuenta.geometry("300x400+430+180")
            miCuenta.grab_set()

            fondo_cuenta = Image.open(r"Imagenes\fondo_MiCuenta.jpg")
            fondo_cuenta_usuario = CTkImage(fondo_cuenta, size=(300, 400))

            frame_cuenta = customtkinter.CTkFrame(miCuenta, width=300, height=400, fg_color="transparent")
            frame_cuenta.pack(padx=0, pady=0)
            fondo_label=customtkinter.CTkLabel(frame_cuenta, text=info_usuario, wraplength=250, justify="left", font=("Comic Sans MS",16, "bold"), image=fondo_cuenta_usuario, width=300, height=400, fg_color="transparent", anchor="n")
            fondo_label.pack(fill="both", expand=True, padx=0, pady=0)

            #------------------------FRAME MODIFICAR DATOS            
            def modificar_datos():    
                fondo_modificar = Image.open(r"Imagenes\fondo_ModificarDatos.jpg")
                fondo_modificar_usuario = CTkImage(fondo_modificar, size=(300, 400))

                frame_modificar = customtkinter.CTkFrame(miCuenta, width=300, height=400, fg_color="transparent")
                frame_cuenta.pack_forget()
                frame_modificar.pack(padx=0, pady=0)
                
                label_modificar = customtkinter.CTkLabel(frame_modificar, width=300, height=400, text="", image=fondo_modificar_usuario, fg_color="transparent")
                label_modificar.pack(padx=0, pady=0)
                
                dni_entry_reg = customtkinter.CTkEntry(frame_modificar, placeholder_text='Ingrese DNI sin puntos')
                dni_entry_reg.place(relx=0.25, rely=0.3)
    
                nombre_entry_reg = customtkinter.CTkEntry(frame_modificar, placeholder_text='Nombre')
                nombre_entry_reg.place(relx=0.25, rely=0.45)

                apellido_entry_reg = customtkinter.CTkEntry(frame_modificar, placeholder_text='Apellido')
                apellido_entry_reg.place(relx=0.25, rely=0.6)

                def modificar_usuario(id):
                    listaUS=[]
                    with open(r"DatosJson\usuarios.json", "r") as file:
                        u_json = json.load(file)
                        for usuario in u_json:
                            listaUS.append(Usuario.from_json(usuario))
                            for user in listaUS:
                                if user.id == id:
                                    user.id = dni_entry_reg.get()
                                    user.nombre = nombre_entry_reg.get()
                                    user.apellido = apellido_entry_reg.get()
                                    messagebox.showinfo("Bien Hecho!","Datos actualizados correctamente.")
                                    miCuenta.after(0, miCuenta.destroy)

                boton_guardar_datos = customtkinter.CTkButton(frame_modificar, text="Actualizar Datos", fg_color='orange',hover_color ='orange3', text_color='black', command=modificar_usuario(dni_entry_reg.get()))
                boton_guardar_datos.place(relx=0.25, rely=0.8)

                #------------------------CERRAR VENTANA MODIFICAR DATOS
                def cerrar_modificar():
                    miCuenta.after(0, miCuenta.destroy)                
                
                boton_volver = customtkinter.CTkButton(frame_modificar, text="Cerrar", command= cerrar_modificar, fg_color='red2',hover_color ='red4', text_color='black')
                boton_volver.place(relx=0.25, rely=0.88)

            boton_modificar = customtkinter.CTkButton(frame_cuenta, text="Modificar Datos", fg_color='orange',hover_color ='orange3', text_color='black', command=modificar_datos)
            boton_modificar.place(relx=0.25, rely=0.72)

            boton_eliminar = customtkinter.CTkButton(frame_cuenta, text="Eliminar Cuenta", fg_color='orange',hover_color ='orange3', text_color='black')
            boton_eliminar.place(relx=0.25, rely=0.8)

            #------------------------CERRAR VENTANA MI CUENTA
            def cerrar_ventana():
                miCuenta.after(0, miCuenta.destroy)

            boton_volver = customtkinter.CTkButton(frame_cuenta, text="Cerrar", command= cerrar_ventana, fg_color='red2',hover_color ='red4', text_color='black')
            boton_volver.place(relx=0.25, rely=0.88)

        boton_profile = customtkinter.CTkButton(self, text='Mi Cuenta', command= mi_cuenta, fg_color='orange',hover_color ='orange3', text_color='black')
        boton_profile.place(relx=0.86, rely=0.08, anchor=tkinter.CENTER)

        #------------------------CERRAR SESION
        def cerrar_sesion():

            with open("DatosJson\idU_Temp.json", "r") as archivo:
                id_temp_json = json.load(archivo)
                id_temp_json.clear()
                
            with open("DatosJson\idU_Temp.json", "w") as archivo:
                json.dump(id_temp_json, archivo)

            FrameUsuario.pack_forget(self)
            FramePrincipal.pack(self, fill="both", expand=True)

        boton_logout = customtkinter.CTkButton(self, text='Cerrar Sesión', command= cerrar_sesion, fg_color='red2',hover_color ='red4', text_color='black')
        boton_logout.place(relx=0.86, rely=0.92, anchor=tkinter.CENTER)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()