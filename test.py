#-*- coding: utf-8 -*-
import os, urllib3, json
import ssl
import requests as rq

ssl._create_default_https_context = ssl._create_unverified_context

context = ssl._create_unverified_context()

NAVER_LAB_CLIENT_ID = os.environ.get('NAVER_LAB_CLIENT_ID', '')
NAVER_LAB_SECRET = os.environ.get('CLIENT_SECRET', '')

import urllib.request
client_id = NAVER_LAB_CLIENT_ID 
client_secret = NAVER_LAB_SECRET
url = "https://openapi.naver.com/v1/datalab/search";
body = "{\"startDate\":\"2017-01-01\",\"endDate\":\"2017-04-30\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"한글\",\"keywords\":[\"한글\",\"korean\"]},{\"groupName\":\"영어\",\"keywords\":[\"영어\",\"english\"]}],\"device\":\"pc\"}";

body = json.dumps({
  "startDate": "2017-01-01",
  "endDate": "2017-04-30",
  "timeUnit": "month",
  "keywordGroups": [{
    "groupName": "LFMALL",
    "keywords": ["LFMALL"]
  }],
  'device': 'pc'
})
print(body)
# print(body.encode("utf-8"))
# print()
# print(json.loads(body))
# print()
# print(json.dumps(json.loads(body)))
# body = json.dumps(json.loads(body))
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

headers = {
  "X-Naver-Client-Id": NAVER_LAB_CLIENT_ID,
  "X-Naver-Client-Secret": NAVER_LAB_SECRET,
  "Content-Type": "application/json"
}
print(headers)
res = rq.post(
  url,
  data=json.loads(body),
  headers=headers,
  verify=False,
)

print(res.status_code)
print(res.json())