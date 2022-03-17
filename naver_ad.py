import time, os, hashlib, hmac, base64, urllib3, json
from bs4 import BeautifulSoup

import requests as rq
from date import get_date

urllib3.disable_warnings()

CUSTOMER_ID = os.environ.get('CUSTOMER_ID', '')
API_KEY = os.environ.get('API_KEY', '')
SECRET_KEY = os.environ.get('SECRET_KEY', '')

if not CUSTOMER_ID or not API_KEY or not SECRET_KEY:
  print('[ERROR] naver api키 설정이 되있지 않습니다.')

def generate_signature(timestamp, method, path, secret_key):
  message = f"{timestamp}.{method}.{path}"
  hash = hmac.new(bytes(secret_key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)
  hash.hexdigest()

  return base64.b64encode(hash.digest())

def _get_header(method, path):
  timestamp = str(round(time.time() * 1000))
  signature = generate_signature(
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
# http://naver.github.io/searchad-apidoc/#/operations/GET/~2Fkeywordstool
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
 
  data = res.json()['keywordList'][0]
  
  return data

# NANER DATALAB 
# https://datalab.naver.com/keyword/trendResult.naver
# TODO: 크롤링 베이스
def dataLabSearchByCrawler(keyword, start_date, end_date, device):
  BASE_URL = 'https://datalab.naver.com'
  path = '/qcHash.naver'
  headers = {
    'referer': 'https://datalab.naver.com/keyword/trendResult.naver',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'PostmanRuntime/7.29.0'
  }
  payload = {
    "queryGroups" : f'{keyword}__SZLIG__{keyword}',
    "startDate" : str(start_date),
    "endDate" : str(end_date),
    "timeUnit" : 'date',
    'device': device # pc: 'pc', mobile: 'mobile', all: ''
  }

  res = rq.post(f'{BASE_URL}{path}', verify=False, headers=headers, data=payload)
  hashKey = res.json().get('hashKey')
  url = f'https://datalab.naver.com/keyword/trendResult.naver?hashKey={hashKey}'
  
  res = rq.get(
    url, 
    headers=headers,
    verify=False,
  )

  soup = BeautifulSoup(res.content, 'html.parser')
  data = soup.find(id='graph_data').text
  d = json.loads(data)

  return d

if __name__ == "__main__":
  r = search('python')
  print(r)
  d = get_date()

  print(d['day0'])
  print(d['day1'])
  print(d['day30'])
  print(dataLabSearchByCrawler('LFMALL', d['day0'], d['day30']))
