import shutil
import os

# Define the source and destination directories
source_dir = '/temp1'
destination_dir = '/temp2'

# Iterate over all subdirectories in the source directory
for subdir in os.listdir(source_dir):
    subdir_path = os.path.join(source_dir, subdir)
    if os.path.isdir(subdir_path):
        # Iterate over all files in the subdirectory
        for filename in os.listdir(subdir_path):
            file_path = os.path.join(subdir_path, filename)
            # Move the file to the destination directory
            shutil.move(file_path, destination_dir)

print("Files moved successfully!")