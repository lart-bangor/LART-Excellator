import sys
from rich import print

tryAgain: str = "Please check folder and try again"

def is_empty(folder: str) -> None:
    """Prints "empty folder" message to console"""
    print(f'\n\t[bright_red]EMPTY DIRECTORY[/bright_red]: The folder [yellow]{folder}[/yellow] is empty.\n' )

def selection(folder: str)  -> None:
    """Prints selected folder path to console"""
    print(f'\n You have selected to work in the following folder: [yellow]{folder}[/yellow]')

def data_selection(name: str)  -> None:
    """Prints path of selected data fodler to console"""
    print(f'\n\t\tData folder selected: [yellow]{name}[/yellow]\n')

def not_found(folder: str)  -> None:
    """Prints 'folder not found' message to console"""
    print(f'\n\t\t[red]NOT FOUND[/red]: There is no folder named [yellow]\{folder} [/yellow]in the current directory.') 
    print(f'{tryAgain:>60}')

def locate(dir: str, full_path: str)  -> None:
    """Prints directory path and full file path to console"""
    print(f'\t\t[green]Dir:[/green] {dir}')
    print(f'\t\t[green]Path:[/green] {full_path}')

def processing_info(fname: str)  -> None:
    """Prints name of file being processed"""
    print(f'\n Currently processing: [yellow]{fname}[/yellow]\n')

def completed_info(task: str, fname: str)  -> None:
     """Prints message on completion of task"""
     print(f'\n [green]{task} data successfully extracted[/green] and saved to file: [purple]{fname}[/purple] \n')
    
def abort() -> None:
    """Calls sys.exit() to exit programme"""
    print("\nOperation aborted by user")
    sys.exit()
     