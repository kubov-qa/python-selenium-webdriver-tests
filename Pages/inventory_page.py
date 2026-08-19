from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class InventoryPage(BasePage):
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")

