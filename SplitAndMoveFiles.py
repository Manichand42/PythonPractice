import os
import shutil

# Source directory containing the files to split and copy
source_directory = 'C:\\23B_Shipped'

# Destination directory where individual folders will be created
destination_directory = 'C:\\Split'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Initialize counter
counter = 0
folder_counter = 1

# Iterate over each file in the source directory
for filename in os.listdir(source_directory):
    # Calculate the full path of the source file
    source_file = os.path.join(source_directory, filename)
    
    # Create a new folder every 10 files
    if counter == 0:
        folder_name = f"folder_{folder_counter}"
        folder_path = os.path.join(destination_directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        folder_counter += 1
    
    # Calculate the full path of the destination file within the created folder
    destination_file = os.path.join(folder_path, filename)
    
    # Copy the source file to the destination folder
    shutil.move(source_file, destination_file)
    
    # Increment the counters
    counter += 1
    
    print(f"File '{filename}' copied to folder '{folder_name}'")
    
    # Reset the counter after 10 files
    if counter == 50:
        counter = 0