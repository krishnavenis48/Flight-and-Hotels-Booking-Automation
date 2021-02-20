class FlightPage_Locators():
    flight_option_xpath = "//a[contains(@class,'text-center flights')]"
    from_drop_xpath = "//div[@id='s2id_location_from']//a[@class='select2-choice']"
    from_value_xpath = "//div[@id='select2-drop']//li[2]"
    to_drop_xpath = "//div[@id='s2id_location_to']//a[@class='select2-choice']"
    to_value_xpath = "//span[@class='select2-match']"
    depart_date_xpath = "//input[@id='FlightsDateStart']"

    adults_increase_xpath = "//div[contains(@class,'row no-gutters row-reverse align-items-end')]//div[contains(" \
                            "@class,'row no-gutters')]//div[1]//div[1]//div[2]//div[1]//span[1]//button[1] "
    child_increase_xpath = "//div[@id='flights']//div[2]//div[1]//div[2]//div[1]//span[1]//button[1]"
    infant_xpath = "//div[contains(@class,'col-lg-4 col-sm-12 col-xs-12')]//div[3]//div[1]//div[2]//div[1]//span[" \
                   "1]//button[1] "
    search_button_xpath = "//div[contains(@class,'col-lg-1 col-sm-12 col-xs-12')]//button[contains(@class," \
                          "'btn-primary btn btn-block')][contains(text(),'Search')] "
