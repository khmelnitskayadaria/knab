import allure

from PageObject.ApiActions import ApiActions
from PageObject.AuthPage import AuthPage
from PageObject.BoardsPage import BoardsPage


def find_board_area():
    pass


@allure.feature("Board")
@allure.title("Delete board")
def test_delete_board(browser):
    api = ApiActions(browser)
    auth_page = AuthPage(browser)
    boards_page = BoardsPage(browser)

    with allure.step('Create a new board'):
        title = 'AutoBoard'
        url = api.create_board(title)

    with allure.step('Delete new board'):
        api.delete_new_board(url)

    with allure.step('Authorization in Trello'):
        auth_page.full_authorization_flow(email='', password='')
        elements = boards_page.find_board_area()
        assert not title in elements
