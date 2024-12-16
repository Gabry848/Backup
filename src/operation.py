import pathlib
from pathlib import Path
import json
import shutil

from rich import console


def read_file():
    with open(pathlib.Path(__file__).parent / 'shared/path.json') as f:
        return json.load(f)
    
    
def copy_files(data):
    data = read_file()
    
    for element in data:
        # Percorso del file da copiare
        source = Path(element['path'])

        # Nuovo percorso di destinazione
        destination = Path(element['to'])

        # Copiare il file
        try:
            shutil.copy(source, destination)
        except:
            print("Errore nel copiare il file")

def add_path(path, to, description):
    data = read_file()
    data.append({"path": path, "to": to, "description": description})
    with open(pathlib.Path(__file__).parent / 'shared/path.json', 'w') as f:
        json.dump(data, f, indent=4)

def remove_path_id(id_):
    data = read_file()
    data.pop(int(id_))
    with open(pathlib.Path(__file__).parent / 'shared/path.json', 'w') as f:
        json.dump(data, f, indent=4)
        
def remove_path(path):
    data = read_file()
    
    i = 0
    for element in data:
        if element['path'] == path:
            data.pop(i)
            break
        i += 1
    
    with open(pathlib.Path(__file__).parent / 'shared/path.json', 'w') as f:
        json.dump(data, f, indent=4)
        
if __name__ == "__main__":
    copy_files(read_file())
