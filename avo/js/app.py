import os
import json


# Spécifiez le chemin du dossier
folder_path = './medias'

# Compter le nombre de fichiers visibles dans le dossier
nb_de_fichiers = len([f for f in os.listdir(folder_path) 
                  if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith('.')])

print(f"{nb_de_fichiers} fichiers")

json_file_path = os.path.join("js", "int.json")



# Écrire l'entier dans un fichier JSON
with open(json_file_path, "w") as fichier:
    json.dump({
        "nb_de_fichiers" : nb_de_fichiers
        }, fichier)

print(f"Fichier écrit dans : {json_file_path}")
