from ultralytics import YOLO
import opencv_jupyter_ui as jcv2
from config import YOLO as YOLOConfig
import yaml


def predict(path):
    # load yaml
    #with open("/home/students/cs/greenery/prep_datas/data.yaml") as f:
    #    film = yaml.load(f, Loader=yaml.FullLoader)

    # Load a model
    model = YOLO(YOLOConfig.MODEL_PATH)  # pretrained YOLOv8n models

    """
    for idx, name in enumerate(film["names"]):
        model.names[idx] = ""
        model.names[idx] = name
        print(model.names[idx])
    """

    # Run batched inference on a list of images
    results = model(
        [path],
        save=True,
        conf=0.6,
        project=YOLOConfig.PRED_IMG_SAVE_PATH
    )  # return a list of Results objects
    return results

if __name__ == "__main__":
    results = predict(YOLOConfig.PRED_IMG_PATH)
