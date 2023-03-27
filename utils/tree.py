import os

def tree(directory, padding, is_last=False, output=None):
    """
    Affiche un arbre de fichiers et de dossiers pour le répertoire spécifié.

    :param directory: Le chemin du répertoire pour lequel générer l'arbre de fichiers.
    :type directory: str
    :param padding: Le niveau d'indentation pour l'affichage de l'arbre de fichiers.
    :type padding: str
    :param is_last: Indique si le répertoire actuel est le dernier de la liste.
    :type is_last: bool

    Cette fonction ignore les fichiers et les dossiers dont le nom commence par un point (.).
    """
    if is_last:
        print(padding[:-3] + '└──', os.path.basename(directory), sep='')
        padding = padding[:-3] + '   '
    else:
        print(padding[:-3] + '├──', os.path.basename(directory), sep='')
        padding = padding[:-3] + '│  '

    files = []
    dirs = []
    if os.path.isdir(directory):
        for entry in os.listdir(directory):
            if entry.startswith('.') or entry == 'build':
                continue
            path = os.path.join(directory, entry)
            if os.path.isfile(path):
                files.append(entry)
            else:
                dirs.append(entry)

    # Afficher les fichiers
    for i, file in enumerate(sorted(files)):
        if i == len(files) - 1 and len(dirs) == 0:
            print(padding + '└──', file)
        else:
            print(padding + '├──', file)

    # Afficher les dossiers
    for i, folder in enumerate(sorted(dirs)):
        path = os.path.join(directory, folder)
        if i == len(dirs) - 1:
            tree(path, padding + '   ', True)
        else:
            tree(path, padding + '   ', False)
    

if __name__ == '__main__':
    tree_output = tree('.', '', True)
    print(tree_output)