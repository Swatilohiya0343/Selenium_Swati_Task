from selenium import webdriver
from time import sleep

from selenium.webdriver.edge import service
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions  import NoSuchElementException
option=webdriver.EdgeOptions()
count = 1
chrome_driver_path =service.Service(r'C:\Users\Administrator\Desktop\msedgedriver.exe')
browser_path = "C:\\Program Files (x86)\\Microsoft\\Edge Beta\\Application\\msedge.exe" 


option.binary_location = browser_path   
browser= webdriver.Edge(service=chrome_driver_path, options = option)
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
                
                
        
   
                
