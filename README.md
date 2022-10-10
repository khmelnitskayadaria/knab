1. WebDriver initialization happens in a fixture. Fixtures in pytest are functions that have their own frequency of execution.
This is an alternative replacement for the SetUp and TearDown methods in unittest. Using a fixture, you can prepare the initial state of the system for testing.\
In pytest - fixtures are released in the conftest.py file
2. The BasePage class defines basic methods for working with WebDriver. In the BasePage class, we create a constructor that takes a driver - an instance of webdriver. Specify the base_url that will be used to open the page.
3. Page object - divided by pages. Each page has a locator class and a class with helper methods for working with page elements, this class is inherited from BasePage.
4. In the test function, the fixture is raised, methods for interacting with page elements are called. The function describes the top-level logic of user actions.

Test cases can be found here https://docs.google.com/spreadsheets/d/1n5BrWYpx9RDbj4SECOirMt62qzxkf1BZKH_Bd3jDlAA/edit#gid=0 