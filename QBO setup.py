__author__ = 'volodymyr'


# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class QBOAccountSetup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://qbo.intuit.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_q_b_o_account_setup(self):
        driver = self.driver
        driver.get(self.base_url + "/app/homepage")
        x = 84 # remove this line when doing real setup
        ##### Logging in
        driver.find_element_by_id("login").send_keys("vlad.adds" + str(x) + "@gmail.com")
        driver.find_element_by_id("password").send_keys("revelup1")
        driver.find_element_by_id("LoginButton").click()

        ##### Creating Location
        driver.find_element_by_id("dijit__TemplatedMixin_4").click()
        driver.find_element_by_link_text("All Lists").click()
        driver.find_element_by_link_text("Locations").click()
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='row']/div[1]/input").click()
        driver.find_element_by_xpath("//div[@class='row']/div[1]/input").send_keys("Location")
        driver.find_element_by_xpath("//button[text()='Save']").click()

        ##### Creating Payments
        driver.find_element_by_id("dijit__TemplatedMixin_4").click()
        driver.find_element_by_link_text("All Lists").click()
        driver.find_element_by_link_text("Payment Methods").click()
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys("Visa Payment")
        driver.find_element_by_xpath("//div[@class='form']/div[3]/input").click()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys(Keys.RETURN)
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys("MC Payment")
        driver.find_element_by_xpath("//div[@class='form']/div[3]/input").click()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys(Keys.RETURN)
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys("AmEx Payment")
        driver.find_element_by_xpath("//div[@class='form']/div[3]/input").click()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys(Keys.RETURN)
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys("Discover Payment")
        driver.find_element_by_xpath("//div[@class='form']/div[3]/input").click()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys(Keys.RETURN)
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys("Debit Payment")
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys(Keys.RETURN)
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys("Gift Card Payment")
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys(Keys.RETURN)
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys("Other Payment")
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys(Keys.RETURN)
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys("Payout")
        driver.find_element_by_xpath("//div[@class='form']/div[@class='row']/div[1]/input[1]").send_keys(Keys.RETURN)

        ##### Assertion of accounts
        driver.find_element_by_id("dijit__TemplatedMixin_4").click()
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "All Lists")))
        driver.find_element_by_link_text("All Lists").click()
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Chart of Accounts")))
        driver.find_element_by_link_text("Chart of Accounts").click()
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//tr/td/span[text()='Sales']")))

        try: self.assertEqual("Sales", driver.find_element_by_xpath("//tr/td/span[text()='Sales']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        print("Sales account exist")
        try: self.assertEqual("Supplies & Materials - COGS", driver.find_element_by_xpath("//tr/td/span[text()='Supplies & Materials - COGS']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        print("COGS account exist")
        try: self.assertEqual("Discounts", driver.find_element_by_xpath("//tr/td/span[text()='Discounts']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        print("Discount account exist")


        ##### Creation of required accounts

        #Assets Account
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//span[text()='Accounts receivable (A/R)']").click()
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='dijit_form_Select_0_dropdown']/table/tbody/tr/td[text()='Other Current Assets']")))
        driver.find_element_by_xpath("//div[@id='dijit_form_Select_0_dropdown']/table/tbody/tr/td[text()='Other Current Assets']").click()
        driver.find_element_by_xpath("//select/option[text()='Other Current Assets']").click()
        driver.find_element_by_xpath("//div[@class='tableCell main-column']/div[1]/div[1]/div[@class='row']/div[1]/input[1]").click()
        driver.find_element_by_xpath("//div[@class='tableCell main-column']/div[1]/div[1]/div[@class='row']/div[1]/input[1]").send_keys("Assets Account")
        driver.find_element_by_xpath("//div[@class='tableCell main-column']/div[1]/div[1]/div[@class='row']/div[1]/input[1]").click()
        driver.find_element_by_xpath("//button[@data-qbo-id='save']").click()
        print("Assets Account created")

        #Liability Account
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//span[text()='Accounts receivable (A/R)']").click()
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='dijit_form_Select_0_dropdown']/table/tbody/tr/td[text()='Other Current Liabilities']")))
        driver.find_element_by_xpath("//div[@id='dijit_form_Select_0_dropdown']/table/tbody/tr/td[text()='Other Current Liabilities']").click()
        driver.find_element_by_xpath("//select/option[text()='Other Current Liabilities']").click()
        driver.find_element_by_xpath("//div[@class='tableCell main-column']/div[1]/div[1]/div[@class='row']/div[1]/input[1]").click()
        driver.find_element_by_xpath("//div[@class='tableCell main-column']/div[1]/div[1]/div[@class='row']/div[1]/input[1]").send_keys("Liabilities Account")
        driver.find_element_by_xpath("//div[@class='tableCell main-column']/div[1]/div[1]/div[@class='row']/div[1]/input[1]").click()
        driver.find_element_by_xpath("//button[@data-qbo-id='save']").click()
        print("Liability Account created")

        #Account Payable
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//span[text()='Accounts receivable (A/R)']").click()
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='dijit_form_Select_0_dropdown']/table/tbody/tr/td[text()='Accounts payable (A/P)']")))
        driver.find_element_by_xpath("//div[@id='dijit_form_Select_0_dropdown']/table/tbody/tr/td[text()='Accounts payable (A/P)']").click()
        driver.find_element_by_xpath("//select/option[text()='Accounts Payable (A/P)']").click()
        driver.find_element_by_xpath("//div[@class='tableCell main-column']/div[1]/div[1]/div[@class='row']/div[1]/input[1]").click()
        driver.find_element_by_xpath("//div[@class='tableCell main-column']/div[1]/div[1]/div[@class='row']/div[1]/input[1]").send_keys("Accounts Payable")
        driver.find_element_by_xpath("//div[@class='tableCell main-column']/div[1]/div[1]/div[@class='row']/div[1]/input[1]").click()
        driver.find_element_by_xpath("//button[@data-qbo-id='save']").click()
        print("Account Payable created")

        try: self.assertEqual("Accounts Payable", driver.find_element_by_xpath("//tr/td/span[text()='Accounts Payable']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        print("Accounts Payable account exist")

        #Creating nesessary items
        driver.find_element_by_id("dijit__TemplatedMixin_4").click()
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "All Lists")))
        driver.find_element_by_link_text("All Lists").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Products and Services')])[2]").click()

        # Creating Short
        driver.refresh()
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").send_keys("Short")
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//button[@data-qbo-id='save']").click()
        print("Short item is created")

        #Creating Item Discount
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").send_keys("Item Discount")
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='row salesAccountIdPane']/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//div[@class='row salesAccountIdPane']/div[1]/input[1]").send_keys("Discounts")
        driver.find_element_by_xpath("//div[@class='row salesAccountIdPane']/div[1]/input[1]").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//button[@data-qbo-id='save']").click()
        print("Item Discount item is created")


        # Creating Order Discount
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").send_keys("Order Discount")
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='row salesAccountIdPane']/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//div[@class='row salesAccountIdPane']/div[1]/input[1]").send_keys("Discounts")
        driver.find_element_by_xpath("//div[@class='row salesAccountIdPane']/div[1]/input[1]").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//button[@data-qbo-id='save']").click()
        print("Order Discount item is created")

        #Creating Employee Service
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").send_keys("Employee Service")
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//button[@data-qbo-id='save']").click()
        print("Employee Service item is created")

        # Creating Rounding Delta
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").send_keys("Rounding Delta")
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//button[@data-qbo-id='save']").click()
        print("Rounding Delta item is created")

        # Creating Discount Refund
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").send_keys("Discount Refund")
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='row salesAccountIdPane']/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//div[@class='row salesAccountIdPane']/div[1]/input[1]").send_keys("Discounts")
        driver.find_element_by_xpath("//div[@class='row salesAccountIdPane']/div[1]/input[1]").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//button[@data-qbo-id='save']").click()
        print("Discount Refund item is created")

        # Creating Surcharge
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").send_keys("Surcharge")
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//button[@data-qbo-id='save']").click()
        print("Surcharge item is created")

        #Creating Service Charge
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").send_keys("Service Charge")
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//button[@data-qbo-id='save']").click()
        print("Service Charge item is created")

        # Creating Coupon Discount
        driver.find_element_by_css_selector("button.button.primary").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").send_keys("Coupon Discount")
        driver.find_element_by_xpath("//div[@class='tableCell nameCell']/div/input[@name='name']").click()
        driver.find_element_by_xpath("//div[@class='row salesAccountIdPane']/div[1]/input[1]").clear()
        driver.find_element_by_xpath("//div[@class='row salesAccountIdPane']/div[1]/input[1]").send_keys("Discounts")
        driver.find_element_by_xpath("//div[@class='row salesAccountIdPane']/div[1]/input[1]").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//button[@data-qbo-id='save']").click()
        print("Coupon Discount item is created")

        #### Enabling Payroll
        # driver.find_element_by_xpath("//span[text()='Employees']").click()
        # driver.find_element_by_link_text("Get started with payroll").click()
        # driver.find_element_by_id("priorPayrolls:haveHistoryx:_0").click()
        # driver.find_element_by_link_text("Continue").click()
        # driver.find_element_by_link_text("Continue").click()

        #### Check if Inventory, Payroll is enabled
        driver.find_element_by_id("dijit__TemplatedMixin_4").click()
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Company Settings")))
        driver.find_element_by_link_text("Company Settings").click()
        driver.find_element_by_link_text("Sales").click()
        driver.find_element_by_xpath("//div[text()='Products and services']").click()
        driver.find_element_by_xpath("//input[@data-qbo-bind='checked: trackQuantityOnHand, visible:!readSalesItems']").click()
        driver.find_element_by_xpath("(//div[@class='tableCell settingContent']/button[text()='Save'])[9]").click()
        driver.find_element_by_xpath("//button[text()='OK']").click()
        print("Inventory is turned on")

        #### Check anything else that should be enabled
        driver.find_element_by_link_text("Expenses").click()
        driver.find_element_by_xpath("(//div[text()='Purchase orders'])[2]").click()
        driver.find_element_by_xpath("//input[@data-qbo-bind='checked: hasPurchaseOrder, visible:!readPurchaseOrder']").click()
        driver.find_element_by_xpath("(//div[@class='tableCell settingContent tracking settingSpacer']/button[text()='Save'])[2]").click()
        # driver.find_element_by_xpath("//button[text()='OK']").click()
        print("Purchase Orders are turned on")


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
