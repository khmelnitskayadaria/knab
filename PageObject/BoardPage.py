from asyncio import sleep

from selenium.webdriver.common.by import By

from PageObject.Base import BasePage


class BoardPageLocators():
    """A class for board locators. All boards locators should
    come here"""

    BOARD = (By.CLASS_NAME, 'board-main-content')
    HEADER = (By.CLASS_NAME, 'board-header u-clearfix js-board-header')
    BOARD_NAME = (By.XPATH, '//*[@id="content"]/div/div[1]/div[1]/div[1]')


class BoardPage(BasePage):
    """Board page action methods come here"""

    def find_title(self):
        find_title = self.find_element(BoardPageLocators.BOARD_NAME)
        return find_title

    def change_title(self, title):
        sleep(10)
        find_title = self.find_element(BoardPageLocators.BOARD_NAME)
        self.driver.move_to_element(find_title)
        find_title.click()
        new_title = find_title.send_keys(title)
        return new_title


