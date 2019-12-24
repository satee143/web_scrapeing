import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('start-maximized') #
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
options.add_argument("--window-size=1080,1920")
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

options.add_argument('user-agent={0}'.format(user_agent))
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://www.accuweather.com')
try:

    element=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//input[@class="search-input"]')))

#element=driver.find_element_by_xpath('//input[@class="search-input"]')
    element.send_keys('505001')
    time.sleep(5)
    element.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.find_element_by_xpath('//div[@class="search-results"]/a').click()
    driver.find_element_by_xpath('//*[text()="Daily"]').click()
    time.sleep(2)
    pincode=driver.find_element_by_xpath('//span/h1').text
    url=driver.current_url
    print(pincode.strip())
except:
    driver.save_screenshot('a.jpg')

