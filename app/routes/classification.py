import os
import sys
import string
import random
from flask import Blueprint, jsonify, request
sys.path.append(os.path.dirname(os.path.abspath('')))
from YOLOPredict import predict
from config import YOLO

classification_routes = Blueprint("classification", __name__)

@classification_routes.route("/predict", methods=["POST"])
def pred():
    return_value = []
    random_file_name = "predict_" + "".join(random.sample(string.ascii_letters, 10)) + ".jpg"
    # load & save file
    f = request.files["file"]
    f.save(YOLO.PRED_IMG_PATH + random_file_name)

    # predict
    results = predict(YOLO.PRED_IMG_PATH + random_file_name)
    for result in results:
        for i in result.boxes.cls.tolist():
            if "{" in result.names[int(i)]:
                fmt_str = result.names[int(i)].split("'")[1]
                return_value.append(fmt_str)
            else:
                return_value.append(result.names[int(i)])
    os.remove(YOLO.PRED_IMG_PATH + random_file_name)
    if len(return_value) == 0:
        return_value.append("undefined")
    return jsonify({
        "result":"success", 
        "data":return_value
    }), 200