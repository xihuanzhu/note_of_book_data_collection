from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
import unittest
import time
class TestAddition(unittest.TestCase):
    driver = None
    def setUp(self):
        global driver
        driver = webdriver.PhantomJS(executable_path=r'F:\software\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        url = 'http://pythonscraping.com/pages/javascript/draggableDemo.html'
        driver.get(url)
        
    def tearDown(self):
        print("Tearing down the test")
        
    def test_drag(self):
        global driver
        element = driver.find_element_by_id("draggable")
        target = driver.find_element_by_id("div2")
        actions = ActionChains(driver)
        actions.drag_and_drop(element, target).perform()
        time.sleep(10)
        self.assertEqual("You are definitelynot a bot!", driver.find_element_by_id("message").text)
        
if __name__ == '__main__':
    unittest.main()