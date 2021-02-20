import time

from Project_06.Locators.HotelPage_locators import HotelPage_Locators


class HotelPages():

    def __init__(self, driver):
        self.driver = driver
        self.destination_drop_xpath = HotelPage_Locators.destination_drop_xpath
        self.destination_value_xpath = HotelPage_Locators.destination_value_xpath
        self.check_in_xpath = HotelPage_Locators.check_in_xpath
        self.check_out_xpath = HotelPage_Locators.check_out_xpath
        self.adults_increase_xpath = HotelPage_Locators.adults_increase_xpath
        self.child_increase_xpath = HotelPage_Locators.child_increase_xpath
        self.search_button_xpath = HotelPage_Locators.search_button_xpath
        self.details_link_xpath = HotelPage_Locators.details_link_xpath
        self.next_photo_button_xpath = HotelPage_Locators.next_photo_button_xpath

    def select_destination(self):
        self.driver.find_element_by_xpath(self.destination_drop_xpath).click()
        self.driver.find_element_by_xpath(self.destination_value_xpath).click()

    def select_check_in(self):
        self.driver.find_element_by_xpath(self.check_in_xpath).clear()
        self.driver.find_element_by_xpath(self.check_in_xpath).send_keys("02/04/2010")

    def select_check_out(self):
        self.driver.find_element_by_xpath(self.check_out_xpath).clear()
        self.driver.find_element_by_xpath(self.check_out_xpath).send_keys("02/04/2020")

    def select_adults(self):
        for i in range(3):
            self.driver.find_element_by_xpath(self.adults_increase_xpath).click()

    def select_child(self):
        for i in range(3):
            self.driver.find_element_by_xpath(self.child_increase_xpath).click()

    def click_search(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()

    def click_details(self):
        self.driver.find_element_by_xpath(self.details_link_xpath).click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(5)

    def click_next_photo(self):
        for i in range(3):
            self.driver.find_element_by_xpath(self.next_photo_button_xpath).click()
            time.sleep(3)
