import os
import shutil

SOURCE_FOLDER = "test_folder"

FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"]
}

for filename in os.listdir(SOURCE_FOLDER):
    file_path = os.path.join(SOURCE_FOLDER, filename)

    if os.path.isfile(file_path):
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                os.makedirs(folder, exist_ok=True)
                shutil.move(file_path, os.path.join(folder, filename))
                moved = True
                break

        if not moved:
            os.makedirs("Others", exist_ok=True)
            shutil.move(file_path, os.path.join("Others", filename))

print("Files organized successfully!")
