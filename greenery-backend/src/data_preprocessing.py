import json
import numpy as np
from PIL import Image
import cv2

def resize_bbox(image: Image, resized_image: Image, json_file: str, img_size: tuple, category: dict) -> list:
    with open(json_file, 'r', encoding='utf-8') as j_f:
        data = json.load(j_f)
    bbox_resized_list = []
    for i in range(len(data["Bounding"])):
        if data["Bounding"][i]["Drawing"] == "BOX":
            category_str = str(data["Bounding"][i]["CLASS"]) + ">" + str(data["Bounding"][i]["DETAILS"])
            if not category_str in category.keys():
                print("\n\n!! ERROR: {} does not exist in category!".format(category_str))
                print("file path: {}\n".format(json_file))
                # sys.exit(-1)
                return None
            type = category[category_str]
            y_ratio = resized_image.shape[0] / image.shape[0]
            x_ratio = resized_image.shape[1] / image.shape[1]
            x1 = float(data["Bounding"][i]["x1"])*x_ratio
            y1 = float(data["Bounding"][i]["y1"])*y_ratio
            x2 = float(data["Bounding"][i]["x2"])*x_ratio
            y2 = float(data["Bounding"][i]["y2"])*y_ratio
            bnd_width = round((x2-x1)/img_size[0],6)
            bnd_height = round((y2-y1)/img_size[1],6)
            x_center = round((x2+x1)/2/img_size[0],6)
            y_center = round((y2+y1)/2/img_size[1],6)
            
            bbox_resized = [type, x_center, y_center, bnd_width, bnd_height]
            bbox_resized_list.append(bbox_resized)
    return bbox_resized_list

def write_txt(path, bbox_resized):
    if bbox_resized != []:
        with open(path, "w", encoding="utf-8") as f:
            str = ""
            for bbox in bbox_resized:
                str += f"{bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]} {bbox[4]}\n"
            f.write(str)
        return True
    else:
        return False 

def data_preprocessing(path: str, new_path: str, json_path: str, new_json_path: str, img_size: tuple, category: dict) -> None:
    img = Image.open(path)
    img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    resized_img = cv2.resize(img, dsize=(img_size), interpolation=cv2.INTER_LINEAR)
    bbox_resized = resize_bbox(img, resized_img, json_path, img_size, category)
    if bbox_resized == None:
        return
    elif write_txt(new_json_path, bbox_resized):
        cv2.imwrite(new_path, resized_img)
    