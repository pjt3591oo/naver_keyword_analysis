from naver_ad import search, dataLabSearch
from pprint import pprint

from date import get_date

def compare(rate, data):
  month_pc = rate['monthlyPcQcCnt'] # 날짜 조정이 안됨
  month_mobile = rate['monthlyMobileQcCnt'] # 날짜 조정이 안됨

  total = sum([item['value'] for item in data])

  for item in data:
    item['day_pc_click'] = item['value'] / total * month_pc
    item['day_mobile_click'] = item['value'] / total * month_mobile

  return data

if __name__ == '__main__':
  keyword = 'LFMALL'
  rate= search(keyword)
  date = get_date()
  data = dataLabSearch(keyword, date['day30'], date['day1'])[0]['data']
  rst = compare(rate, data)
  
  print(rst)
