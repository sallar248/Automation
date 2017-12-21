## Notes for Python Testing

Browser get
driver.git(("http://www.google.com")

Interactions with the page
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")

Sending Keys
element.send_keys("some text")
element.send_keys(" and some", Keys.ARROW_DOWN)
element.clear

Filling in forms
element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_element_by_tag_name("option)
for option in all_options:
    print("Value is" %s" % option.get_attribute("value"))
    option.click()


Select Elements
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)

Deselecting
select = Select(driver.find_element_by_id('id'))
select.deselect)all()

Drag and Drop
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selemenium.webdriver import actionChains
actio_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()


Switching between windows / frames
driver.switch_to_window("windowName")

Popup Dialogs
alert = driver.switch_to_alert()

Navigation History
driver.get("http://www.example.com")

Move backward / forward
driver.forward()
driver.back()

Cookies
example
