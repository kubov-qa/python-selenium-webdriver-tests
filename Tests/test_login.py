from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Tests.test_data import VALID_USERNAME, LOCKED_OUT_USERNAME, VALID_PASSWORD, BASE_URL


def test_successful_login():
  driver = webdriver.Chrome()
  login_page = LoginPage(driver)
  login_page.open(BASE_URL)
  login_page.login(VALID_USERNAME, VALID_PASSWORD)

  inventory_page = InventoryPage(driver)
  assert inventory_page.text(InventoryPage.PRODUCTS_TITLE) == InventoryPage.PRODUCTS_TITLE_TEXT
  assert driver.current_url == InventoryPage.INVENTORY_URL

  driver.quit()

def test_locked_out_user_cannot_login():
  driver = webdriver.Chrome()
  login_page = LoginPage(driver)
  login_page.open(BASE_URL)
  login_page.login(LOCKED_OUT_USERNAME, VALID_PASSWORD)
  assert login_page.text(LoginPage.ERROR_MESSAGE) == LoginPage.LOCKED_OUT_ERROR_TEXT

  driver.quit()
