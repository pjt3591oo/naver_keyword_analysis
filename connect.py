import cx_Oracle, os

os.putenv('NLS_LANG', '.UTF8')

# 로컬에 설치된 libclntsh.dylib의 경로를 명시한다.
# 윈도우 C:\\Users\\${process.env.USERNAME}\\instantclient_19_10

LOCATION = f"/usr/local/lib"
cx_Oracle.init_oracle_client(lib_dir=LOCATION)

class Connect(object):
  def __init__(self):
    self.connect = cx_Oracle.connect(
      dsn=f"{os.environ['ORACLE_HOST']}/{os.environ['ORACLE_SID']}",
      user=f"{os.environ['ORACLE_USER']}", 
      password=f"{os.environ['ORACLE_PASSWORD']}"
    )

  def __enter__(self):
    print('enter')
    
    return self.connect
  
  def __exit__(self, type, value, trace_back):
    print('exit')
    self.connect.close()
