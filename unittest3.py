from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest
import re
import random
class TestWikipedia(unittest.TestCase):
    bsObj = None
    url = None
    def test_PageProperties(self):
        global bsObj
        global url
        url = "https://blog.csdn.net/serverke/article/details/108140525"
        # 测试遇到的前100个页面
        for i in range(1, 10):
            bsObj = BeautifulSoup(urlopen(url))
            titles = self.titleMatchesURL()
            self.assertEquals(titles[0], titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLink()
        print("Done!")
        
    def titleMatchesURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find("a", {"class":"follow-nickName"}).attrs["href"]
        print(pageTitle)
        pageTitle = pageTitle[(pageTitle.index("csdn.net/")+9):]
        urlTitle = url[(url.index("csdn.net/")+9):url.index("article/")-1]
        return [pageTitle, urlTitle]
    
    def contentExists(self):
        global bsObj
        content = bsObj.find("div",{"id":"article_content"})
        if content is not None:
            return True
        return False
    
    def getNextLink(self):
        #使用第5章介绍的方法返回随机链接
        links = bsObj.findAll("a", href=re.compile("^(https://blog.csdn.net/).*/article/details/.*$"))
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        return newArticle

if __name__ == '__main__':
    unittest.main()