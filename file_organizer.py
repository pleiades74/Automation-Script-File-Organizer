import os
import shutil

FOLDER_PATH = "path/to/your/folder"

for filename in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, filename)
    if os.path.isfile(file_path):
        ext = filename.split(".")[-1]
        folder = os.path.join(FOLDER_PATH, ext)
        os.makedirs(folder, exist_ok=True)
        shutil.move(file_path, os.path.join(folder, filename))

print("Files organized by extension!")
