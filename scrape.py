import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://bhuvan.nrsc.gov.in/nices/#InteractiveView');
time.sleep(5)

# Clicking the button "Hydrological fluxes at 0.15"
hydro_button = driver.find_element_by_id('bg-torq')
hydro_button.click()

time.sleep(5)
driver.quit()