from repositorio import Repositorio
from commit import Commit
from archivo import Archivo
from rama_v2 import Rama
from archivo import lista_para_commit

repositorio = Repositorio()
commit = Commit()
archivo = Archivo()

def main():
    
    while True:
        print("\n === Git Simulation Command Menu === \n" )
        print("'git branch <name_branch>' - Crear nueva rama")
        print("'git branch' - Ver rama actual")
        print("'git checkout <name_branch>' - Cambiar de rama")
        print("'git commit -m <message>' - Hacer commit")
        print("'git log' - Mostrar historial de commits")
        print("'git merge <name_branch>' - Fusionar dos ramas")
        print("'nano' - Crear archivo")
        print("'git log -n 1 <name_branch>' - Ver ultimo commit de la rama")
        print("'git add .' - Agregar todos los archivos al staged")
        print("===================================")

        comando = input()

        match comando:
            case "git branch":
                print(repositorio.git_branch())

            case comando if comando.startswith("git branch"):
                nombre_rama = comando.split(" ", 2)[2]
                repositorio.git_branch_crear_rama(nombre_rama)

            case comando if comando.startswith("git checkout"):
                nombre_otra_rama = comando.split(" ", 2)[2]
                repositorio.git_checkout_cambiar_rama(nombre_otra_rama)
            
            case "git add .":
                print(archivo.git_add())   

            case comando if comando.startswith("git commit -m"):
                if lista_para_commit == []:
                    print("NO hay archivos en el stage")
                else: 
                    descripcion = comando.split(" ", 3)[3]
                    print(commit.git_commit(descripcion, repositorio.rama_actual))

            case "git log":
                commit.git_log()

            case "nano":
                nombre = input("Nombre del archivo: ")
                contenido = input("Contenido del archivo: ")
                archivo.crear_archivo(nombre, contenido)

            case comando if comando.startswith("git merge"):
                rama = comando.split(" ", 2)[2]
                repositorio.git_merge(rama, repositorio.rama_actual)

            case comando if comando.startswith("git log -n 1"):
                rama_commit = comando.split(" ", 4)[4]
                ultimo_commit = None

                # Itera sobre los commits en total_commit
                for subcommit in Commit.total_commit:
                    # Verifica si el nombre de la rama está en el commit
                    if rama_commit in subcommit:
                        ultimo_commit = subcommit  # Actualiza el último commit encontrado

                # Después de iterar, verifica si se encontró un último commit
                if ultimo_commit is not None:
                    # Imprime el último commit encontrado
                    print(f"Último commit en la rama '{rama_commit}': {ultimo_commit}")
                    Rama(rama_commit).agregar_commit(ultimo_commit)  # Agrega el commit a la rama
                else:
                    print(f"No se encontró ningún commit en la rama '{rama_commit}'.")

print(f"desde main {lista_para_commit}")
      


if __name__ == "__main__":
    main()
    