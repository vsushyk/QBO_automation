__author__ = 'volodymyr'

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from random import randint
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Gmail.const import x


class QBOCreateAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://quickbooks.intuit.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_q_b_o_create_account(self):
        driver = self.driver
        driver.get(self.base_url + "/start/core_sui?bc=USP-TDN/")
        driver.find_element_by_id("userFirstName").clear()
        driver.find_element_by_id("userFirstName").send_keys("Firstname")
        driver.find_element_by_id("userLastName").clear()
        driver.find_element_by_id("userLastName").send_keys("Lastname")
        driver.find_element_by_id("userEmail").clear()
        print("x=" + str(x))
        driver.find_element_by_id("userEmail").send_keys("vlad.adds" + str(x) + "@gmail.com")
        driver.find_element_by_id("confirmUserEmail").clear()
        driver.find_element_by_id("confirmUserEmail").send_keys("vlad.adds" + str(x) + "@gmail.com")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("revelup1")
        driver.find_element_by_id("confirmUserPassword").clear()
        driver.find_element_by_id("confirmUserPassword").send_keys("revelup1")
        time.sleep(5)
        driver.find_element_by_id("newUserSubmitButton").click()
        time.sleep(5)
        driver.find_element_by_link_text("Continue to Trial").click()
        time.sleep(15)
        driver.find_element_by_id("uniqName_50_0").clear()
        driver.find_element_by_id("uniqName_50_0").send_keys("123 Street St")
        driver.find_element_by_id("uniqName_50_1").clear()
        driver.find_element_by_id("uniqName_50_1").send_keys("San Francisco")
        driver.find_element_by_id("uniqName_12_1").click()
        driver.find_element_by_id("dijit_MenuItem_19_text").click()
        driver.find_element_by_id("uniqName_50_3").clear()
        driver.find_element_by_id("uniqName_50_3").send_keys("94133")
        driver.find_element_by_id("uniqName_50_4").clear()
        driver.find_element_by_id("uniqName_50_4").send_keys("(415)888-7777")
        driver.find_element_by_xpath("//button[@class='primary']").click()
        driver.find_element_by_id("uniqName_48_0").clear()
        driver.find_element_by_id("uniqName_48_0").send_keys("Restaurant, Caterer, or Bar")
        driver.find_element_by_id("uniqName_48_0").send_keys(Keys.RETURN)
        driver.find_element_by_xpath("//form[@id='dijit_form_Form_1']/div[3]/div[1]/div[1]").click()
        driver.find_element_by_xpath('//td[text()="Products and services"]').click()
        driver.find_element_by_xpath("//form[@id='dijit_form_Form_1']/div[4]/div[1]/div[1]").click()
        driver.find_element_by_xpath('//td[text()="Sole proprietor"]').click()
        driver.find_element_by_xpath("//ul/li[1]/input[1]").click()
        driver.find_element_by_xpath("//ul/li[2]/input[1]").click()
        driver.find_element_by_xpath("//button[@class='primary']").click()
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "primary")))
        time.sleep(5)
        driver.find_element_by_xpath("//button[@class='primary']").click()
        print("QBO account successfully created. Your login is vlad.adds" + str(x) + "@gmail.com. And password is revelup1")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
