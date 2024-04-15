from flask import Blueprint, jsonify, request
from YOLOPredict import predict
from config import YOLO

classification_routes = Blueprint("classification", __name__)

@classification_routes.route("/predict", methods=["GET", "POST"])
def _predict():
    return_value = []
    # load & save file
    f = request.files["file"]
    f.save(YOLO.PRED_IMG_PATH)

    # predict
    results = predict(YOLO.PRED_IMG_PATH)
    for result in results:
        for i in result.boxes.cls.tolist():
            if "{" in result.names[int(i)]:
                fmt_str = result.names[int(i)].split("'")[1]
                return_value.append(fmt_str)
            else:
                return_value.append(result.names[int(i)])
    return jsonify({
        "result":"success", 
        "data":return_value
    }), 200