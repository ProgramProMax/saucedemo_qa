import allure
from selenium.webdriver import Chrome

from pages.login import LoginPage
from .fixtures import browser  # noqa


@allure.feature('Авторизация')
@allure.story('Проверка возможности авторизации')
class TestLogin:

    INVENTORY_URL = 'https://www.saucedemo.com/inventory.html'

    @allure.title('Проверка авторизации с валидными данными')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, browser: Chrome) -> None:
        '''Тестирование успешного входа'''
        with allure.step('Открыть страницу авторизации'):
            login_page = LoginPage(browser)
            login_page.open()

        with allure.step('Ввести валидные данные и авторизоваться'):
            login_page.login('standard_user', 'secret_sauce')

        with allure.step('Проверить, что авторизация прошла успешно'):
            assert login_page.get_current_url() == self.INVENTORY_URL, (
                'URL не соответствует ожидаемому после авторизации'
            )

        with allure.step(
            'Проверить, что контейнер с инвентарем '
            ' отображается на странице после авторизации'
        ):
            assert login_page.is_inventory_container_displayed(), (
                'Контейнер с инвентарем не отображается на '
                'странице после авторизации'
            )

    @allure.title('Проверка авторизации с невалидными данными')
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_invalid_data(self, browser: Chrome) -> None:
        '''Тестирование обработки авторизации с неверными данными'''
        with allure.step('Открыть страницу авторизации'):
            login_page = LoginPage(browser)
            login_page.open()

        with allure.step((
            'Ввести невалидные данные '
            'и попытаться авторизоваться'
        )):
            login_page.login('invalid_user', 'invalid_password')

        with allure.step('Проверить, что отображается сообщение об ошибке'):
            assert login_page.is_error_displayed(), (
                'Сообщение об ошибке не отображается '
                'при вводе невалидных данных'
            )
            assert (
                'Username and password do not match'
                in login_page.get_error_message()
            ), (
                'Текст сообщения об ошибке не соответствует ожидаемому '
                'при вводе невалидных данных'
            )

    @allure.title('Авторизация с заблокированным пользователем')
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_locked_user(self, browser: Chrome) -> None:
        '''Тестирование обработки авторизации заблокированного пользователя'''
        with allure.step('Открыть страницу авторизации'):
            login_page = LoginPage(browser)
            login_page.open()

        with allure.step(
            'Ввести данные заблокированного пользователя '
            'и попытаться авторизоваться'
        ):
            login_page.login('locked_out_user', 'secret_sauce')

        with allure.step('Проверить, что отображается сообщение об ошибке'):
            assert login_page.is_error_displayed(), (
                'Сообщение об ошибке не отображается при попытке '
                'авторизации заблокированного пользователя'
            )
            assert (
                login_page.get_error_message() ==
                'Epic sadface: Sorry, this user has been locked out.'
            ), (
                'Текст сообщения об ошибке не соответствует ожидаемому '
                'при попытке авторизации заблокированного пользователя'
            )

    @allure.title('Авторизация с пустыми полями')
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_empty_fields(self, browser: Chrome) -> None:
        '''Тестирование обработки авторизации с пустыми данными'''
        with allure.step('Открыть страницу авторизации'):
            login_page = LoginPage(browser)
            login_page.open()

        with allure.step('Оставить поля пустыми и попытаться авторизоваться'):
            login_page.login('', '')

        with allure.step('Проверить, что отображается сообщение об ошибке'):
            assert login_page.is_error_displayed(), (
                'Сообщение об ошибке не отображается '
                'при попытке авторизации с пустыми полями'
            )
            assert (
                login_page.get_error_message() ==
                'Epic sadface: Username is required'
            ), (
                'Текст сообщения об ошибке не соответствует ожидаемому '
                'при попытке авторизации с пустыми полями'
            )

    @allure.title('Aвторизация пользователем с задежками')
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_slow_user(self, browser: Chrome) -> None:
        '''Тестирование обработки авторизации пользователя с задержкой'''
        with allure.step('Открыть страницу авторизации'):
            login_page = LoginPage(browser)
            login_page.open()

        with allure.step((
            'Ввести данные пользователя с задержками '
            'и попытаться авторизоваться'
        )):
            login_page.login('performance_glitch_user', 'secret_sauce')

        with allure.step((
            'Проверить, что авторизация прошла успешно,'
            ' несмотря на задержки'
        )):
            assert login_page.get_current_url() == self.INVENTORY_URL, (
                'URL не соответствует ожидаемому '
                'после авторизации пользователя с задержками'
            )
            assert login_page.is_inventory_container_displayed(), (
                'Контейнер с инвентарем не отображается на странице '
                'после авторизации пользователя с задержками'
            )
