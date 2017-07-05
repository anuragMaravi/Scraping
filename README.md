# Scraping
The basic web scraping python script using selenium and chromedriver. 

## Getting Started

This script is used for extracting the data from an Interactive Graph.


### Installing Selenium

If you already have 'pip' installed on your system, just use to install selenium

```
pip install -U selenium
```

### Downloading Chromedriver

Download the of latest release of chromedriver for your system

[chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### Path for chromedriver

You need to make sure the standalone ChromeDriver binary (which is different than the Chrome browser binary) is either in your path or available in the webdriver.chrome.driver environment variable.

Or 

You can use the chromedriver directly from the downloads 

```
chromedriver = "/Users/anuragmaravi/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
```
But its better if you put it in the correct path

## Testing

To test selenium just use the following code:

```
import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
```
