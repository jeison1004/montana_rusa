from commit import lista_commit

class Repositorio:
    total_de_ramas = []
    rama_actual = "master"
    total_de_ramas.append(rama_actual)


    # Método para crear una nueva rama
    def git_branch_crear_rama(self, nombre_nueva_rama):
        if nombre_nueva_rama not in self.total_de_ramas:
            self.total_de_ramas.append(nombre_nueva_rama)
            print(f"Rama '{nombre_nueva_rama}' creada con éxito.")
        else:
            print(f"La rama '{nombre_nueva_rama}' ya existe.")


    # Método para cambiar de rama
    def git_checkout_cambiar_rama(self, rama_para_cambiar):
        if rama_para_cambiar == self.rama_actual:
            print("Ya se encuentra en la rama actual.")
        elif rama_para_cambiar in self.total_de_ramas:
            self.rama_actual = rama_para_cambiar
            print(f"Rama cambiada a '{self.rama_actual}' con éxito.")
        else:
            print("La rama no existe.")


    #Metodo para que el usuario vea en que rama se encuentra
    def git_branch(self):
        return self.rama_actual
    
    #Metodo para hacer merge
    def git_merge(self, rama_merge, rama_actual):
        # Verifica si la rama existe en la lista de commits
        rama_merge_encontrada = False
        archivos_a_mergear = None

        # Buscar la rama_merge en lista_commit
        for commit in lista_commit:
            if commit[3] == rama_merge:  # Suponiendo que el nombre de la rama está en la posición 3
                rama_merge_encontrada = True
                archivos_a_mergear = commit[-1]  # Extraemos el último elemento (archivos)
                break

        if not rama_merge_encontrada:
            return "La rama no existe"

        # Buscar la rama_actual en lista_commit
        for commit in lista_commit:
            if commit[3] == rama_actual:
                commit.append(archivos_a_mergear)  # Agregar los archivos a la lista de la rama actual
                return "Merge hecho con éxito"

        return "La rama actual no existe"




# prueba = Repositorio()
# print(prueba.git_branch())
# prueba.git_branch_crear_rama("CUlo")
# prueba.git_checkout_cambiar_rama("CUlo")

# print(prueba.git_branch())


        