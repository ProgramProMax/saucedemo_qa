from .base import BasePage


class LoginPage(BasePage):
    '''Класс страницы '''

    class locators:
        '''Набор локаторов для страницы авторизации'''
        USERNAME_INPUT = ('id', 'user-name')
        PASSWORD_INPUT = ('id', 'password')
        LOGIN_BUTTON = ('id', 'login-button')
        ERROR_MESSAGE = ('css selector', '[data-test="error"]')
        LOGO = ('css selector', '.login_logo')
        INVENTORY_CONTAINERS = ('css selector', '.inventory_container')

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.saucedemo.com/'

    def open(self) -> None:
        '''Метод открытия страницы'''
        super().open(self.url)

    def login(self, username: str, password: str) -> None:
        '''
        Метод осуществления входа
        :param username: Имя пользователя
        :type usesrname: str
        :param password: Пароль
        :type password: str
        '''
        self.input_text(username, *self.locators.USERNAME_INPUT)
        self.input_text(password, *self.locators.PASSWORD_INPUT)
        self.click(*self.locators.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        '''Метод получения сообщения об ошибке'''
        return self.get_text(*self.locators.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        '''Метод проверки отображения сообщения об ошибке'''
        return self.is_displayed(*self.locators.ERROR_MESSAGE)

    def is_logo_displayed(self) -> bool:
        '''Метод проверки отображения лого'''
        return self.is_displayed(*self.locators.LOGO)

    def is_inventory_container_displayed(self) -> bool:
        '''Метод проверки отображения элементов магазина'''
        return self.is_displayed(*self.locators.INVENTORY_CONTAINERS)
