Option Chain Scraper
Introduction
This Python script is designed to scrape option chain data from the National Stock Exchange of India (NSE) website using Selenium and Beautiful Soup. The script allows the user to select an index (currently NIFTY or BANKNIFTY), and then choose to extract option chain data either by strike price or by expiration date. The script saves the extracted data as a Pandas DataFrame and provides an option to download the data as a CSV file.

Dependencies
This script requires the following dependencies:

Python 3
Selenium
Beautiful Soup 4
Pandas
Chrome webdriver (you need to install a compatible version of the Chrome webdriver and add its location to your system PATH)
Installation
Clone the repository to your local machine
Install the dependencies using pip: pip install -r requirements.txt
Download and install a compatible version of the Chrome webdriver: https://sites.google.com/a/chromium.org/chromedriver/downloads
Add the location of the Chrome webdriver executable to your system PATH variable
Usage
Open the option_chain_scraper.py script in a text editor
Set the desired index and filter type in the INDEX and filter variables, respectively
If using the strike filter, set the desired strike price in the strike_price variable
If using the exp_date filter, set the desired expiration date in the exp_date variable
Run the script using the command python option_chain_scraper.py
The script will scrape the data and save it as a Pandas DataFrame, which can be accessed using the variable df
If using the strike filter, the script will also download the data as a CSV file
Example
Here is an example of how to use the script to extract option chain data for NIFTY with a strike price of 17100:
from option_chain_scraper import get_option_chain_data, get_options_by, page_inits
import pandas as pd

INDEX = 'NIFTY'
filter_type = 'strike'
strike_price = 17100.00

driver = page_inits(index=INDEX)
options = get_options_by(driver, filter_type=filter_type, strike_price=strike_price)

# Wait for the content to be updated
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, "//span[@id='chBox']"), strike_price)
)

# Click on the download link
download_link = driver.find_element(By.ID, 'download_csv')
download_link.click()

# Retrieve page source using Selenium and parse with BeautifulSoup
page_source = driver.page_source
df = get_option_chain_data(page_source)

# Print the DataFrame
print(df)
