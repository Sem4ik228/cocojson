import os
import shutil
import json

counter = 0

rrr = os.listdir('jsons_dir')
al_images = 0
al_annotations = 0
al_images_annotations = 0

for i in rrr:
    path = os.path.join('jsons_dir', i)
    #print(al_images)
    #print(al_annotations)
    #print(al_images_annotations)
    js = json.load(open(path))
    #l_images = len(js['images'])
    #l_annotations = len(js['annotations'])
    an = set()
    im = set()
    #im_an = set()
    for a in js['annotations']:
        an.add(a['id'])
    for a in js['images']:
        im.add(a['id'])

        
    #max_im_an = max(im_an)
    max_im = max(im)
    max_an = max(an)
    for j in range(max_an):
        js['annotations'][j]['image_id']+=al_images_annotations
    for j in range(max_im):
        js['images'][j]['id']+=al_images
    for j in range(max_an):
        js['annotations'][j]['id']+=al_annotations    
    al_images_annotations+=max_im
    al_images+=max_im
    al_annotations+=max_an

    an = set()
    im = set()
    im_an = set()
    for a in js['annotations']:
        an.add(a['id'])
        im_an.add(a['image_id'])
    for a in js['images']:
        im.add(a['id'])

    counter+=1



    print(len(an), len(im_an), len(im))
    print(max(an), max(im_an), max(im))
    json.dump(js, open(path, 'w'))
    #print(l_images, l_annotations)

    #shutil.copy2(path, )
    #os.remove(os.path.join(path, 'annotations'))