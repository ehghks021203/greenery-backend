## **Config File 내용**
```
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = ""

    # set server encoding style
    JSON_AS_ASCII = False

    # etc.
    DEBUG = True

class Server:
    SERVER_DOMAIN = "my.server.domain.com"
    SERVER_PORT = "5000"

class Data:
    RAW_DATA_PATH = "/MY_RAW_DATA_PATH/"
    PREP_DATA_PATH = "/MY_PREP_DATA_PATH/"
    DATASET_PATH = "/MY_DATASET_PATH/"
    BREAK_POINT_PATH = "./.data_break_point.bp"
    IMAGE_SIZE = (1080,1080)

class YOLO:
    MODEL_PATH = "/yolo/model/path/model.pt"
    PRED_IMG_SAVE_PATH = "./app/static"
    PRED_IMG_PATH = "./app/static/test1.jpg"
    IMG_SIZE = (480,640)
    

class Chatbot:
    SYSTEM_PROMPT = f"""
        너는 재활용 전문가로 활동하고 있어.
        나는 어떤 물건에 대해 분리 수거 방법에 대해 질문을 할거고 너는 분리 수거 방법을 알려주면 돼.
        질문의 형태는 '통조림캔의 배출 방법에 대해 알려줘'와 같이 할거고 너는 이에 대한 대답을 하면 되는데 첫 문장은 '통조림캔의 배출 방법에 대해 알려드리겠습니다.'로 시작해야 해.
        모든 대화는 50자 이내로 해줘.

        그리고 존댓말로 친절하게 대답해줘.

        분리배출과 관련된 질문이 아니라면 답변해주지 말고, '저는 분리 배출 방법을 안내해주는 챗봇이에요. 분리 배출과 관련된 질문을 해주세요.'라고 대답해.
    """
    OPENAI_KEY = ""
    MODEL = "gpt-4"
```