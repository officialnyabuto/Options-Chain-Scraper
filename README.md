﻿**Option Chain Scraper**

**Introduction**

This Python script is designed to scrape option chain data from the National Stock Exchange of India (NSE) website using Selenium and Beautiful Soup. The script allows the user to select an index (currently NIFTY or BANKNIFTY), and then choose to extract option chain data either by strike price or by expiration date. The script saves the extracted data as a Pandas DataFrame and provides an option to download the data as a CSV file.

**Dependencies**

This script requires the following dependencies:

- Python 3
- Selenium
- Beautiful Soup 4
- Pandas
- Chrome webdriver (you need to install a compatible version of the Chrome webdriver and add its location to your system PATH)

**Installation**

1. Clone the repository to your local machine
1. Install the dependencies using pip: **pip install -r requirements.txt**
1. Download and install a compatible version of the Chrome webdriver: <https://sites.google.com/a/chromium.org/chromedriver/downloads>
1. Add the location of the Chrome webdriver executable to your system PATH variable

**Usage**

1. Open the **option\_chain\_scraper.py** script in a text editor
1. Set the desired index and filter type in the **INDEX** and **filter** variables, respectively
1. If using the **strike** filter, set the desired strike price in the **strike\_price** variable
1. If using the **exp\_date** filter, set the desired expiration date in the **exp\_date** variable
1. Run the script using the command **python option\_chain\_scraper.py**
1. The script will scrape the data and save it as a Pandas DataFrame, which can be accessed using the variable **df**
1. If using the **strike** filter, the script will also download the data as a CSV file

**Example**

Here is an example of how to use the script to extract option chain data for NIFTY with a strike price of 17100:

from option\_chain\_scraper import get\_option\_chain\_data, get\_options\_by, page\_inits

import pandas as pd

INDEX = 'NIFTY'

filter\_type = 'strike'

strike\_price = 17100.00

driver = page\_inits(index=INDEX)

options = get\_options\_by(driver, filter\_type=filter\_type, strike\_price=strike\_price)

\# Wait for the content to be updated

WebDriverWait(driver, 10).until(

`    `EC.text\_to\_be\_present\_in\_element((By.XPATH, "//span[@id='chBox']"), strike\_price)

)

\# Click on the download link

download\_link = driver.find\_element(By.ID, 'download\_csv')

download\_link.click()

\# Retrieve page source using Selenium and parse with BeautifulSoup

page\_source = driver.page\_source

df = get\_option\_chain\_data(page\_source)

\# Print the DataFrame

print(df)
