# 🌟 Backup project

Welcome to the **Backup** project! 🚀

## Project Description

A simple project for copy files and folders to other pat

## Key Features

<!--- **Automatic Backup**: Schedule automatic backups to ensure that your data is always up-to-date.-->
- **Easy Recovery**: Recover your data with a few simple clicks.
- **User-Friendly Interface**: Easily navigate through the features with a clear and intuitive interface.
- Multi-Platform Compatibility\*\*: Works on Windows, macOS and Linux.

## Installation

To get started with the Backup project, follow these simple steps:

1. Clone the repository:
   ```bash git clone https://github.com/Gabry848/backup.git```
2. Browse to the project directory:
   ```bash cd Backup```
3. Install the required dependencies:
   ```bash pip install -r requirements.txt```

## Usage

Once installed, you can start the programme by running the following command:

```bash python main.py```

The Backup project offers a number of CLI commands to manage the file paths to be copied and moved. Here is a list of the commands available:

- **add**: Add a new file path to be copied.
  ```bash
  python main.py add --path <percorso-file> --to <percorso-destinazione> --description <descrizione-opzionale>
  ```

- **remove**: Remove a file path.
  ```bash python main.py remove --path <percorso-file>```
  you can olso remove path with his id
  ```bash python main.py remove --index <id>```

- **list**: Show a table of all the paths of files that will be moved.
  ```bash python main.py list```

- **start**: Move the files to the new paths specified.
  ```bash python main.py start```

- **clear**: Clear all the paths stored.
  ```bash python main.py clear```

You can also use the `--help` option to get more information about each command.

## Contribute

We are always looking for contributors! If you wish to contribute, please follow these steps:

1. Fork the project.
2. Create a new branch for your feature (`git checkout -b feature/new-functionality`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Do branch push (`git push origin feature/new-functionality`).
5. Open a Pull Request.

## Licence

This project is distributed under the MIT licence. See the [LICENSE](LICENSE) file for more details.
