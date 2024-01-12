# 요청 url
# https://openapi.naver.com/v1/papago/n2mt
# client id: HdQp_E5iqki6avh4oBIY
# client secret: naP6GBV0ud

import urllib.request
import json

client_id = "HdQp_E5iqki6avh4oBIY"
client_secret = "naP6GBV0ud"

encoding_text = urllib.parse.quote("동준아 보고싶어, 사랑해! 조심히 다녀와서 토요일에 만나자!")
data = f"source=ko&target=en&text={encoding_text}"
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)

# -H(Header)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if rescode == 200:
    response = json.loads(response.read().decode("utf-8"))
    print(response['message']['result']['translatedText'])
