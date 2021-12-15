from os import path, walk, listdir
import shutil

project = 'my_project3'

try:
    for root, dirs, files in walk(project):
        if 'templates' in dirs and root != project:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entry), path.join(project, 'templates', entry))
except FileExistsError:
    print("Уже есть!")