from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import unittest
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options

        options = Options()
        service = Service(ChromeDriverManager().install())

        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_login_correct_credentials(self):
        driver = self.driver
        driver.get("https://www.yourlearningpal.com/login")

        driver.find_element(By.ID, "txtUser").clear()
        driver.find_element(By.ID, "txtUser").send_keys("test1")

        driver.find_element(By.ID, "txtPassword").clear()
        driver.find_element(By.ID, "txtPassword").send_keys("Test12456")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        page_text = driver.find_element(By.TAG_NAME, "body").text
        self.assertTrue(
            "Course Selection" in page_text or "Dashboard" in page_text
        )

    def test_login_incorrect_credentials(self):
        driver = self.driver
        driver.get("https://www.yourlearningpal.com/login")

        driver.find_element(By.ID, "txtUser").clear()
        driver.find_element(By.ID, "txtUser").send_keys("test1")

        driver.find_element(By.ID, "txtPassword").clear()
        driver.find_element(By.ID, "txtPassword").send_keys("wrongpassword123")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        page_text = driver.find_element(By.TAG_NAME, "body").text
        self.assertTrue(
            "Invalid" in page_text or "incorrect" in page_text or "Error" in page_text
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()