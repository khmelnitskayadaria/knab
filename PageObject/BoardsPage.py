from selenium.webdriver.common.by import By

from PageObject.Base import BasePage


class BoardsPageLocators():
    """A class for boards locators. All boards locators should
    come here"""

    FRAME = (By.CLASS_NAME, 'JpK+-eghInruBP js-react-root')
    CREATE_BOARD = (By.ID, 'create-board-tile')
    TITLE_FIELD = (By.ID, 'create-board-title-input')
    CREATE_BUTTON = (By.ID, 'create-board-submit-button')


class BoardsPage(BasePage):
    """Boards page action methods come here"""

    def click_on_create_board_in_list(self):
        create_board_in_list_button = self.find_element(BoardsPageLocators.CREATE_BOARD)
        create_board_in_list_button.click()
        return create_board_in_list_button

    def enter_title(self, title):
        frame = self.find_element(BoardsPageLocators.FRAME)
        self.driver.switch_to.frame(frame)
        title_field = self.find_element(BoardsPageLocators.TITLE_FIELD)
        title_field.click()
        title_field.send_keys(title)
        return title_field

    def click_on_create_button(self):
        frame = self.find_element(BoardsPageLocators.FRAME)
        self.driver.switch_to.frame(frame)
        return self.find_element(BoardsPageLocators.CREATE_BUTTON).click()
