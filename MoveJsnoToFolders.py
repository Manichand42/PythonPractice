from datetime import datetime
import pandas as pd
import os
import shutil

def read_excel_create_folders_move_files(excel_file, sheet_name, folder_column, file_column, destination_folder):
    # Read data from Excel
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    folder_data = df[folder_column].tolist()
    file_data = df[file_column].tolist()

    # Create folders and move files
    for folder, file in zip(folder_data, file_data):
        folder_path = os.path.join(destination_folder, str(folder))
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            #print(f"Folder '{folder_path}' created.")

        json_file = os.path.join(source_folder, file + '.json')
        if os.path.exists(json_file):
            destination_file = os.path.join(folder_path, file + '.json')
            shutil.move(json_file, destination_file)
        else:
            print(f"{folder} : File '{file}.json' does not exist.")


       

# Example usage
excel_file = 'C:\Apps\TablesList\OCA\PVOLists.xlsx'
column_name = 'PVO Name'
source_folder = 'C:\InputFiles\\23B\ALL'
destination_folder = 'C:\outputFiles'
folder_column = 'module'
xls = pd.ExcelFile(excel_file)
sheet_names = xls.sheet_names
# Print sheet names
print ('-----------------------------------------')
for sheet_name in sheet_names:
    if sheet_name in ('HCM','COM','HCSC','FIN','FISC','SCM'):
        read_excel_create_folders_move_files(excel_file, sheet_name, folder_column, column_name, destination_folder)
# Read data from Excel
print ('-----------------------------------------')
