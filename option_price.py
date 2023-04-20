from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.nseindia.com/option-chain'
INDEX = 'NIFTY'
# INDEX = 'BANKNIFTY'

def page_inits(index='NIFTY'):

    # Create a Chrome webdriver instance
    driver = webdriver.Chrome()

    # Load the options chain URL
    driver.get(URL)

    # Select the desired index from the dropdown menu
    index_dropdown = driver.find_element(By.ID, 'equity_optionchain_select')
    index_dropdown.click()
    index_option = driver.find_element(By.XPATH, f"//option[@value='{index}']")
    index_option.click()

    return driver


def get_option_chain_data(html_source):
    soup = BeautifulSoup(html_source, 'html.parser')
    option_chain = soup.find("table", {"id": "optionChainTable-indices"})
    
    # Get the table header
    header = option_chain.find("thead")
    header_rows = header.find_all("tr")
    headers = [th.text.strip() for th in header_rows[1].find_all("th")]

    # Get all the table rows
    rows = option_chain.find_all("tr")

    # Extract the table data into a list of lists
    data = []
    for row in rows:
        cells = row.find_all("td")
        if not cells:
            continue
        data.append([cell.text.strip() for cell in cells])

    # Create a DataFrame with the table data and headers
    df = pd.DataFrame(data, columns=headers)
    
    return df


def get_options_by(filter='strike'):
    if filter=='strike':
        # Select the desired strike price from the dropdown menu
        strike_price_dropdown = driver.find_element(By.ID, 'strikeSelect')
        strike_price_dropdown.click()
        # Get all the strike price options
        strike_price_options = strike_price_dropdown.find_elements(By.TAG_NAME, 'option')
        time.sleep(3)
        options= strike_price_options

        # Print the strike price values
        for option in options:
            value = option.get_attribute('value')
            if not value:
                # Skip over empty option values
                continue

            try:
                value = float(value.replace(',', ''))
            except ValueError:
                print(f"Error: Invalid value '{value}' found in strike price options")
                continue

            if value == strike_price:
                print(option.get_attribute('value'))
                option.click()

                time.sleep(3)
                # Retrieve page source using Selenium and parse with BeautifulSoup
                page_source = driver.page_source
                df = get_option_chain_data(page_source)
                print(df)
                break

    if filter=='exp_date':
        # Select the desired EXP.DATE from the dropdown menu
        exp_date_dropdown = driver.find_element(By.ID, 'expirySelect')
        exp_date_dropdown.click()
        # Get all the EXP.DATE options
        exp_date_options = exp_date_dropdown.find_elements(By.TAG_NAME, 'option')
        time.sleep(2)
        # exp_date_dropdown = driver.find_element(By.ID, 'dateSelect')
        options= exp_date_options

        # Print the strike price values
        for option in options:
            value = option.get_attribute('value')
            if not value:
                # Skip over empty option values
                continue

            if value == exp_date:
                print(option.get_attribute('value'))
                option.click()

                # Retrieve page source using Selenium and parse with BeautifulSoup
                page_source = driver.page_source
                df = get_option_chain_data(page_source)
                print(df)

strike_price = 17100.00
# exp_date = '20-Apr-2023'
driver = page_inits()
options = get_options_by(filter='strike')

try:
    # Wait for the content to be updated
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//span[@id='chBox']"), strike_price)
    )

    # Click on the download link
    download_link = driver.find_element(By.ID, 'download_csv')
    download_link.click()

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Close the webdriver instance
    driver.quit()
