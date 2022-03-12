from naver_ad import search, dataLabSearch
from pprint import pprint

if __name__ == '__main__':
  keyword = 'python'
  r = search(keyword)

  month = r['monthlyPcQcCnt'] # 날짜 조정이 안됨

  # keyword: python
  # naver data lab result
  # data = [{'period': '20220301', 'value': 29.94011}, {'period': '20220302', 'value': 81.82207}, {'period': '20220303', 'value': 99.27288}, {'period': '20220304', 'value': 80.83832}, {'period': '20220305', 'value': 39.56372}, {'period': '20220306', 'value': 44.48246}, {'period': '20220307', 'value': 99.74337}, {'period': '20220308', 'value': 100.0}, {'period': '20220309', 'value': 42.00171}, {'period': '20220310', 'value': 85.88537}, {'period': '20220311', 'value': 73.43883}]
  data = dataLabSearch(keyword)[0]['data']
  
  total = sum([item['value'] for item in data])
  for item in data:
    item['day_click'] = item['value'] / total * month
  
  pprint(data)
  print(r)
