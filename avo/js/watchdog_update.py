import os
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class DossierHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.mettre_a_jour_json()

    def on_created(self, event):
        self.mettre_a_jour_json()

    def on_deleted(self, event):
        self.mettre_a_jour_json()

    def mettre_a_jour_json(self):
        folder_path = './medias'
        nb_de_fichiers = len([f for f in os.listdir(folder_path) 
                              if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith('.')])
        json_file_path = os.path.join("js", "int.json")
        with open(json_file_path, "w") as fichier:
            json.dump({"Nb de fichiers": nb_de_fichiers}, fichier)
        print(f"Fichier JSON mis à jour : {nb_de_fichiers} fichiers")

if __name__ == "__main__":
    folder_path = './medias'
    event_handler = DossierHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
