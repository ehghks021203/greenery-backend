import os
import sys
import shutil
from sklearn.model_selection import train_test_split
sys.path.append(os.path.dirname(os.path.abspath('')))
from config import Data
import src.data_utils as data_utils


def distribute_files(img_path, label_path):
    images = [x for x in os.listdir(img_path)]
    labels = [x for x in os.listdir(label_path)]

    print("### Start split train test valid dataset...")
    print("# images dataset count: {:6d}".format(len(images)))
    print("# labels dataset count: {:6d}".format(len(labels)))
    
    train_X, test_X, train_y, test_y = train_test_split(images, labels, test_size=0.1, random_state=42, shuffle=True)
    train_X, valid_X, train_y, valid_y = train_test_split(train_X, train_y, test_size=0.1, random_state=42, shuffle=True)
    all_files = {'train': train_X, 'valid': valid_X, 'test': test_X}
    
    progress = 0
    print("\rPROGRESS: {:5d}/{:5d}".format(progress, len(images)), end="")
    for dir, file_list in all_files.items():
        img_path = os.path.join(Data.DATASET_PATH, dir, 'images')
        lbl_path = os.path.join(Data.DATASET_PATH, dir, 'labels')
        for f in file_list:
            txtfile = f.split('.')[0] + '.txt'
            shutil.copy(os.path.join(Data.PREP_DATA_PATH, "images", f), os.path.join(img_path, f))
            shutil.copy(os.path.join(Data.PREP_DATA_PATH, "labels", txtfile), os.path.join(lbl_path, txtfile))
            progress += 1
            print("\rPROGRESS: {:5d}/{:5d}".format(progress, len(images)), end="")
    print("\n### SUCCESS !!!")
    print("## train: {:5d}\n## valid: {:5d}\n## test: {:5d}".format(len(all_files["train"]), len(all_files["valid"]), len(all_files["test"])))

if __name__ == "__main__":
    # Delete existing folder
    data_utils.delete_folders(Data.DATASET_PATH)

    # Create Datasets Folder
    data_utils.create_folders(Data.DATASET_PATH)
    
    # split preprocessing dataset(train, valid, test)
    distribute_files(os.path.join(Data.PREP_DATA_PATH, "images"), os.path.join(Data.PREP_DATA_PATH, "labels"))