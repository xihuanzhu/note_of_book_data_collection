from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest
class TestWikipedia(unittest.TestCase):
    bsObj = None
    def setUpClass():
        global bsObj
        url = "https://blog.csdn.net/serverke/article/details/108140525"
        bsObj = BeautifulSoup(urlopen(url))
        
    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find("h1").get_text()
        self.assertEqual("kaggle比赛前2%摸奖银牌总结", pageTitle)
        
    def test_contentExists(self):
        global bsObj
        content = bsObj.find("div",{"id":"article_content"})
        self.assertIsNotNone(content)
        
if __name__ == '__main__':
 unittest.main()