import pytest
from selene import browser, be, have

@pytest.fixture()
def open_browser():
    browser.driver.set_window_size(1920, 1500)
    browser.open('https://google.com')

def test_search(size_browser, open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_not_find_results(open_browser):
    res = 'sdflsdnfjvbsnldfkjbndfbsdfbsdfbsdf'
    browser.element('[name="q"]').should(be.blank).type(res).press_enter()
    browser.element('[class="card-section"]').should(have.text(f'По запросу {res} ничего не найдено'))
