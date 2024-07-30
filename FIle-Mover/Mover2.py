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
            # Get the file name and extension
            file_name, file_ext = os.path.splitext(filename)
            # Move the file to the destination directory
            count = 1
            while True:
                new_filename = f"{file_name}_{count}{file_ext}"
                new_file_path = os.path.join(destination_dir, new_filename)
                if not os.path.exists(new_file_path):
                    shutil.move(file_path, new_file_path)
                    break
                count += 1

print("Files moved and renamed successfully!")