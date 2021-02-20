import time

import HtmlTestRunner
from selenium import webdriver
import unittest
from Project_06.Pages.HomePage import HomePages
from Project_06.Pages.HotelPage import HotelPages
from Project_06.Pages.FlightPage import FlightPage
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class Travels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/home/jackdaniel/PycharmProjects/selenium/Project_05/Driver/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    """def test_01_hotel_booking(self):
        driver = self.driver
        driver.get("https://phptravels.com/demo/")

        home_page = HomePages(driver)
        home_page.click_link()

        hotel_page = HotelPages(driver)
        hotel_page.select_destination()
        hotel_page.select_check_in()
        hotel_page.select_check_out()
        hotel_page.select_adults()
        hotel_page.select_child()
        hotel_page.click_search()
        hotel_page.click_details()
        hotel_page.click_next_photo()
        time.sleep(5)"""

    def test_01_flight_booking(self):
        driver = self.driver
        driver.get("https://phptravels.com/demo/")

        home_page = HomePages(driver)
        home_page.click_link()

        flight_Page = FlightPage(driver)
        flight_Page.click_flight_option()
        flight_Page.select_from()
        flight_Page.select_to()
        flight_Page.select_depart()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
