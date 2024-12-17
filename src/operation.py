import json
import shutil

import os
import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
log = logging.getLogger("rich")


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

        if os.path.isfile(source):
            shutil.copy(source, destination)
            log.info("Copy file " + source + " to " + destination, extra={"markup": True})
        elif os.path.isdir(source):
            if os.path.exists(destination):
                log.info(f"La cartella di destinazione '{destination}' esiste già.", extra={"markup": True})
                # Opzione: sovrascrivi o unisci
                log.warning("Vuoi sovrascrivere la cartella? (s/n):", extra={"markup": True})
                risposta = input("                    ").lower()
                if risposta == 's':
                    shutil.rmtree(destination)  # Elimina la cartella di destinazione
                    shutil.copytree(source, destination)
                    log.info("Copy folder " + source + " to " + destination + " sovrascrivendo il contenuto.", extra={"markup": True})
                else:
                    log.info("operazione annullata.", extra={"markup": True})
            else:
                # Copia la cartella se la destinazione non esiste
                shutil.copytree(source, destination)
                log.info("Copy folder " + source + " to " + destination, extra={"markup": True})
            
        else:
            log.error("PATH NOT FOUND", extra={"markup": True})

def add_path(path, to, description):
    data = read_file()
    data.append({"path": path, "to": to, "description": description})
    with open('shared\\path.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    log.info("Added path " + path, extra={"markup": True})

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

    log.info("Remove path " + path, extra={"markup": True})    


def clear():
    data = []
    with open('shared\\path.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    log.info("Clear all paths", extra={"markup": True})
    
if __name__ == "__main__":
    copy_files(read_file())
