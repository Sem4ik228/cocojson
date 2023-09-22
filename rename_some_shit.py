import json
import os

jso = 'unzipped/task_bus2-2023_06_08_08_44_36-coco1.0/annotations/instances_default.json'

imgs = 'unzipped/task_bus2-2023_06_08_08_44_36-coco1.0/images'

js = json.load(open(jso))

for i in range(len(js['images'])):
    src = js['images'][i]['file_name'][-9:]
    for im in os.listdir(imgs):
        if src==im[-9:]:
            js['images'][i]['file_name'] = js['images'][i]['file_name'][-9:]
            print(js['images'][i]['file_name'])
            os.rename(os.path.join(imgs, im), os.path.join(imgs, im[-9:]))
            break
json.dump(js, open(jso, 'w+'))

