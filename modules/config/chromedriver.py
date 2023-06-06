from selenium import webdriver
# Configure ChromeDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
# Initialize ChromeDriver
driver = webdriver.Chrome('../../resources/chromedriver.exe', options=chrome_options)
