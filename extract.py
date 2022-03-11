from connect import Connect

def extract_db():
  print('\n[EXTRACT] 네이버 API 호출을 위한 데이터를 오라클에서 가져옵니다.')
  oracleSql = f"""
    SELECT distinct KEYWORD FROM KW_API_NV
  """
  
  rows = []

  with Connect() as connect:
    cursor = connect.cursor()
    cursor.execute(oracleSql)
    rows = [i[0] for i in cursor]
  
  print(f'[EXTRACT] 네이버 호출에 사용될 키워드는 {len(rows)}개 입니다.\n')
  return rows
  
def extract_test():
  print('\n[EXTRACT] 네이버 API 호출을 위한 데이터를 임시 데이터를 사용합니다.')
  
  rows =['LFMALL', '반팔티스타일링']
  
  print(f'[EXTRACT] 네이버 호출에 사용될 키워드는 {len(rows)}개 입니다.\n')
  
  return ['LFMALL', '반팔티스타일링']

if __name__ == "__main__":
  print(extract_db())
  print(extract_test())