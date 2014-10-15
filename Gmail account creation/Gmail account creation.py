__author__ = 'volodymyr'

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.remote.webelement import WebElement
from const import x


class GMailAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://accounts.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_g_mail_account(self):
        driver = self.driver
        driver.get(self.base_url + "/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1")
        driver.find_element_by_id("link-signup").click()
        driver.find_element_by_id("FirstName").clear()
        driver.find_element_by_id("FirstName").send_keys("Firstname")
        driver.find_element_by_id("LastName").clear()
        driver.find_element_by_id("LastName").send_keys("Lastname")
        driver.find_element_by_id("GmailAddress").clear()
        driver.find_element_by_id("GmailAddress").send_keys("vlad.adds"+str(x))
        print("Your email is vlad.adds" + str(x) + "@gmail.com")
        driver.find_element_by_id("Passwd").click()
        driver.find_element_by_id("Passwd").clear()
        driver.find_element_by_id("Passwd").send_keys("revelup1")
        driver.find_element_by_id("PasswdAgain").clear()
        driver.find_element_by_id("PasswdAgain").send_keys("revelup1")
        driver.find_element_by_xpath("//span[@id='BirthMonth']/div[1]").click()
        driver.find_element_by_xpath("//div[text()='January']").click()
        driver.find_element_by_id("BirthDay").clear()
        driver.find_element_by_id("BirthDay").send_keys("1")
        driver.find_element_by_id("BirthYear").clear()
        driver.find_element_by_id("BirthYear").send_keys("1990")
        driver.find_element_by_xpath("//div[@id='Gender']/div[1]").click()
        driver.find_element_by_xpath("//div[text()='Male']").click()
        driver.find_element_by_id("RecoveryPhoneNumber").clear()
        driver.find_element_by_id("RecoveryPhoneNumber").send_keys("9168351247")
        driver.find_element_by_id("RecoveryEmailAddress").clear()
        driver.find_element_by_id("RecoveryEmailAddress").send_keys("vlad.adds1@gmail.com")
        driver.find_element_by_id("recaptcha_response_field").clear()
        time.sleep(5)
        driver.find_element_by_id("TermsOfService").click()
        time.sleep(1)
        driver.find_element_by_id("submitbutton").click()
        time.sleep(5)
        driver.find_element_by_id("next-button").click()
        print("All done.")
        time.sleep(100)



        # driver.find_element_by_id("submitbutton").click()
        # driver.find_element_by_id("close-button").click()

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
