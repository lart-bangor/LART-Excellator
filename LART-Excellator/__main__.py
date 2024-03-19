#################################################
#                                               #
#   Files need to be in the folder called data  #
#   and then inside a language folder           #
#     e.g. CYM_ENG                              #
#                                               #
#################################################

# importing packages
import os
from rich.prompt import Prompt 
from rich import print
import navigate
import atol_extractor
import mgt_extractor

absolute_path = os.path.abspath(__file__)
directoryPath = os.path.dirname(absolute_path)
welcome: str = 'Exellator says: [green]Welcome[/green]. '
where: str = "You are currently working in the following folder:"
selection: str = "You selected: "
print(f'\n{welcome:>56}')
print(f'{where:>66}  [yellow]{directoryPath}[/yellow]')
print("\n")


dataType = Prompt.ask('\t\tEnter the test for which you want to extract data (Default is: AToL).',
                        default='AToL',
                        choices=['MGT', 'exit'])
if dataType == "exit":
    navigate.abort()

print(f'\n{selection:>30} [turquoise2]{dataType}[/turquoise2]')

folder_path = os.path.join(directoryPath, "data", dataType)


#'\\data\\' + dataType

if os.path.isdir(folder_path):
    if  os.listdir(folder_path):
        #navigate.selection(folder_path)
        print("\n")
        if dataType == "AToL":
            atol_extractor.extract_atol(folder_path, directoryPath)
        elif dataType == "MGT":
             mgt_extractor.exract_mgt(folder_path, directoryPath)
        else:
             print("An ERROR has occured with task selection")
        print("\n")
    else:
        navigate.is_empty(folder_path)
else:
       navigate.locate(directoryPath, folder_path)
       navigate.not_found(folder_path)

       

