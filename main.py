import time

# importing all the necessary selenium packages
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# for defifning proxies
#import random
#import config
#ips=['114.143.0.177:80','64.227.134.208:80','103.133.221.251:80']
#def rand_proxy():
#    proxy=random.choice(ips)
#    return proxy

# importing BeautifulSoup
from bs4 import BeautifulSoup

# setting up the service and driver(Chrome)
service=Service(executable_path='chromedriver.exe')
driver=webdriver.Chrome(service=service)

# in case want to setup proxies
#chrome_options=webdriver.ChromeOptions()
#proxy=rand_proxy()
#chrome_options.add_argument(f'--proxy-server={proxy}')



# opening the linkedin login webpage
driver.get('https://linkedin.com/login')
time.sleep(2)

# entering the login details and clicking enter
input_email=driver.find_element(By.ID,'username')
input_email.send_keys('sameeran4218@gmail.com'+Keys.ENTER)
input_password=driver.find_element(By.ID,'password')
input_password.send_keys('Starboy11'+Keys.ENTER)

# waiting in case website asks for security measures
time.sleep(30)

# after logging in, navigating to Sundar Pichai's profile
driver.get('https://www.linkedin.com/in/sundarpichai/')
time.sleep(3)

# scrolling to the bottom of the page slowly to load all the data
x = 0
while x < 20:
    driver.execute_script('scrollBy(0,100)')
    time.sleep(0.5)
    x += 1

#now that the data is fully loaded , we will scrape the data like name,job,location,about

# creating a BeautifulSoup object for the profile page
html_content=driver.page_source
soup=BeautifulSoup(html_content,'html.parser')

# scraping the basic information
name=soup.find('h1',class_='text-heading-xlarge inline t-24 v-align-middle break-words').text
job=soup.find('div',class_='text-body-medium break-words').text
location=soup.find('span',class_='text-body-small inline t-black--light break-words').text
about=driver.find_element(By.XPATH,'//*[@id="profile-content"]/div/div[2]/div/div/main/section[3]/div[3]/div/div/div/span[1]').text

#printing the basic information
print("Name: "+name.strip())
print("Job: "+job.strip())
print("Location: "+location.strip())
print("About: "+about)
print(" ")



# navigating to the Education page
show_education=driver.find_element(By.ID,'navigation-index-see-all-education').click()
time.sleep(10)

# creating a new BeautifulSoup object for the Education page
education_content=driver.page_source
soup2=BeautifulSoup(education_content,'html.parser')

# scraping education info such as institute name, degree and printing them out
education=soup2.find_all('li',class_='pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column')
for edu in education:
    institute=edu.find_next('span',class_='visually-hidden')
    degree_span=edu.find_next('span',class_='t-14 t-normal')
    degree=degree_span.find_next('span',class_='visually-hidden')
    print("Institute: "+institute.text)
    print("Degree: "+degree.text)

# closing the driver
time.sleep(5)
driver.quit()

