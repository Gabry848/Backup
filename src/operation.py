import json
import shutil

import os
import sys

def get_base_path():
    """Restituisce il percorso base del file corrente, anche con PyInstaller."""
    if hasattr(sys, "_MEIPASS"):
        # Quando il programma è eseguibile
        return sys._MEIPASS
    else:
        # Quando è eseguito come script Python
        return os.path.dirname(os.path.abspath(__file__))


def read_file():
    with open('shared\\path.json') as f:
        return json.load(f)
    
    
def copy_files(data):
    data = read_file()
    
    for element in data:
        # Percorso del file da copiare
        source = element['path']

        # Nuovo percorso di destinazione
        destination = element['to']

        # Copiare il file
        try:
            shutil.copy(source, destination)
        except:
            print("Errore nel copiare il file")

def add_path(path, to, description):
    data = read_file()
    data.append({"path": path, "to": to, "description": description})
    with open('shared\\path.json', 'w') as f:
        json.dump(data, f, indent=4)

def remove_path_id(id_):
    data = read_file()
    data.pop(int(id_))
    with open('shared\\path.json', 'w') as f:
        json.dump(data, f, indent=4)
        
def remove_path(path):
    data = read_file()
    
    i = 0
    for element in data:
        if element['path'] == path:
            data.pop(i)
            break
        i += 1
    
    with open('shared\\path.json', 'w') as f:
        json.dump(data, f, indent=4)
        
if __name__ == "__main__":
    copy_files(read_file())
