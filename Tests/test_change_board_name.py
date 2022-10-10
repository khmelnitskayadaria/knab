import allure

from PageObject.ApiActions import ApiActions
from PageObject.AuthPage import AuthPage
from PageObject.BoardPage import BoardPage


@allure.feature("Board")
@allure.title("Change board name")
def test_change_board_name(browser):
    auth_page = AuthPage(browser)
    api = ApiActions(browser)
    board = BoardPage(browser)

    with allure.step('Create a new board'):
        title = 'AutoBoard'
        url = api.create_board(title)

    with allure.step('Authorization in Trello'):
        auth_page.full_authorization_flow(email='', password='')

    with allure.step('Board opening'):
        api.driver.get(url)
        assert f'{title}' in board.find_title()

    with allure.step('Change board name'):
        new_title = 'ChangeTitle'
        board.change_title(new_title)
        assert f'{new_title}' in board.find_title()

    with allure.step('Delete new board'):
        api.delete_new_board(url)


