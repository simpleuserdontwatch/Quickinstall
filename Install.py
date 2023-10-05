import os
import sys
drive = sys.argv[1]
seven_zip_path = sys.argv[2]
install_wim_path = sys.argv[3]
drive = sys.argv[1]
print('Preparing to install windows')
os.system(f'format {drive}: /Q /Y')
print('Unpacking install.wim file')
command = f'{seven_zip_path} x -o{drive}: {install_wim_path}'
os.system(command)
print('Creating boot files')
os.system('bcdboot {drive}: /s {drive}: /f ALL')
input("Done! You may close the command prompt now")
