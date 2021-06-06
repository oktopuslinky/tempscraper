'''
NOTES:
The website you are trying to scrape from has been coded in angular, which is why you will not be able to easily scrape with BeautifulSoup.
Instead, use selenium.

HELPFUL LINKS:
https://www.youtube.com/watch?v=QoyIWDKrWU0
for selenium^^

https://www.wunderground.com/history/monthly/us/tx/austin/KAUS/date/2010-10
page to scrape from^^

https://selenium-python.readthedocs.io/getting-started.html
selenium documentation^^
'''

'''
As of now, the data for highs is being fetched.

TODO
- Fetch data for other years (search using search bar, automate this process)
- Fetch data for lows
- Average the highs and lows
- Get this data into lists and plot
- Analyze trends

'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
import time
import sys

url = "https://www.usclimatedata.com/climate/austin/texas/united-states/ustx2742"

chrome_driver_path = "/Users/devag/OneDrive/Documents/ESS IA/tempscraper/chromedriver"

chrome_options = Options()
chrome_options.add_argument("window-size=1200x600")
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome('./chromedriver', options=chrome_options)


webdriver = webdriver.Chrome(
    executable_path = chrome_driver_path,
    options = chrome_options
)

# default search query
search_query = "March 2011"



if len(sys.argv) >= 2:
    search_query = sys.argv[1]
    #print(search_query)




with webdriver as driver:
    # timeout
    wait = WebDriverWait(driver, 10)

    # retriever data
    driver.get(url)

    
    # find selection
    #search = driver.find_element_by_id("tDatepicker")
    #search.send_keys(search_query + Keys.RETURN)

    goto_history = driver.find_element_by_id("history-tab").click()
    the_input = driver.find_element_by_id("year_month_selector")

    '''
    the_input.click()
    for i in range(13):
        the_input.send_keys(Keys.BACKSPACE)
    '''

    the_input.send_keys(Keys.BACKSPACE*13 + search_query + Keys.RETURN)

    time.sleep(2)

    results = driver.find_elements_by_class_name("high.text-right")
    #print(results)
    for ind_res in results:
        print(ind_res.text)
        #res_arr = ind_res.text.split('\n')
        #print(res_arr)
      
    #goto_history.send_keys(Keys.RETURN)
    
    my = driver.find_elements_by_class_name("history_month_year_name")
    for data in my:
        print(data.text)

    # wait

    #wait.until(presence_of_all_elements_located(By.ID, "results_area"))
    '''
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.Id, "year_month_selector"))
        )
    except:
        print("element not found")
    finally:
        search = driver.find_element_by_id("year_month_selector")
        print("vis: " + str(search.is_displayed()))

        search.send_keys(search_query + Keys.RETURN)

    #time.sleep(10)

    results = driver.find_elements_by_tag_name("td")

    for quote in results:
      quoteArr = quote.text.split('\n')
      print(quoteArr)
      print()
    '''
    driver.close()