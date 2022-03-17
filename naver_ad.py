import time, os, hashlib, hmac, base64, urllib3, json
from bs4 import BeautifulSoup

import requests as rq

from pprint import pprint 
from date import get_date_yyyymmdd, get_date_yyyy_mm_dd

urllib3.disable_warnings()

CUSTOMER_ID = os.environ.get('CUSTOMER_ID', '')
API_KEY = os.environ.get('API_KEY', '')
SECRET_KEY = os.environ.get('SECRET_KEY', '')

NAVER_LAB_CLIENT_ID = os.environ.get('NAVER_LAB_CLIENT_ID', '')
NAVER_LAB_SECRET = os.environ.get('CLIENT_SECRET', '')

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
# FIXME: 크롤링 베이스
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

# NANER DATALAB
# https://developers.naver.com/apps
# FIXME: 오픈 API 베이스
def datalabSearchByApi(keyword, start_date, end_date, device):
  payload = {
    "keywordGroups" : [
      {
        "groupName": keyword,
        "keywords": [keyword]
      }
    ],
    "startDate" : start_date,
    "endDate" : end_date,
    "timeUnit" : 'date',
    'device': device == 'mobile' and 'mo' or 'pc' # pc: 'pc', mobile: 'mo'
  }

  headers = {
    "X-Naver-Client-Id": NAVER_LAB_CLIENT_ID,
    "X-Naver-Client-Secret": NAVER_LAB_SECRET,
    "Content-Type": "application/json"
  }

  res = rq.post(
    'https://openapi.naver.com/v1/datalab/search', 
    headers=headers, 
    data=json.dumps(payload),
    verify=False,
  )

  return res.json()["results"]


if __name__ == "__main__":
  keyword = 'LFMALL'
  device = 'mo'
  # r = search(keyword)
  # print(r)
  d = get_date_yyyymmdd()

  # print(d['day0'])
  # print(d['day1'])
  # print(d['day30'])
  print(f"검색 키워드: {keyword}, 검색기간: {d['day30']} ~ {d['day1']}")
  
  pprint(dataLabSearchByCrawler(keyword, d['day30'], d['day1'], device))
 
  d = get_date_yyyy_mm_dd()
  pprint(datalabSearchByApi(keyword, d['day30'], d['day1'], device))
