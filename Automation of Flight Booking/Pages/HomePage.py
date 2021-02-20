import time
from Project_06.Locators.HomePage_locators import HomePage_Locators


class HomePages():

    def __init__(self, driver):
        self.driver = driver
        self.front_end_xpath = HomePage_Locators.front_end_xpath

    def click_link(self):
        self.driver.find_element_by_xpath(self.front_end_xpath).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(10)
