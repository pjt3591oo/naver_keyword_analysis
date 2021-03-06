from naver_ad import search, dataLabSearchByCrawler
from date import get_date_yyyymmdd
from pprint import pprint


def compare(month_rate, data):

  total = sum([item['value'] for item in data])

  for item in data:
    item['day_click'] = item['value'] / total * month_rate

  return data

if __name__ == '__main__':
  keyword = 'LFMALL'
  device_pc = 'pc'
  device_mobile = 'mo'

  rate= search(keyword)

  date = get_date_yyyymmdd()
  pc_data = dataLabSearchByCrawler(keyword, date['day30'], date['day1'], device_pc)[0]['data']
  mobile_data = dataLabSearchByCrawler(keyword, date['day30'], date['day1'], device_mobile)[0]['data']
  
  print(pc_data)  
  
  rst_pc = compare(rate['monthlyPcQcCnt'], pc_data)
  rst_mobile = compare(rate['monthlyMobileQcCnt'], mobile_data)
  
  pprint(rst_pc)
  print()
  pprint(rst_mobile)
