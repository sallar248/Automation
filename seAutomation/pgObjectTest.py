#!/usr/bin/python

import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

def setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):

# Load the main page
    main_page = page.MainPage(self.driver)

# Checks if the word "python" is in title
    assert main_page.is_title_matches(), 
    main_page.search_text_element = "pycon"
    main_page.click_go_button()
    search_results_page = page.SearchResultsPage(self.driver)
    # Verify that the rsults page is not empty
    assert search_results_page.is_results_found(), 

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()    


