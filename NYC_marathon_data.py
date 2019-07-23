##Code for scraping the results of the 2018 NYC marathon
##Created by Aparna Sundaram
##Created on July 21st 2019
##To be added to Git Hub



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import re

##provide the path to the Chrome driver
driver = webdriver.Chrome(r'C:\Users\aparn\Downloads\chromedriver.exe')

#Provide the URL for the page you want to scrape 
driver.get("https://results.nyrr.org/event/M2018/finishers?_ga=2.187862696.1887926060.1563589053-1852531103.1563589053")
print(1)


# Click Show more button to go to load more records

for i in range(0, 50):
    try:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # wait to load page
        time.sleep(5)
        
        #click the show more button
        record_button = driver.find_element_by_xpath('//div[4]/a[@href="#"]')
        record_button.click()
        print('button clicked')
        
        
    
    except:
        print("in exception")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    


#initialize the csv file
csv_file = open('runners.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
print(2)
writer.writerow(['name', 'country', 'age', 'sex', 'runner_Id', 'hours', 'minutes', 'seconds', 'place'])
print(3)


# Find all the runners on the page. This tells the code to wait until all the runners are loaded on page.
wait_runner = WebDriverWait(driver, 10)
runners = wait_runner.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="row rms-grid-item"]')))
print(4)
print(len(runners))


index=1
while True:
    print("Scraping number " + str(index))
    index = index + 1
        

        
    for runner in runners:
        
        #initialize an empty directory
        runner_dict = {}
            
        name=runner.find_element_by_xpath('.//div[@class="name rms-grid-line ng-binding"]').text
        country= runner.find_element_by_xpath('.//div[2]/span[2]').text

        agesex=runner.find_element_by_xpath('.//span[@class="ng-binding ng-scope"]').text
        age= re.findall('\d+', agesex)[0]    
        sex = re.findall('M|F', agesex)[0]

        bib=runner.find_element_by_xpath('.//span[@class="left-bordered ng-scope"]').text
        runner_Id = re.findall('\d+', bib)[0]

        time=runner.find_element_by_xpath('.//span[2]/span[@class="num ng-binding"]').text
        hr_,min_,sec_=time.split(':')
        hour= hr_
        mins = min_
        sec = sec_
        
        place=runner.find_element_by_xpath('.//span[4]/span[@class="num ng-binding"]').text

        #print (name, "|", country, "|", age, "|", sex, "|", runner_Id, "|", hour, "|", mins, "|", sec,"|", place)

        runner_dict['name'] = name
        runner_dict['country'] = country
        runner_dict['age'] = age
        runner_dict['sex'] = sex
        runner_dict['runner_Id'] = runner_Id
        runner_dict['hour'] = hour
        runner_dict['minutes'] = mins
        runner_dict['seconds'] = sec
        runner_dict['place'] = place

        writer.writerow(runner_dict.values()) ##Puts the values into a csv file. 
        #print(5)

        continue
