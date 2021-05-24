# cocojson

Utility scripts for COCO json annotation format

## Install

`cocojson` package can be installed through `pip3 install -e .` (editable install) or `pip3 install .`

## Usage

### Utility Tools

#### Merge

Merges multiple datasets in coco json format

Expected format of 1 x Dataset:
- 1 x json file 
- 1 x Image Folder (to get to the image, path is assumed to be "Image Folder"/"file_name" given in json)

Merged Dataset:
- 1 x json file (image's "file_name" will be subpaths, for eg, "Image Folder from DatasetA/image01.png")
- Master Images Folder 
    - Image Folder from DatasetA
    - Image Folder from DatasetA
    - ...

Only given category IDs for each dataset will be merged. Merged category list will merge constituent categories based on category name.

```python
python3 -m cocojson.merge_coco -h
```

```
usage: merge_coco.py [-h] -j JSON -r ROOT -c CIDS [CIDS ...] -o OUTPUT [--outname OUTNAME]

optional arguments:
  -h, --help            show this help message and exit
  -j JSON, --json JSON  path to coco json
  -r ROOT, --root ROOT  path to root image directory
  -c CIDS [CIDS ...], --cids CIDS [CIDS ...]
                        category ids to merge
  -o OUTPUT, --output OUTPUT
                        path to output directory
  --outname OUTNAME     name of output json (default: "merged")

Typical usage: merge_coco.py \ 
-j <path_to_coco_json_1> -r <path_to_images_1>  -c 1 \ 
-j <path_to_coco_json_2> -r <path_to_images_2> -c 1 2 \ 
-j <path_to_coco_json_3> -r <path_to_images_3> -c 1 2 \ 
-o <path_to_output_dataset>
Categories will be merged by category name
```

#### Sample

```python
python3 -m cocojson.sample_coco
```

```
usage: sample_coco.py [-h] [--k K] json imgroot outdir

positional arguments:
  json        Path to coco json
  imgroot     Path to img root
  outdir      Path to output dir

optional arguments:
  -h, --help  show this help message and exit
  --k K       Random k images to extract
```

### Converters

#### CVAT XML to COCO

##### CVAT Image XML

TODO

##### CVAT Video XML

TODO

#### COCO to Darknet

TODO
