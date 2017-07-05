import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains



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
ac.move_to_element(region_click).move_by_offset(6, -10) #Use this offset to locate the accurate latitude and longitude
ac.click()
ac.perform()

time.sleep(2)

#Click on the 'Get Trend'
get_trend = driver.find_element_by_xpath('//*[@id="chicken_contentDiv"]/table/tbody/tr[5]/td/a/b')
get_trend.click()

# time.sleep(5)
# driver.quit()