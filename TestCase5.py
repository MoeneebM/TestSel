#-------------------------------------------------------------------------------
# Name:        TestCase 5
# Purpose:
#
# Author:      Moeneeb Mosaval
#
# Created:     12/06/2021
# Copyright:   (c) Moeneeb Mosaval 2021
# Licence:     None
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
           command_executor='http://ec2-3-134-243-110.us-east-2.compute.amazonaws.com:4444/wd/hub',
           desired_capabilities={'browserName': 'firefox'})
           #desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})

    def sign_in_to_offerzen(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.offerzen.com/"
        driver.get(self.base_url)
        driver.find_element_by_link_text("Sign in").click()
        sign_ = driver.find_element_by_css_selector("h2").text
        print (sign_)


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
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()