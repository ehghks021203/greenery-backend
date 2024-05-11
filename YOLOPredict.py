from ultralytics import YOLO
import opencv_jupyter_ui as jcv2
from config import YOLO as YOLOConfig
import yaml


def predict(path):
    # Load a model
    model = YOLO(YOLOConfig.MODEL_PATH)  # pretrained YOLOv8n models

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
