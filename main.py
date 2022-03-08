import json
import os
import PIL
import numpy as np
from labelme.utils import img_arr_to_b64
import threading
import base64

raw_dir = "./dataset/before"
converted_path = "./dataset/converted"


def json_convertor(filename):
    json_origin = os.path.join(raw_dir, filename)
    image_name = filename.replace('_gtCoarse_polygons.json', '_leftImg8bit.png')
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
        try:
            img = PIL.Image.open(os.path.join(raw_dir, image_name))
            img_arr = np.array(img)
        except:
            print('err')
        new_content['imageData'] = str(img_arr_to_b64(img_arr), 'utf-8')
        new_content["imageHeight"] = origin_content['imgHeight']
        new_content["imageWidth"] = origin_content['imgWidth']
    print(filename)
    with open(os.path.join(converted_path, image_name.replace('.png', '.json')), 'w+') as f:
        json.dump(new_content, f)


def png_convertor():
    import os
    import shutil

    png_path = raw_dir  # png格式图片所在文件夹的路径
    jpg_path = converted_path  # jpg格式图片存放文件夹的路径
    file_walk = os.listdir(png_path)
    fileNum = 0  # png文件夹下所有文件个数计数
    png_fileNum = 0  # png文件夹下png图片个数计数

    for filePath in file_walk:
        fileNum += 1
        protion = os.path.splitext(filePath)

        if protion[1].lower() == '.png':  # 判断文件后缀是否为png
            if png_fileNum == 0:  # 当png文件夹中有png图片
                # 判断是否存在jpg文件夹，存在则清空文件夹，不存在就建立文件夹
                if os.path.exists(jpg_path):
                    shutil.rmtree(jpg_path)
                    os.mkdir(jpg_path)
                    print("jpg文件夹内原文件已清除")
                else:
                    os.mkdir(jpg_path)
                    print("jpg文件夹已创建")
            png_fileNum += 1
            print("正在处理：" + filePath)

            # 复制转存png图片为jpg格式到jpg文件夹中
            shutil.copyfile(os.path.join(png_path, filePath), os.path.join(jpg_path, protion[0] + '.jpg'))

    print('\n文件夹内共有' + str(fileNum) + '个文件，其中png格式文件有' + str(png_fileNum) + '个，已全部完成转换，存至jpg文件夹内')


def main():
    thread_list = []
    files = os.listdir(raw_dir)
    json_files = []
    png_files = []
    thread_png=threading.Thread(target=png_convertor)
    thread_list.append(thread_png)
    if not os.path.exists(converted_path):
        os.mkdir(converted_path)
    for item in files:
        if len(item.split('.')) == 2:
            if item.split('.')[1] == 'png':
                png_files.append(item)
            elif item.split('.')[1] == 'json':
                json_files.append(item)
                thread = threading.Thread(target=json_convertor, args=[item])
                thread.start()
                thread_list.append(thread)
    for thread in thread_list:
        thread.join()
    print('完成转换')


if __name__ == "__main__":
    main()
