import os
import shutil


def organize_folder(folder_path):

    files = os.listdir(folder_path)

    for file in files:

        file_path = os.path.join(folder_path, file)

        if not os.path.isfile(file_path):
            continue

        name, extension = os.path.splitext(file)

        extension = extension.lower()

        if extension in [".jpg", ".png", ".jpeg"]:
            folder_name = "Images"

        elif extension == ".pdf":
            folder_name = "PDFs"

        elif extension in [".mp4", ".mkv"]:
            folder_name = "Videos"

        elif extension in [".mp3", ".wav"]:
            folder_name = "Music"

        else:
            folder_name = "Others"

        target_folder = os.path.join(folder_path, folder_name)

        os.makedirs(target_folder, exist_ok=True)

        shutil.move(
            file_path,
            os.path.join(target_folder, file)
        )