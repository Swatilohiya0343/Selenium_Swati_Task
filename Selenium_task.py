from selenium import webdriver
from time import sleep
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path

browser = webdriver.Chrome()

from selenium.common.exceptions  import NoSuchElementException



url="https://www.cbse.gov.in/cbsenew/question-paper.html"


browser.get(url)
for i in range(1,11):
    try:
        page1=browser.find_element_by_xpath('//*[@id="cbp-ntaccordion"]/li['+str(i)+']/h3')
        page1.click()
        page2=browser.find_element_by_xpath('//*[@id="cbp-ntaccordion"]/li['+str(i)+']/div/ul/li[1]/h4')
        page2.click()
        sleep(4)
        for j in range(1,31):
                    
                
                    try:
                        
                        reviews=browser.find_element_by_xpath('//*[@id="cbp-ntaccordion"]/li[1]/div/ul/li[1]/div/div[2]/table/tbody/tr['+str(j)+']/td[2]/a')
                       
                      
                        reviews.click()
                        print(j)
                       
                    except NoSuchElementException:
                        pass
    except NoSuchElementException:
        pass
                
                
        
   
                
