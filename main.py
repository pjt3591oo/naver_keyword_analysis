import signaturehelper
import requests as rq
import time, os

CUSTOMER_ID = os.environ['CUSTOMER_ID']
API_KEY = os.environ['API_KEY']
SECRET_KEY = os.environ['SECRET_KEY']

BASE_URL = "https://api.naver.com"

def get_header(method, path):
  timestamp = str(round(time.time() * 1000))
  signature = signaturehelper.Signature.generate(
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

if __name__ == "__main__":
  path = '/keywordstool'
  headers = get_header('GET', path)
  res = rq.get(
    f"{BASE_URL}{path}", 
    headers=headers, 
    verify=False,
    params = {
      "hintKeywords": "python"
    }
  )
  
  data = res.json()['keywordList'][0]
  print(f"keyword: {data['relKeyword']}, Pc: { data['monthlyPcQcCnt']}, Mobile: {data['monthlyMobileQcCnt']}")