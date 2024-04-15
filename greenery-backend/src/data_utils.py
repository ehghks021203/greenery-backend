import os
import sys
sys.path.append(os.path.dirname(os.path.abspath('')))
import config
import json
import shutil
import numpy as np
from sklearn.model_selection import train_test_split
from PIL import Image
import cv2

def list_dir(path: str) -> list:
    return [x for x in os.listdir(os.path.join(path))]

def copy_files(src, dest):
    files = list_dir(src)
    for f in files:
        shutil.copy(os.path.join(src, f), os.path.join(dest, f))

def create_folders(path):
    train_path = os.path.join(path, "train")
    valid_path = os.path.join(path, "valid")
    test_path = os.path.join(path, "test")
    if not os.path.isdir(train_path):
        os.makedirs(os.path.join(train_path, "images"))
        os.makedirs(os.path.join(train_path, "labels"))
    if not os.path.isdir(valid_path):
        os.makedirs(os.path.join(valid_path, "images"))
        os.makedirs(os.path.join(valid_path, "labels"))
    if not os.path.isdir(test_path):
        os.makedirs(os.path.join(test_path, "images"))
        os.makedirs(os.path.join(test_path, "labels"))

def delete_folders(path):
    train_path = os.path.join(path, "train")
    valid_path = os.path.join(path, "valid")
    test_path = os.path.join(path, "test")
    if os.path.isdir(train_path):
        shutil.rmtree(train_path)
    if os.path.isdir(valid_path):
        shutil.rmtree(valid_path)
    if os.path.isdir(test_path):
        shutil.rmtree(test_path)

def copy_by_dirs(origin_path, path, dir, files):
    img_path = os.path.join(path, dir, 'images')
    lbl_path = os.path.join(path, dir, 'labels')
    for f in files:
        txtfile = f.split('.')[0] + '.txt'
        shutil.copy(os.path.join(origin_path, "images", f), os.path.join(img_path, f))
        shutil.copy(os.path.join(origin_path, "labels", txtfile), os.path.join(lbl_path, txtfile))


