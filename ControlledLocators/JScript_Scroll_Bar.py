import time

from selenium.webdriver.common.keys import Keys


class ScrollBar:

    def __init__(self, driver):
        self.driver = driver

    # this function used to scroll down to end of the page of browser's page.

    def scroll_To_End_Of_Page(self):
        SCROLL_PAUSE_TIME = 1.0
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    # this function used to scroll DOWN for a little bit on the browser's page.

    def scroll_To_Vertical_Down_Of_Page(self):
        # Wait to load page
        time.sleep(10)
        # Scroll down to bottom
        self.driver.execute_script("window.scrollTo(0,400);")

    # this function used to scroll UP for a little bit on the browser's page.

    def scroll_To_Vertical_Up_Of_Page(self):
        SCROLL_PAUSE_TIME = 1.0
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Scroll Up to bottom
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)


