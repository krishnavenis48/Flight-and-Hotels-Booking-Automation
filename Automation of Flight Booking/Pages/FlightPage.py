from Project_06.Locators.FlightPage_locators import FlightPage_Locators


class FlightPage():

    def __init__(self, driver):
        self.driver = driver
        self.flight_option_xpath = FlightPage_Locators.flight_option_xpath
        self.from_drop_xpath = FlightPage_Locators.from_drop_xpath
        self.from_value_xpath = FlightPage_Locators.from_value_xpath
        self.to_drop_xpath = FlightPage_Locators.to_drop_xpath
        self.to_value_xpath = FlightPage_Locators.to_value_xpath
        self.depart_date_xpath = FlightPage_Locators.depart_date_xpath
        self.adults_increase_xpath = FlightPage_Locators.adults_increase_xpath
        self.child_increase_xpath = FlightPage_Locators.child_increase_xpath
        self.infant_xpath = FlightPage_Locators.infant_xpath
        self.search_button_xpath = FlightPage_Locators.search_button_xpath

    def click_flight_option(self):
        self.driver.find_element_by_xpath(self.flight_option_xpath).click()

    def select_from(self):
        self.driver.find_element_by_xpath(self.from_drop_xpath).click()
        self.driver.find_element_by_xpath(self.from_drop_xpath).send_keys("LHE")
        self.driver.find_element_by_xpath(self.from_value_xpath).click()

    def select_to(self):
        self.driver.find_element_by_xpath(self.to_drop_xpath).click()
        self.driver.find_element_by_xpath(self.to_drop_xpath).send_keys("DXB")
        self.driver.find_element_by_xpath(self.to_value_xpath).click()

    def select_depart(self):
        self.driver.find_element_by_xpath(self.depart_date_xpath).clear()
        self.driver.find_element_by_xpath(self.depart_date_xpath).send_keys("05/10/2010")