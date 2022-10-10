import allure

from PageObject.AuthPage import AuthPage
from PageObject.BoardPage import BoardPage
from PageObject.BoardsPage import BoardsPage


@allure.feature("Board")
@allure.title("Creating a new board UI")
def test_create_board(browser):
    auth_page = AuthPage(browser)
    boards = BoardsPage(browser)
    board = BoardPage(browser)

    with allure.step('Authorization in Trello'):
        auth_page.full_authorization_flow(email='', password='')

    with allure.step('Creating a new board'):
        boards.click_on_create_board_in_list()
        title = 'AutoBoard'
        boards.enter_title(title)
        boards.click_on_create_button()

    with allure.step('Check that board was created'):
        element = board.find_title()
        assert title in element


