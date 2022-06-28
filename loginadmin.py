from playwright.sync_api import Page
import pytest
from models.search import SearchPage





# def test_example_is_working(page):
#     page.goto("https://example.com")
#     assert page.inner_text('h1') == 'Example Domain'
#     page.click("text=More information")
# test_search.py
# test_search.py

# test_search.py

# in the test
def test_1(page:Page):

    # in the test
    # in the test

    
    searc = SearchPage(page)
    searc.navigate()
    searc.search("admin@yourstore.com","admin")
    assert page.title() == "Dashboard / nopCommerce administration"
    

    