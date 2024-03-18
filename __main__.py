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
import atol_extractor
import mgt_extractor

absolute_path = os.path.abspath(__file__)
directoryPath = os.path.dirname(absolute_path)
welcome: str = 'Exellator says: Welcome. '
where: str = "You are currently working in the following folder: "
selection: str = "You selected: "
print(f'\n{welcome:>40}')
print(f'{where:>66}  {directoryPath}')
print("\n")


dataType = Prompt.ask('Enter the test for which you want to extract data. Default is: AToL.',
                        default='AToL',
                        choices=['MGT', 'exit'])
if dataType == "exit":
    atol_extractor.abort()

print(f'\n{selection:>30} {dataType}\n')

folder_path = os.path.join(directoryPath, "data", dataType)


#'\\data\\' + dataType

if os.path.isdir(folder_path):
    if  os.listdir(folder_path):
        print(f'\n You have selected to work in the following folder: {folder_path}')
        print("\n")
        if dataType == "AToL":
            atol_extractor.extract_atol(folder_path, directoryPath)
        elif dataType == "MGT":
             mgt_extractor.exract_mgt(folder_path, directoryPath)
        else:
             print("An ERROR has occured with task selection")
        print("\n")
    else:
        print("\n\tEMPTY DIRECTORY: The folder \"" + folder_path + "\" is empty.\n" )
else:
       print("Dir " + directoryPath)
       print("\n")
       print("Path " + folder_path)
       print("\n\tNOT FOUND: There is no folder named \"" + folder_path + "\" in the current directory. Please check folder and try again.\n")

