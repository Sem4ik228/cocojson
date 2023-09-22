import os
import sys
import json
import shutil


dir = 'unzipped'

counter = 0

for i in os.listdir(dir):
    js_path = os.path.join(dir, i, 'annotations', 'instances_default.json')
    js = json.load(open(js_path))
    os.makedirs(f"dataset/{i}", exist_ok = True)
    os.makedirs(f"dataset/{i}/images", exist_ok = True)
    os.makedirs(f"dataset/{i}/annotations", exist_ok = True)
    img_folder_path = os.path.join(dir, i, 'images')
    for j in os.listdir(img_folder_path):

        old_path = os.path.join(img_folder_path, j)
        new_path = os.path.join(f'dataset/{i}/images', str(counter)+'.jpg')

        shutil.copy2(old_path, new_path)
        for k in range(len(js['images'])):
            
            if js['images'][k]['file_name'] == j:
                
                js['images'][k]['file_name'] = str(counter)+'.jpg'
                print(str(counter)+'.jpg')
                break

        counter+=1
    json.dump(js, open(os.path.join(f"dataset/{i}/annotations", 'instances_default.json'), 'w+'))
        
        


#json.dump(json.load(open('unzipped/task_accident_gazel2-2023_07_12_08_55_23-coco 1.0/annotations/instances_default.json')), open('res_jsons/res.json', 'w+'))



    #os.system(f"python merge.py {res_json} {path} {res_json}")