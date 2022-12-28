from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep

chromePath = os.getcwd() + "/chromedriver.exe"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--mute-audio")
# chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

driver = webdriver.Chrome(chromePath)
#
# ##Starting

driver.get("https://www.amazon.in/")

sleep(2)
driver.maximize_window()
search = driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']")
search.send_keys("shoes")
search.send_keys(Keys.ENTER)
#print(driver.current_window_handle)

sleep(2)
shoes_data = driver.find_elements(By.XPATH, "//*[@data-component-type='s-search-result']")
print(len(shoes_data))

shoes_link=[]
i = 1
for shoe in shoes_data:
    # print(i)
    # print(shoe.text)
    links = shoe.find_elements(By.TAG_NAME, "a")
    link = links[-1].get_attribute("href")
    shoes_link.append(link)
    i += 1

print(shoes_link)
#
#
#
# all_links=[]
# #recomedation Shoes
# for j in range(0,60):
#     driver.get(shoes_link[j])
#     Rdata = driver.find_elements(By.XPATH, "//*[@class='a-carousel-card']")
#     #print(len(Rdata))
#     i = 0
#     for shoe in Rdata:
#         # print(i)
#         # print(shoe.text)
#         links = shoe.find_elements(By.TAG_NAME, "a")
#         all_links.append(links[-1].get_attribute("href"))
#         i+= 1
# print(len(all_links))
# for l in all_links:
#     print(l)
# print(len(set(all_links)))
#Profile
for pqr in range(0,5):
    driver.get(shoes_link[pqr])
    print(pqr)
    print(shoes_link[pqr])

    image = driver.find_element(By.XPATH, "//*[@id='landingImage']")
    i = image.get_attribute("src")
    print(i)
    name=driver.find_elements(By.XPATH, '//*[@id="productTitle"]')
    print(name[0].text)
    try:
        price=driver.find_elements(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')


    except:
        price = driver.find_elements(By.XPATH,
                                     '//*[@id="corePrice_desktop"]/div/table/tbody/tr[1]/td[2]/span[1]/span[3]/span[2]')
    try:
        print(price[0].text)
    except:
        print(None)
    try:
        mrp_price=driver.find_elements(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[2]/span/span[1]/span/span[2]')
        print(mrp_price[0].text)
    except:
        mrp_price=None
        print(mrp_price)

    specs = driver.find_elements(By.XPATH, "//*[@id='feature-bullets']/ul/li")
    for s in specs:
        print(s.text)

    try:
        rating = driver.find_element(By.XPATH, '//*[@id="acrPopover"]')
        print(rating[0].text)
    except:
        print("rating cannot be found")





driver.close()
