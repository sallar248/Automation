import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):

class SearchText(unittest.TestCase):
    def setUp(self):
    # create a new Firefox session
    self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(30)
    self.driver.maximize_window()
    # navigate to the application home page
    self.driver.get("http://www.google.com/")

