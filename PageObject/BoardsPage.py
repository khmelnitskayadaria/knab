import allure
from selenium.webdriver.common.by import By

from PageObject.Base import BasePage


class BoardsPageLocators():
    """A class for boards locators. All boards locators should
    come here"""

    FRAME = (By.CLASS_NAME, 'JpK+-eghInruBP js-react-root')
    CREATE_BOARD = (By.ID, 'create-board-tile')
    TITLE_FIELD = (By.ID, 'create-board-title-input')
    CREATE_BUTTON = (By.ID, 'create-board-submit-button')
    BOARD_AREA = (By.ID, 'boards-page-board-section-list')


class BoardsPage(BasePage):
    """Boards page action methods come here"""

    @allure.step("Click on Crete button")
    def click_on_create_board_in_list(self):
        create_board_in_list_button = self.find_element(BoardsPageLocators.CREATE_BOARD)
        create_board_in_list_button.click()
        return create_board_in_list_button

    @allure.step("Enter title in field")
    def enter_title(self, title):
        frame = self.find_element(BoardsPageLocators.FRAME)
        self.driver.switch_to.frame(frame)
        title_field = self.find_element(BoardsPageLocators.TITLE_FIELD)
        title_field.click()
        title_field.send_keys(title)
        return title_field

    @allure.step("Click on create board title")
    def click_on_create_button(self):
        frame = self.find_element(BoardsPageLocators.FRAME)
        self.driver.switch_to.frame(frame)
        return self.find_element(BoardsPageLocators.CREATE_BUTTON).click()

    @allure.step("Find area with all boards")
    def find_board_area(self):
        boards = self.find_element(BoardsPageLocators.BOARD_AREA)
        return boards