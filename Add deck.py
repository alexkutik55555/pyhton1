# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://sentence-mining.dev.icemint.org/login")
        driver.find_element_by_name("login").click()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("alexku")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("12345678")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text("Decks").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log Out'])[1]/following::button[1]").click()
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("QQQQ")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create new deck'])[2]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Spanish'])[2]/following::div[7]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Spanish'])[5]/following::div[13]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Spanish'])[1]/following::div[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='German'])[3]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Download'])[1]/following::div[1]").click()
        driver.find_element_by_link_text("Log Out").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
