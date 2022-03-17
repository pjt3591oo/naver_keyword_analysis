
import unittest
from naver_ad import generate_signature

class TestNaverAd(unittest.TestCase):

  def test_sigunature(self):
    sigunature = generate_signature(
      1647306472521,   # timestamp
      'GET',           # method
      '/keywordstool', # path
      'a'              # SECRET_KEY
    )
    self.assertEqual(
      sigunature,
      b'c5WP4jkgmRUyqXfgQoBdqlflu5LqhHkqIrUtfNsslf8='
    )

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