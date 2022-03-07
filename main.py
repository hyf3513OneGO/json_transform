import json
import os

raw_dir = "../datasets/before"

def json_convertor(filename):

    json_origin = os.path.join(raw_dir,filename)
    new_content = {}
    with open(json_origin, 'r') as f:
        new_content['version'] = '3.16.7'
        new_content['flags'] = {}
        shapes = []

        origin_content = json.load(f)
        for item in origin_content.get('objects'):
            if item['label'] == 'road':
                shapes.append({"label": "road", "line_color": None, "fill_color": None, "points": item['polygon']})
        new_content['shapes'] = shapes
        new_content['lineColor'] = [
            0,
            255,
            0,
            128
        ]
        new_content['fillColor'] = [
            255,
            0,
            0,
            128
        ]
        new_content['imagePath'] = json_origin
        new_content['imageData'] = raw_dir
        new_content["imageHeight"] = origin_content['imgHeight']
        new_content["imageWidth"] = origin_content['imgWidth']
    with open('new.json', 'w+') as f:

        json.dump(new_content, f)
def png_convertor(filename):
    pass
def main():
    files=os.listdir(raw_dir)
    json_files=[]
    png_files=[]

if __name__ == "__main__":
    main()
