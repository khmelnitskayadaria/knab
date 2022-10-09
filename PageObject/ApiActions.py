from PageObject.Base import BasePage
import requests




class ApiActions(BasePage):

    def create_board(self, name):
        url = "https://api.trello.com/1/boards/"

        query = {
            'name': f'{name}',
            'key': api_key,
            'token': token
        }

        response = requests.request(
            "POST",
            url,
            params=query
        )


        response = response.json()
        url = response['url']
        return url

    def delete_new_board(self, value):
        str_url = self.driver.getCurrentUrl()
        url = str_url.replace("https://trello.com/b/", "").replace(f"/{value}", "")
        query = {
             'key': api_key,
            'token': token
        }

        response = requests.request(
            "DELETE",
            url,
            params=query
        )

        return response.text


