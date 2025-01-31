#En este archivo estara la clase Archivo, y se usara para que el usuario cree nuevos archivos

class Archivo:
    list_total_archivos = []  # Lista en donde se guardarán los archivos en forma de una lista de dos elementos
    archivos_para_commit = []

    # Este método va a ser usado para crear archivos
    def crear_archivo(self, nombre, contenido):
        archivo = [] 
        archivo.append(nombre)
        archivo.append(contenido)

        # Se va a guardar el archivo en la lista total de archivos
        self.list_total_archivos.append(archivo)

        print(f"{nombre} creado con éxito")

   
    def git_add(self):
        if not self.list_total_archivos:
            return "No hay archivos"
        else:
            # Crear una copia de los archivos y los pasa al stage 
            self.archivos_para_commit = [archivo.copy() for archivo in self.list_total_archivos]
            self.list_total_archivos.clear()
            return "Archivos pasados al stage"


#Se instancia el objeto, y se guarda la lista en una variable para que sea usado en main
mi_lista = Archivo()
mi_lista.git_add()
lista_para_commit = mi_lista.archivos_para_commit






        
