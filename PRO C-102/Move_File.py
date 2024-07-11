
import os
import shutil

# Define source and destination directories
from_dir = "/path/to/Downloads"
to_dir = "/path/to/Document_Files"

# Get list of all files in the source directory
list_of_files = os.listdir(from_dir)
print(list_of_files)

# Loop through the list of files
for file_name in list_of_files:
    # Get the file name and extension
    name, extension = os.path.splitext(file_name)

    # If the file has no extension, skip it
    if extension == '':
        continue

    # If the file is a document file, move it to the Document_Files directory
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name

        # Check if the destination directory exists
        if os.path.exists(path2):
            print(f"Moving {file_name}...")
            shutil.move(path1, path3)
        else:
            # Make the destination directory and move the file
            os.makedirs(path2)
            print(f"Moving {file_name}...")
            shutil.move(path1, path3)