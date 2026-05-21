import os
import shutil

folder_path = "/Users/apple/Desktop/test_files"

file_types = {
    "Images": [".jpg", ".png"],
    "PDFs": [".pdf"],
    "Documents": [".txt"]
}

files = os.listdir("/Users/apple/Desktop/test_files")

for file_name in files:

    full_path = os.path.join(folder_path, file_name)

    if os.path.isfile(full_path):

        extension = os.path.splitext(file_name)[1].lower()

        for folder, extensions in file_types.items():

            if extension in extensions:

                new_folder = os.path.join(folder_path, folder)

                os.makedirs(new_folder, exist_ok=True)

                shutil.move(
                    full_path,
                    os.path.join(new_folder, file_name)
                )

                print("Moved:", file_name)