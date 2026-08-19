from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class InventoryPage(BasePage):
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    PRODUCTS_TITLE_TEXT = "Products"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
