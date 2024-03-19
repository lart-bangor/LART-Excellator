import sys
from rich import print

tryAgain =str = "Please check folder and try again"

def is_empty(folder):
    print(f'\n\t[red]EMPTY DIRECTORY[/red]: The folder [yellow]{folder}[/yellow] is empty.\n' )

def selection(folder):
    print(f'\n You have selected to work in the following folder: [yellow]{folder}[/yellow]')

def data_selection(name):
    print(f'\n\t\tData folder selected: [yellow]{name}[/yellow]\n')

def not_found(folder):
    print(f'\n\t\t[red]NOT FOUND[/red]: There is no folder named [yellow]\{folder} [/yellow]in the current directory.') 
    print(f'{tryAgain:>60}')

def locate(dir, full_path):
    print(f'\t\t[green]Dir:[/green] {dir}')
    print(f'\t\t[green]Path:[/green] {full_path}')

def processing_info(fname):
    print(f'\n Currently processing: [yellow]{fname}[/yellow]\n')

def completed_info(task, fname):
     print(f'\n [green]{task} data successfully extracted[/green] and saved to file: [purple]{fname}[/purple] \n')
    
def abort():
    print("\nOperation aborted by user")
    sys.exit()
     