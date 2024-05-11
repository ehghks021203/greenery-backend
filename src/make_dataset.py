import os
import sys
import json
sys.path.append(os.path.dirname(os.path.abspath('')))
from config import Data
from src import data_utils
from src.data_preprocessing import data_preprocessing

def load_breakpoint() -> dict:
    if os.path.isfile(Data.BREAK_POINT_PATH):
        with open(Data.BREAK_POINT_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    else:
        return {"total_count":0, "data":{}}

def save_breakpoint(bp, main, sub=None, dir=None):
    if not sub and not dir:
        bp[main]["complete"] = 1
    elif not dir:
        bp[main][sub]["complete"] = 1
    else:
        bp[main][sub][dir]["complete"] = 1

    with open(Data.BREAK_POINT_PATH, "w", encoding="utf-8") as f:
        json.dump(bp, f, ensure_ascii=False)

if __name__ == "__main__":
    # Check is exist raw data directory
    if os.path.isdir(Data.RAW_DATA_PATH):
        if not os.path.isdir(os.path.join(Data.RAW_DATA_PATH, "images")) or not os.path.isdir(os.path.join(Data.RAW_DATA_PATH, "labels")):
            print("\n\n!! ERROR: not exist 'images' or 'labels' directory in raw data path.\n")
            sys.exit()
    else:
        print("\n\n!! ERROR: not exist raw data directory.\n")
        sys.exit()

    if os.path.isdir(Data.PREP_DATA_PATH):
        if not os.path.isdir(os.path.join(Data.PREP_DATA_PATH, "images")):
            os.makedirs(os.path.join(Data.PREP_DATA_PATH, "images"))
        if not os.path.isdir(os.path.join(Data.PREP_DATA_PATH, "labels")):
            os.makedirs(os.path.join(Data.PREP_DATA_PATH, "labels"))
    else:
        print("\n\n!! ERROR: not exist prep data directory.\n")
        sys.exit()

    if not os.path.isdir(Data.DATASET_PATH):
        os.makedirs(Data.DATASET_PATH)
        print("### Create Dataset directory...")
    
    # Load break point & Category data
    print("### Load break point data...")
    bp = load_breakpoint()

    data_dict = {}
    category_dict = {}
    category_index = 0
    total_data_count = 0
    for main in data_utils.list_dir(os.path.join(Data.RAW_DATA_PATH, "images")):
        data_dict[main] = []
        for sub in data_utils.list_dir(os.path.join(Data.RAW_DATA_PATH, "images", main)):
            data_dict[main].append(sub)
            category_dict[main + ">" + sub] = category_index
            category_index += 1
    
    # Make data.yaml file
    if not os.path.isfile(os.path.join(Data.DATASET_PATH, "data.yaml")):
        print("### Make data.yaml file...")
        data_str = "train: ../train/images\nval: ../valid/images\ntest: ../test/images\n\nnc: {}\nnames: [\n".format(len(category_dict.keys()))
        for k, v in category_dict.items():
            data_str += "  \"{}\",\n".format(k)
        data_str = data_str[:-1] + "\n]\n"
        with open(os.path.join(Data.DATASET_PATH, "data.yaml"), "w", encoding="utf-8") as f:
            f.write(data_str)

    for k, v in category_dict.items():
        print(k, v)

    # Data preprocessing
    print("### Start data preprocessing...")
    print("path: {}".format(Data.PREP_DATA_PATH))
    for main in data_dict.keys():
        if main in bp and bp[main]["complete"] == 1:
            continue
        if not main in bp:
            bp[main] = {"complete":0}

        for sub in data_dict[main]:
            if sub in bp[main] and bp[main][sub]["complete"] == 1:
                continue
            if not sub in bp[main]:
                bp[main][sub] = {"complete":0}
            
            for dir in data_utils.list_dir(os.path.join(Data.RAW_DATA_PATH, "images", main, sub)):
                if dir in bp[main][sub] and bp[main][sub][dir]["complete"] == 1:
                    continue
                if not dir in bp[main][sub]:
                    bp[main][sub][dir] = {"complete":0}

                for file in data_utils.list_dir(os.path.join(Data.RAW_DATA_PATH, "images", main, sub, dir)):
                    try:
                        img_path = os.path.join(Data.RAW_DATA_PATH, "images", main, sub, dir, file.split(".")[0] + ".jpg")
                        prep_img_path = os.path.join(Data.PREP_DATA_PATH, "images", file.split(".")[0] + ".jpg")
                        json_path = os.path.join(Data.RAW_DATA_PATH, "labels", main, sub, dir, file.split(".")[0] + ".Json")
                        prep_json_path = os.path.join(Data.PREP_DATA_PATH, "labels", file.split(".")[0] + ".txt")
                        if os.path.isfile(img_path) and os.path.isfile(json_path):
                            data_preprocessing(
                                path=img_path, 
                                new_path=prep_img_path,
                                json_path=json_path, 
                                new_json_path=prep_json_path, 
                                img_size=Data.IMAGE_SIZE,
                                category=category_dict
                            )
                            total_data_count += 1
                        elif not os.path.isfile(json_path):
                            print("!! ERROR: {} file is not exist.".format(os.path.isfile(json_path)))
                        
                        print("\rPREP COUNT: {:5d}".format(total_data_count), end="")
                    except Exception as e:
                        print(e)
                        sys.exit(-1)
                    #print(f)
                    break
                save_breakpoint(bp, main, sub, dir)
            save_breakpoint(bp, main, sub)
        save_breakpoint(bp, main)
