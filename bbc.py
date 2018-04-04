# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
	self.driver = webdriver.Firefox(executable_path='/var/lib/jenkins/workspace/first_app/geckodriver')
	
    	
        
    def test_search_in_python_org(self):
    	driver = self.driver
    	driver.get("http://www.bbc.com/")
    	elem = driver.find_element_by_id("orb-search-q")
    	elem.clear()
    	elem.send_keys("Coral")
    	elem.send_keys(Keys.RETURN)
    	assert "Coral Products" not in driver.page_source

    def tearDown(self):
    	self.driver.close()

if __name__ == "__main__":
	unittest.main()