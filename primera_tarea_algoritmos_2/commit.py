import uuid
from datetime import datetime
from archivo import lista_para_commit

class Commit:
    total_commit = []  # Aquí se van a guardar todos los commits que se hagan
     

    # Método para cuando el usuario ingrese el comando git commit
    def git_commit(self, descripcion, rama):
        nuevo_commit = [] 
        id = str(uuid.uuid4())  
        date = datetime.now()
        archivos_en_commit = lista_para_commit[:]  # Copia sin limpiar la lista


        # Armamos el commit y lo guardamos en la lista total commit
        nuevo_commit.append(id)
        nuevo_commit.append(date)
        nuevo_commit.append(descripcion)
        nuevo_commit.append(rama)  # Agregar el nombre de la rama al commit
        nuevo_commit.append(archivos_en_commit)  
        self.total_commit.append(nuevo_commit)

        return "Commit hecho con éxito"

    # Método para cuando el usuario ingrese el comando git log
    def git_log(self):
        logs = []  
        for commit in self.total_commit:
            # Formato: ID (rama) descripción fecha
            logs.append(f"{commit[0]} ({commit[3]}) {commit[2]} {commit[1]}") 
        
        # Mostrar los commits uno por uno
        for log in logs:
            print(log)
        
        return logs  # Retorna la lista de logs si es necesario



#Esto es para usar la lista de commit en el main
objeto_commit = Commit()
lista_commit = objeto_commit.total_commit
print(lista_para_commit)

 




    
        