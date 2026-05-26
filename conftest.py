import pytest
from pytest_bdd import scenarios
from playwright.sync_api import sync_playwright
import sys
from pathlib import Path

# Add features path for pytest-bdd discovery
pytest_plugins = ['pytest_bdd']

@pytest.fixture(scope="session")
def browser():
    """Session-scoped browser fixture"""
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture
def page(browser):
    """Page fixture for each test"""
    page = browser.new_page()
    yield page
    page.close()

# def pytest_configure(config):
#     """Register custom markers"""
#     config.addinivalue_line(
#         "markers", "login_validation: mark test as login validation"
#     )
