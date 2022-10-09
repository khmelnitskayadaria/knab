from time import sleep

import allure

from PageObject.ApiActions import ApiActions
from PageObject.AuthPage import AuthPage
from PageObject.BoardPage import BoardPage


@allure.feature("Board")
@allure.title("Creating a new board")
def test_create_board(browser):
    auth_page = AuthPage(browser)
    api = ApiActions(browser)
    board = BoardPage(browser)

    with allure.step('Create a new board'):
        title = 'AutoBoard'
        url = api.create_board(title)

    with allure.step('Preconditions. Authorization in Trello'):
        auth_page.go_to_site()
        auth_page.enter_email('')
        auth_page.click_go_button()
        sleep(5)
        auth_page.enter_password('')
        auth_page.click_login_button()

    with allure.step('Board opening'):
        sleep(5)
        api.driver.get(url)
        # assert f'{title}' in board.find_title()

    with allure.step('Change board name'):
        new_title = 'ChangeTitle'
        board.change_title(new_title)
        assert f'{new_title}' in board.find_title()


