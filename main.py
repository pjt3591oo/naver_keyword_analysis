from PyInquirer import prompt

from extract import extract_db, extract_test
from loader import loader_db, loader_print

from cli import style, questions

from naver_ad import search

import time

class KeywordAPI():
  def __init__(self, extractor, loader):
    self.extractor = extractor
    self.loader = loader

  def __call__(self):
    search_keywords = self.extractor()
    rst = []

    # 너무 빠르게 API를 호출하면 429에러 발생
    for keyword in search_keywords:
      rst.append(search(keyword))
      time.sleep(0.5)

    loader_print(rst)

if __name__ == "__main__":
  answers = prompt(questions, style=style)
  extract = extract_test
  loader = loader_print
  
  if answers['extract'] == 'oracle':
    extract = extract_db
  if answers['loader'] == 'oracle':
    loader = loader_db

  keyword_api = KeywordAPI(
    extract, 
    loader
  )
  keyword_api()
  