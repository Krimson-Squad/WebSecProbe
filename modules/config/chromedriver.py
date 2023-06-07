# CONFIGURATION MODULE FOR CHROMEDRIVER
# YOU CAN MODIFY IT AS PER YOUR NEED
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
