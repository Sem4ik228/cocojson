import shutil
import os
dir = 'dataset'

for i in os.listdir(dir):
    dir_path = os.path.join(dir, i, 'images')
    for j in os.listdir(dir_path):
        old_path = os.path.join(dir_path, j)
        new_path = os.path.join('images', j)
        shutil.copy2(old_path, new_path)
