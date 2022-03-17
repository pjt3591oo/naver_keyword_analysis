from datetime import datetime, timedelta

def get_date_yyyymmdd(format='%Y%m%d'):
  today = datetime.now()
  day0  = today - timedelta(days=0)
  day1  = today - timedelta(days=1)
  day30 = today - timedelta(days=30)
  
  return {
    'day0': day0.strftime(format),
    'day1': day1.strftime(format),
    'day30': day30.strftime(format)
  }

def get_date_yyyy_mm_dd(format='%Y-%m-%d'):
  today = datetime.now()
  day0  = today - timedelta(days=0)
  day1  = today - timedelta(days=1)
  day30 = today - timedelta(days=30)
  
  return {
    'day0': day0.strftime(format),
    'day1': day1.strftime(format),
    'day30': day30.strftime(format)
  }

