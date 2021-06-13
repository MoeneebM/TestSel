#-------------------------------------------------------------------------------
# Name:        TestCase 4
# Purpose:
#
# Author:      Moeneeb
#
# Created:     12/06/2021
# Copyright:   (c) Moeneeb 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import xlrd

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
           command_executor='http://localhost:4444/wd/hub',
           desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})

    def sign_in_to_offerzen(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.offerzen.com/"
        driver.get(self.base_url)
        driver.find_element_by_link_text("Sign in").click()
        self.assertEqual("Sign In - OfferZen", driver.title)

    def create_reporitory(self):
        driver = self.driver
        pass


    def delete_repository(self):
        driver = self.driver
        pass

    def test_create_delete_repository(self):
        self.sign_in_to_offerzen()
        #self.create_reporitory()
       #self.delete_repository()

    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()