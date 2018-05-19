from selenium import webdriver
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options)
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("https:\\spotify.com")
##assert "Python" in driver.title
elem1 = driver.find_element_by_id("header-login-link")
elem1.click()
##elem1 = driver.find_element_by_css_selector("#wimp > div.grid > div.grid__row > nav > ul > li.currentUser > a.btn.js-login.current-user__login")
##elem1.click()
##elem1 = driver.find_element_by_id("username")
##elem1.clear()
##elem1.send_keys("lenrok09@gmail.com")
##elem1 = driver.find_element_by_id("password")
##elem1.clear()
##elem1.send_keys("fvgvtw3w")
##elem1.send_keys(Keys.RETURN)
##driver.get("https:\\listen.tidal.com\rising")

####elem1 = driver.find_element_by_id("header-login-link")
##driver.get("https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbLiRSasKsNU9")


##elem = driver.find_element_by_name("q")
##elem.clear()
##elem.send_keys("pycon")
##elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
##driver.close()
