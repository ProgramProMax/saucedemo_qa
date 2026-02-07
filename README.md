# Автоматизация тестирования SauceDemo

Проект для автоматизации тестирования авторизации на сайте [SauceDemo](https://www.saucedemo.com/).

## Структура проекта

```
saucedemo-qa/
├── pages/           # Page Object модели
├── tests/           # Тесты
├── allure-results/  # Результаты Allure
├── reports/         # HTML отчеты
├── Dockerfile       # Конфигурация Docker
├── requirements.txt # Зависимости Python
└── README.md
```

## Предварительные требования

- Python 3.10+
- Docker (опционально, для запуска в контейнере)
- Allure CLI (для генерации отчетов)

## Установка

1. Клонировать репозиторий
2. Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов

### Локальный запуск

```bash
# Запуск всех тестов
pytest tests/

# Запуск с Allure отчетом
pytest tests/ --alluredir=allure-results

# Генерация Allure отчета
allure serve allure-results

# Запуск конкретного теста
pytest tests/test_login.py::TestLogin::test_successful_login
```

### Запуск в Docker

```bash
# Cборка и запуск
docker build -t saucedemo-qa .
```

## Тестовые сценарии

1. ✅ Успешная авторизация (standard_user)
2. ✅ Авторизация с неверным паролем
3. ✅ Авторизация заблокированным пользователем
4. ✅ Авторизация с пустыми полями
5. ✅ Авторизация пользователем с задержками (performance_glitch_user)

## Генерация отчетов

### Allure отчеты

```bash
# Генерация отчета
allure generate allure-results -o allure-report --clean

# Открытие отчета
allure open allure-report
```

### HTML отчет

HTML отчет генерируется автоматически в папку `allure-report/`

## Используемые технологии

- Python 3.10
- Selenium WebDriver
- Pytest
- Allure Framework
- Page Object Pattern
- Docker
- WebDriver Manager
