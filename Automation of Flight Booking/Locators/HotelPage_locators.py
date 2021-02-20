class HotelPage_Locators():
    # hotel page
    destination_drop_xpath = "//div[@id='s2id_autogen16']//span[@class='select2-chosen'][contains(text(),'Search by " \
                             "Hotel or City Name')] "
    destination_value_xpath = "//div[@id='select2-drop']//li[1]//ul[1]//li[1]"
    check_in_xpath = "//input[@id='checkin']"
    check_out_xpath = "//input[@id='checkout']"
    adults_increase_xpath = "//div[contains(@class,'col o2')]//button[contains(@class,'btn btn-white " \
                            "bootstrap-touchspin-up')][contains(text(),'+')] "
    child_increase_xpath = "//div[contains(@class,'col 01')]//button[contains(@class,'btn btn-white " \
                           "bootstrap-touchspin-up')][contains(text(),'+')] "
    search_button_xpath = "//form[contains(@name,'HOTELS')]//button[contains(@class,'btn btn-primary btn-block')][" \
                          "contains(text(),'Search')] "
    details_link_xpath = "//div[@class='content-wrapper']//div[1]//div[1]//div[2]//div[1]//div[3]//div[1]//div[2]//a[1]"
    next_photo_button_xpath = "//div[@class='slider gallery-slideshow slick-initialized slick-slider']//button[" \
                              "@class='slick-next slick-arrow'][contains(text(),'Next')] "
