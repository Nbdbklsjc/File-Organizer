import os, shutil

def f
ile_organizer(directory):
    for file in os.listdir(directory):
        ext = file.split(".")[-1]
        folder = os.path.join(directory, ext)
        if not os.path.exists(folder): os.makedirs(folder)
        shutil.move(os.path.join(directory, file), os.path.join(folder, file))
