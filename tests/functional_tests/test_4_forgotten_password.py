import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_forgotten_password_path(self):

        # Check if Django is working
        self.browser.get('http://localhost:8000')
        self.browser.maximize_window()
        self.assertIn('Pur Beurre', self.browser.title)

        # Check if Visitor succeed to reach login page.
        login_page = self.browser.find_element_by_id('Connexion')
        login_page.click()
        time.sleep(3)

        # Find reset password link and click on it
        forgotten_password_link = self.browser.find_element_by_id('reset_password')
        forgotten_password_link.click()
        time.sleep(3)

        # Fill password_reset form with box id = "id_email"
        password2_box = self.browser.find_element_by_id('id_email')
        password2_box.send_keys('rati.lekishvili1@gmail.com')
        time.sleep(2)
        password2_box.send_keys(Keys.ENTER)
        time.sleep(3)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
