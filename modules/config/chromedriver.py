from selenium import webdriver
# Configure ChromeDriver
chrome_options = webdriver.ChromeOptions()
chrome_option.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
# Initialize ChromeDriver
driver = webdriver.Chrome(executable_path='../../resources/chromedriver.exe', options=chrome_options)
