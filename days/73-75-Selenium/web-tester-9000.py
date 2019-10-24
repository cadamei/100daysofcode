from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # replaced Firefox by Chrome
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

new_rfc = 'https://rap-qa.dimensiondata.com.au/rfc/create'

driver = webdriver.Chrome()
driver.get(new_rfc)

driver.find_element_by_id('edit-name').send_keys(user)
driver.find_element_by_id('edit-pass').send_keys(pw + Keys.RETURN)