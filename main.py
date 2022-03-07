import json


def main():
    json_origin = 'aachen_000000_000019_gtCoarse_polygons.json'
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
        new_content['imagePath']=json_origin
        new_content['imageData']=""
        new_content["imageHeight"]=origin_content['imgHeight']
        new_content["imageWidth"]=origin_content['imgWidth']
    with open('new.json','w+') as f:

        json.dump(new_content,f)

if __name__ == "__main__":
    main()
