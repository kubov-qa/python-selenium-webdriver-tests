from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    
    def __init__(self, driver, timeout=10):
      self.driver = driver
      self.timeout = timeout

    
    def find(self, locator):
      element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
      return element

    
    def click(self, locator):
      element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
      element.click()
    

    def open(self, url):
      self.driver.get(url)
    
