# Greenery (data preprocessing & backend)

> More info about project: [Greenery](https://github.com/bkk21/Greenery)

## **Dataset**
- AI Hub \
    생활 폐기물 이미지 [Link](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=140)

<br/>

## **Environment**
GPU : Nvidia Quadro RTX 5000 * 2\
OS  : Ubuntu 22.04 LTS\
CUDA 12.1\
PyTorch 2.1.1

<br/>

## **Project Organization**
```
├── app
│   ├── routes
│   │   ├── __init__.py
│   │   ├── chatbot.py
│   │   └── classification.py
│   ├── static
│   │   └── predict    <= predict result(jpg)
│   └── __init__.py
├── result
│   └── separate_model
│       └── predict    <= predict result(jpg)
├── src
│   ├── chatbot.py
│   ├── data_preprocessing.py
│   ├── data_utils.py
│   ├── make_dataset.py
│   └── split_dataset.py
├── .data_break_point.bp
├── config.py
├── README.md
├── run.py
└── YOLOPredict.py
```
### **Project codes**
- 데이터 전처리 코드

    - make_dataset.py\
    원천데이터에서 YOLO 학습용 데이터로 전처리 합니다.
    - split_dataset.py\
    전처리한 데이터를 학습, 검증, 테스트 데이터로 분할합니다.

- 백엔드(backend) 코드

    - run.py\
    백엔드 서버를 구동합니다.

코드를 실행하기 전 config.py의 내용을 변경해야 합니다.
_[config.py](CONFIG.md)_

### **Data preprocessing**

`make_dataset.py`를 실행하기 전에 전처리 데이터를 저장할 디렉토리를 생성해야 합니다.

```
python make_dataset.py
```

해당 작업은 꽤 많은 시간이 소요됩니다.

이후, 전처리 데이터를 train, valid, test 데이터셋으로 분할해줍니다.

```
python split_dataset.py
```

위 작업을 모두 끝마친 후 yolo v8 모델을 학습하면 됩니다.

<br/>

### **Running backend server**
```
python run.py
```

백엔드 서버를 구동하기 전 config.py의 Server 클래스 내용을 변경해주어야 합니다. 


## **Data Organization**
전처리가 끝난 후 데이터셋의 트리 구조는 아래와 같습니다:

```
├── datasets
│   └── data.yaml
├── prep_datas
│   ├── images
│   │   └── too many datas... (jpg)
│   └── labels
│       └── too many datas... (txt)
└── raw_datas
    ├── images
    │   ├── 의류
    │   │   ├── 기타
    │   │   ├── 상의
    │   │   ├── 하의
    │   │   ├── 외투
    │   │   ├── 레깅스
    │   │   ├── 면의류
    │   │   ├── 원피스
    │   │   ├── 합성섬유
    │   │   └── 기타의류
    │   ├── 나무
    │   │   ├── 기타
    │   │   ├── 주걱
    │   │   ├── 도마
    │   │   ├── 액자
    │   │   ├── 장식품
    │   │   ├── 포장재
    │   │   ├── 나무행거
    │   │   └── 주방용품
    │   ├── 도기류
    │   │   ├── 병
    │   │   ├── 컵
    │   │   ├── 받침
    │   │   ├── 기타
    │   │   ├── 화분
    │   │   ├── 주전자
    │   │   ├── 장식품
    │   │   ├── 그릇류
    │   │   ├── 항아리
    │   │   └── 뚝배기
    │   ├── 비닐류
    │   │   ├── 기타
    │   │   ├── 봉투
    │   │   ├── 에어캡
    │   │   ├── 포장제
    │   │   ├── 과자봉지
    │   │   ├── 리필용기
    │   │   └── 일회용덮개
    │   ├── 고철류
    │   │   ├── 기타
    │   │   ├── 고철
    │   │   ├── 주전자
    │   │   ├── 골프채
    │   │   ├── 철옷걸이
    │   │   ├── 비철금속
    │   │   ├── 프라이팬
    │   │   └── 전기프라이팬
    │   ├── 자전거
    │   │   ├── 두발자전거
    │   │   ├── 세발자전거
    │   │   └── 네발자전거
    │   ├── 가구류
    │   │   ├── 의자
    │   │   ├── 책상
    │   │   ├── 장롱
    │   │   ├── 소파
    │   │   ├── 협탁
    │   │   ├── 침대
    │   │   ├── 밥상
    │   │   ├── 화장대
    │   │   ├── 싱크대
    │   │   ├── 수납장
    │   │   └── 서랍장
    │   ├── 유리병
    │   │   ├── 기타
    │   │   ├── 물병
    │   │   ├── 소주병
    │   │   ├── 맥주병
    │   │   ├── 기타술병
    │   │   ├── 박카스병
    │   │   ├── 주방용기
    │   │   └── 음료수병
    │   ├── 스티로폼류
    │   │   ├── 보호재
    │   │   ├── 포장용기
    │   │   ├── 스티로폼
    │   │   └── 네모트레이
    │   └── 전자제품
    │   │   ├── 믹서
    │   │   ├── 오디오
    │   │   ├── 냉장고
    │   │   ├── 에어컨
    │   │   ├── 전기밥솥
    │   │   ├── 팩시밀리
    │   │   ├── 전기다리미
    │   │   ├── 전자레인지
    │   │   ├── 이동전화단말기
    │   │   ├── 기타
    │   │   ├── 가습기
    │   │   ├── 연수기
    │   │   ├── 복사기
    │   │   ├── 전기오븐
    │   │   ├── 공기청정기
    │   │   ├── 식기건조기
    │   │   ├── 음식물처리기
    │   │   ├── TV
    │   │   ├── 컴퓨터
    │   │   ├── 세탁기
    │   │   ├── 선풍기
    │   │   ├── 청소기
    │   │   ├── 전기히터
    │   │   ├── 자동판매기
    │   │   ├── 전기정수기
    │   │   └── 비디오플레이어
    └── labels
        └── images와 하위 디렉토리 내용 비슷

```

- 형광등 관련 데이터 이미지가 없어 아직 처리하지 못함
- 유리병과 스티로폼의 클래스 명이 "유리병류", "스티로폼류"로 구분되어 있어 폴더명을 바꿔주었음
