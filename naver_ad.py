import time, os, hashlib, hmac, base64, urllib3, json
from bs4 import BeautifulSoup

import requests as rq


urllib3.disable_warnings()

CUSTOMER_ID = os.environ.get('CUSTOMER_ID', '')
API_KEY = os.environ.get('API_KEY', '')
SECRET_KEY = os.environ.get('SECRET_KEY', '')

if CUSTOMER_ID or API_KEY or SECRET_KEY:
  print('[ERROR] naver api키 설정이 되있지 않습니다.')

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

# NAVER SEARCH AD API
def search(keyword):
  BASE_URL = "https://api.naver.com"
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
  print(res.json())
  data = res.json()['keywordList'][0]
  
  return data

# NANER DATALAB 

def dataLabSearch(keyword):
  BASE_URL = 'https://datalab.naver.com'
  path = '/qcHash.naver'
  headers = {
    'referer': 'https://datalab.naver.com/keyword/trendResult.naver',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'PostmanRuntime/7.29.0'
  }
  payload = {
    "queryGroups" : '파이썬__SZLIG__파이썬',
    "startDate" : '20220301',
    "endDate" : '20220312',
    "timeUnit" : 'date',
    'device': 'pc'
  }
  res = rq.post(f'{BASE_URL}{path}', headers=headers, data=payload)
  hashKey = res.json().get('hashKey')
  print(hashKey)
  url = f'https://datalab.naver.com/keyword/trendResult.naver?hashKey={hashKey}'
  print(url)
  res = rq.get(url, headers=headers)
  soup = BeautifulSoup(res.content, 'html.parser')
  data = soup.find(id='graph_data').text
  d = json.loads(data)
  return d

if __name__ == "__main__":
  # print(search("python"))
  print(dataLabSearch('LFMALL'))