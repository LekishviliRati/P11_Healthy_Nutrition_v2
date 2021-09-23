import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AutocompleteTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_autocomplete_path(self):

        # Check if Django is working
        self.browser.get('http://localhost:8000')
        self.browser.maximize_window()
        self.assertIn('Pur Beurre', self.browser.title)

        # Fill navigation search field
        input_field_navigation = self.browser.find_element_by_id('nav_input_base')
        input_field_navigation.send_keys('Pri')
        time.sleep(5)
        # Check if autocomplete field is not missing
        autocomplete_field = self.browser.find_element_by_id('ui-id-1')
        self.assertTrue(autocomplete_field)

        # Fill home page search field
        input_field_home_page = self.browser.find_element_by_id('nav_input_home')
        input_field_home_page.send_keys('Pri')
        time.sleep(5)
        # Check if autocomplete field is not missing
        autocomplete_field = self.browser.find_element_by_id('ui-id-1')
        self.assertTrue(autocomplete_field)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
