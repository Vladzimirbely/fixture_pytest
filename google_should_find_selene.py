import pytest
from selene import browser, be, have

@pytest.fixture()
def size_browser():
    browser.driver.set_window_size(1920, 1500)
@pytest.fixture()
def open_browser():
    browser.open('https://google.com')

def test_search(size_browser, open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))