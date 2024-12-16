import pathlib
from pathlib import Path
import json
import shutil


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
        shutil.copy(source, destination)

def add_path(path, to, description):
    data = read_file()
    data.append({"path": path, "to": to, "description": description})
    with open(pathlib.Path(__file__).parent / 'shared/path.json', 'w') as f:
        json.dump(data, f)

        
if __name__ == "__main__":
    copy_files(read_file())
