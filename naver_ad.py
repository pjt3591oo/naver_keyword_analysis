import requests as rq
import time, os, hashlib, hmac, base64

import urllib3
urllib3.disable_warnings()

CUSTOMER_ID = os.environ['CUSTOMER_ID']
API_KEY = os.environ['API_KEY']
SECRET_KEY = os.environ['SECRET_KEY']

BASE_URL = "https://api.naver.com"

def _generate(timestamp, method, path, secret_key):
  message = f"{timestamp}.{method}.{path}"
  hash = hmac.new(bytes(secret_key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)
  hash.hexdigest()

  return base64.b64encode(hash.digest())

def _get_header(method, path):
  timestamp = str(round(time.time() * 1000))
  signature = _generate(
    timestamp, 
    method, 
    path, 
    SECRET_KEY
  )

  return {
    'Content-Type': 'application/json; charset=UTF-8',
    'X-Timestamp': timestamp,
    'X-API-KEY': API_KEY,
    'X-Customer': str(CUSTOMER_ID),
    'X-Signature': signature
  }

def search(keyword):
  
  path = '/keywordstool'
  headers = _get_header('GET', path)
  res = rq.get(
    f"{BASE_URL}{path}", 
    headers=headers, 
    verify=False,
    params = {
      "hintKeywords": keyword
    }
  )

  print(f'[API 결과] HTTP 응답코드: {res.status_code}, API: 키워드 검색: {keyword}') 
  data = res.json()['keywordList'][0]
  
  return data

if __name__ == "__main__":
  print(search("python"))