import click
from rich.console import Console
from rich.table import Table

import operation

# Crea un'istanza di Console di Rich per stampare in modo bello
console = Console()

@click.command()
@click.option("--path", "-p", help="Path del file da copiare")
@click.option("--to", "-t", help="Path di destinazione")
@click.option("--description", "-d", help="Descrizione del file")
def add_path(path, to, description=""):
    """Aggiungi un nuovo path"""
    operation.add_path(path, to, description)    
    
@click.command()
@click.option("--path", "-p", help="Path del file da rimuovere", default="index")
@click.option("--index", "-i", help="Id del file fa rimuovere", default=None)    
def remove_path(path, index=None):
    """Rimuovi un path"""
    if path == "index":
        operation.remove_path_id(index)
    else:
        operation.remove_path(path)
    
@click.command()
def table():
    """tabella con tutti i path dei file che verranno spostati"""
    table = Table(title="List of paths")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Path", style="magenta")
    table.add_column("To", justify="left", style="green")
    table.add_column("Description", justify="right", style="green")

    i = 0
    for element in operation.read_file():
        # Aggiungi righe alla tabella
        table.add_row(str(i), element["path"], element["to"], element["description"])
        i += 1

    console.print(table)

@click.command()
def move_files():
    """copy the file to the new path """
    operation.copy_files(operation.read_file())


@click.group()
def cli():
    """Programma CLI con Click e Rich"""
    pass

# Aggiungi i comandi al gruppo CLI
cli.add_command(table)
cli.add_command(move_files)
cli.add_command(add_path)
cli.add_command(remove_path)


if __name__ == "__main__":
    cli()
