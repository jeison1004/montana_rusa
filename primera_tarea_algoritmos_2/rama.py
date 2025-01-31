"""
Este modulo va a tener a la clase Rama, la cual va a tener un metodo para crear ramas y ver en que rama se encuentra, otro para mostar los commits,
y otro para fusionar las ramas
"""

class Rama2():
    total_de_ramas = []
    rama_actual = "master"

    #Metodo para que el usuario vea en que rama se encuentra
    def git_branch(self):
        return self.rama_actual
    
    #Metodo para crear una nueva rama, va a recibir el nombre de la nueva rama y lo va a agregar a la lista de total_de_ramas
    def git_branch_crear_rama(self, nombre_nueva_rama):
        nueva_rama = nombre_nueva_rama
        self.total_de_ramas.append(nueva_rama)

    #Metodo para cambiar de rama, va a recibir el nombre de una rama, se va a revisar si esa rama existe, y si existe se cambia el valor de rama_actual
    def git_branch_cambiar_rama(self, rama_para_cambiar):
        if rama_para_cambiar == self.rama_actual:
            return "Ya se encuentra en la rama"
        else: 
            for i in self.total_de_ramas:
                if rama_para_cambiar == i:
                    self.rama_actual = rama_para_cambiar
                    return "Rama cambiada con exito"

                else: 
                    return "La rama no existe"
                
# rama_prueba = Rama()
# rama_prueba.git_branch_crear_rama("Ramita")
# rama_prueba.git_branch_cambiar_rama("Ramita")

            

    

