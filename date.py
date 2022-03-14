from datetime import datetime, timedelta

def get_date(format='%Y%m%d'):
  today = datetime.now()
  day0  = today - timedelta(days=0)
  day1  = today - timedelta(days=1)
  day30 = today - timedelta(days=30)
  
  return {
    'day0': day0.strftime(format),
    'day1': day1.strftime(format),
    'day30': day30.strftime(format)
  }