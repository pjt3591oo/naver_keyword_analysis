# import sys
# from os import path
# change_path = path.dirname( path.dirname( path.abspath(__file__) ) )
# print(change_path)
# sys.path.append(change_path)

import unittest

from naver_ad import generate_signature
# import ..naver_ad.generate_signature as generate_signature


# print(naver_ad)

class TestNaverAd(unittest.TestCase):

  def test_upper(self):
    # sigunature = generate_signature(
    #   1647306472521,   # timestamp
    #   'GET',           # method
    #   '/keywordstool', # path
    #   'a'              # SECRET_KEY
    # )
    # print(sigunature)
    self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
    self.assertTrue('FOO'.isupper())
    self.assertFalse('Foo'.isupper())

  def test_split(self):
    s = 'hello world'
    self.assertEqual(s.split(), ['hello', 'world'])
    # check that s.split fails when the separator is not a string
    with self.assertRaises(TypeError):
      s.split(2)

if __name__ == '__main__':
  unittest.main()

# from ../naver_ad import generate_signature

# sigunature = generate_signature(
#   1647306472521,   # timestamp
#   'GET',           # method
#   '/keywordstool', # path
#   'a'              # SECRET_KEY
# )
# print(sigunature)