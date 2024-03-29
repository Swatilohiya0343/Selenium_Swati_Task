from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By for specifying the locator strategy
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.binary_location = '/usr/bin/google-chrome'  # Specify Chrome binary location
chrome_options.add_argument('--headless')  # Run Chrome in headless mode

browser = webdriver.Chrome(options=chrome_options)

url = "https://www.cbse.gov.in/cbsenew/question-paper.html"

browser.get(url)
for i in range(1, 11):
    try:
        page1 = browser.find_element(By.XPATH, '//*[@id="cbp-ntaccordion"]/li[' + str(i) + ']/h3')
        page1.click()
        page2 = browser.find_element(By.XPATH, '//*[@id="cbp-ntaccordion"]/li[' + str(i) + ']/div/ul/li[1]/h4')
        page2.click()
        sleep(4)
        for j in range(1, 31):
            try:
                reviews = browser.find_element(By.XPATH, '//*[@id="cbp-ntaccordion"]/li[1]/div/ul/li[1]/div/div[2]/table/tbody/tr[' + str(j) + ']/td[2]/a')
                reviews.click()
                print(j)
            except NoSuchElementException:
                pass
    except NoSuchElementException:
        pass
                
