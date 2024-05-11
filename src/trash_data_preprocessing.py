from PyKakao import Local
import os
import sys
import pandas as pd
sys.path.append(os.path.dirname(os.path.abspath('')))

from config import Kakao, BASE_DIR

FILE_NAME = "trash_place_data"
FILE_EXTENSION = ".csv"

print(f"## Load file to: {BASE_DIR}/data/{FILE_NAME}{FILE_EXTENSION}")
data = pd.read_csv(BASE_DIR + "/data/trash_place_data.csv")
new_data = pd.DataFrame(columns=["id", "addr", "lat", "lng", "place", "class", "type", "call_number"])
local = Local(service_key=Kakao.API_KEY)

idx = 0
for i in range(len(data)):
    sa = local.search_address(data["addr"][i])
    if len(sa["documents"]) == 0:
        print(f"\r!! ERROR: data not exist (addr: {data['addr'][i]})")
        continue

    addr = sa["documents"][0]["address_name"]
    lat = sa["documents"][0]["y"]
    lng = sa["documents"][0]["x"]
    new_data.loc[i] = [idx, addr, lat, lng, data["place"][i], data["class"][i], data["type"][i], data["call"][i]]
    print(f"\r# Data preprocessing: {i+1:4d}/{len(data):4d}", end="")
    idx += 1
new_data.to_csv(BASE_DIR + "/data/prep_" + FILE_NAME + FILE_EXTENSION, header=True, index=False)
print(f"## Data Preprocessing end!")
print(f"## File saved to: {BASE_DIR}/data/prep_{FILE_NAME}{FILE_EXTENSION}")
