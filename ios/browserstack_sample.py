from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
  
desired_cap = {
    # Set your access credentials
    "browserstack.user" : "usapaincraft_KdGprt",
    "browserstack.key" : "TTT9o1kBsqYpsUvrVqcB",
  
    # Set URL of the application under test
    "app" : "bs://0d108a48232e1ea2ef6fc1ac4ca707e36356d1fb",
  
    # Specify device and os_version for testing
    "device" : "iPhone 12 Pro Max",
    "os_version" : "16",
      
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "browserstack-build-1",
    "name" : "first_test"
}
  
# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap
)
  
# If you have uploaded your app, write your test case here. 
  
# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
