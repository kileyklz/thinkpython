import time
import selenium


## Open remote browser from docker 172.18.3.1 port 4000 and goto amazon.com
## set browser to maximize

driver = selenium.webdriver.Remote("http://172.18.3.1:4000", selenium.webdriver.DesiredCapabilities.CHROME)
driver.get("http://amazon.com")
driver.maximize_window()

## wait for 5 seconds then take as screenshot
time.sleep(5)
driver.save_screenshot("test2.png")

## close browser
driver.quit()

# Path: Selenium-examples/test3.py