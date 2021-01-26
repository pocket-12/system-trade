# OSに依存する操作をするのに必要なモジュール(ファイル・フォルダ操作)
import os

# JSON形式のデータを扱うのに必要なモジュール
import json

# Webサイトから情報を収集するのに使うモジュール
import requests

# APIのURL
API_URL = "http://localhost:18080/kabusapi"
# APIを使用する際のパスワード
API_PASSWORD = os.environ["API_PASSWORD"]

# APIの利用にはトークンを取得する必要がある　
# トークンを取得する関数
def get_token():

    URL = API_URL + "/token"

    headers = {"content-type": "applicaiton/json"}
    payload = {"APIPassword": API_PASSWORD}

    try:
        response = requests.post(URL, data = json.dumps(payload).encode("utf8"),headers=headers)
   
    except Exception as e:
        print(e)

    return json.loads(response.text).get("Token")


# 価格情報を取得する関数
def get_price(token):

    symbol = "9483"
    exchange = "1"
    URL = API_URL + "/board/" + symbol + "@" + exchange

    headers = {
        "content-type": "application/json",
        "X-API-KEY": token
    }

    try:
        response = requests.get(URL, headers = headers)
    except Exception as e:
        print(e)

    return json.loads(response.text).get("CurrentPrice")


