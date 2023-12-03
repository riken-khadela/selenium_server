from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set the path to the ChromeDriver (change this to your ChromeDriver path)
chromedriver_path = '/home/dell/Desktop/selenium_server/chromedriver'
chrome_binary_path = '/usr/bin/google-chrome'

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_binary_path

# chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

# Create a service object with specified path and options
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
breakpoint()
# Replace this with your desired website URL
website_url = 'https://example.com'

# Open the website
driver.get(website_url)

# Perform actions as needed...

# Close the browser window
driver.quit()
