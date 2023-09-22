import os
import json
import shutil

dir = 'dataset'

counter = 0

for i in os.listdir(dir):
    js_path = os.path.join(f"dataset/{i}/annotations", 'instances_default.json')
    shutil.copy2(js_path, os.path.join('jsons_dir', i+'.json'))
    
    #json.dump(js, open(os.path.join(f"dataset/{i}/annotations", 'instances_default.json'), 'w+'))
        