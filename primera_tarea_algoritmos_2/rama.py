class Rama:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la rama
        self.commit_reciente = None  # Puntero al commit más reciente

    def agregar_commit(self, commit): #A este metodo lo debo pasar el commit que se crea
        self.commit_reciente = commit  # Actualiza el puntero al commit más reciente
        print(f"Rama: {self.nombre}, Último Commit: {self.commit_reciente if self.commit_reciente else 'Ninguno'}")
