from connect import Connect

def loader_db(row):
  print('\n[LOADER] 네이버 API 호출 결과를 오라클에 저장합니다.')

  oracleSql = f"""
    SELECT distinct KEYWORD FROM KW_API_NV
  """
  
  rows = []

  with Connect() as connect:
    cursor = connect.cursor()
    cursor.execute(oracleSql)
  
def loader_print(dataset):
  print('\n[LOADER] 네이버 API 호출 결과를 화면에 출력만 합니다.')
  
  for i in dataset:
    print(i)

if __name__ == "__main__":
  loader_db()