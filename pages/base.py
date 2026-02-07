from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    '''Базовый класс страницы сайта'''

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url: str) -> None:
        '''
        Метод открытия страницы по url

        :param url: URL ссылка
        :type url: str
        '''
        self.driver.get(url)

    def find_element(self, *locator: tuple[str, str]) -> WebElement:
        '''
        Метод нахождения элемента на текущей страницу

        :param locator: Пара данных (По чему поиск, значение)
        :type loacator: tuple[str, str]
        '''
        return self.driver.find_element(*locator)

    def find_elements(self, *locator: tuple[str, str]) -> list[WebElement]:
        '''
        Метод нахождения множества элементов на текущей страницу

        :param locator: Пара данных (По чему поиск, значение)
        :type loacator: tuple[str, str]
        '''
        return self.driver.find_elements(*locator)

    def click(self, *locator: tuple[str, str]) -> None:
        '''
        Метод нажатия на элемент на текущей страницу

        :param locator: Пара данных (По чему поиск, значение)
        :type loacator: tuple[str, str]
        '''
        self.find_element(*locator).click()

    def input_text(self, text: str, *locator: tuple[str, str]) -> None:
        '''
        Метод ввода текста в элемент

        :param text: Текст для ввода
        :type text: str
        :param locator: Пара данных (По чему поиск, значение)
        :type loacator: tuple[str, str]
        '''
        self.find_element(*locator).send_keys(text)

    def get_text(self, *locator: tuple[str, str]) -> str:
        '''
        Метод вывода текста из элемент

        :param locator: Пара данных (По чему поиск, значение)
        :type loacator: tuple[str, str]
        '''
        return self.find_element(*locator).text

    def is_displayed(self, *locator: tuple[str, str]) -> bool:
        '''
        Метод проверки отображения элемента

        :param locator: Пара данных (По чему поиск, значение)
        :type loacator: tuple[str, str]
        '''
        return self.find_element(*locator).is_displayed()

    def get_current_url(self) -> str:
        '''Метод получения текущего url'''
        return self.driver.current_url
