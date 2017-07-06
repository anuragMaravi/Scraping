import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import pandas as pd


print "Scarping Started"
driver = webdriver.Chrome()
driver.get('http://bhuvan.nrsc.gov.in/nices/#InteractiveView') #Url for the site to scrape

# Clicking the button "Hydrological fluxes at 0.15"
hydro_button = driver.find_element_by_id('bg-torq')
hydro_button.click()
time.sleep(5) # Use it when the page is loaded slow

#Selecting Interactive and trend 
interactive_click = driver.find_element_by_xpath('//p[@id="t1112" and @class="l2heading"]')
interactive_click.click()

#Selecting from the dropdown
select = Select(driver.find_element_by_id('prdlist'))
select.select_by_value('sm')

time.sleep(2)

#Select a region from the map
region_click = driver.find_element_by_xpath('//*[@id="OpenLayers_Layer_WMS_39"]/img[2]')
# location = region_click.location
# print location
ac = ActionChains(driver)
ac.move_to_element(region_click).move_by_offset(5, -10) #Use this offset to locate the accurate latitude and longitude
ac.click()
ac.perform()

time.sleep(5)

#Click on the 'Get Trend'
get_trend = driver.find_element_by_xpath('//*[@id="chicken_contentDiv"]/table/tbody/tr[5]/td/a/b')
get_trend.click()

time.sleep(25)

#Hover over the trend
trend = driver.find_element_by_xpath('//*[@id="stepplot"]/div/canvas[2]')
ac2 = ActionChains(driver)
ac2.move_to_element(trend)
ac2.move_to_element(trend)

# Use X = -186 for Start date
# Use X = 215 for End Date
date_range = np.arange(-186, 215, 1) #Set the start and end date here
data = []
list_reading = []
print "Reading Data"
for i in date_range:
	ac2.move_to_element(trend).move_by_offset(i, 0)
	ac2.perform()
	#Xpath for getting readings
	reading = driver.find_element_by_xpath('//*[@id="stepplot"]/div/div[2]')
	print reading.text
	date, moisture = reading.text.split(': Surface Soil Moisture: ', 1)
	data.append([date, float(moisture)])


#Use data to do something
print "Scraping Completed"

print "Creating CSV"
df = pd.DataFrame(data, columns=['Date','Soil Moisture'])
df.to_csv('soil.csv', index = False)
print "csv created as: soil.csv"

driver.quit()


