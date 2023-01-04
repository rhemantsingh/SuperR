from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, pickle
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

sleep(1.5)
shoes_data = driver.find_elements(By.XPATH, "//*[@data-component-type='s-search-result']")
print("First pages link:-")
print(len(shoes_data))

shoes_link = []

for shoe in shoes_data:
    # print(i)
    # print(shoe.text)
    links = shoe.find_elements(By.TAG_NAME, "a")
    link = links[-1].get_attribute("href")
    shoes_link.append(link)

print("Same as above 'i think'")
print(len(shoes_link))

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
pName = []
pPrice = []
pSpec = []
pMRP = []
pImage = []
pColor = []
pCategory = []
pSubcategory = []
pLink = []
limit = len(shoes_link)
count = 0
for pqr in shoes_link:

    driver.get(pqr)
    print(count)

    if count < limit:
        Rdata = driver.find_elements(By.XPATH, "//*[@class='a-carousel-card']")

        i = 0
        for sh in Rdata:
            #print(i)
            # print(shoe.text)
            links = sh.find_elements(By.TAG_NAME, "a")
            shoes_link.append(links[-1].get_attribute("href"))
            i += 1
    count = count + 1

    try:
        WebDriverWait(driver, 2).until(
                   EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="inline-twister-expanded-dimension-text-color_name"]')))
        color = driver.find_element(By.XPATH,'//*[@id="inline-twister-expanded-dimension-text-color_name"]').text
    except:
        color = "None"
    try:
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[3]/span/a')))
        category = driver.find_element(By.XPATH, '//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[3]/span/a').text
    except:
        category = "None"
    try:
        WebDriverWait(driver, 2).until(
                   EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[7]/span/a')))
        subcat = driver.find_element(By.XPATH,'//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[7]/span/a').text
    except:
        subcat = "None"
    print(f"Color={color} ./... Category: {category} ....Sub-cat={subcat}")
    try:
        image = driver.find_element(By.XPATH, "//*[@id='landingImage']")
        i = image.get_attribute("src")
    except:
        i = "None"
    print('\n' + i)
    try:
        name = driver.find_elements(By.XPATH, '//*[@id="productTitle"]')[0].text
        print("Name : " + name)
    except:
        name = "None"
    try:
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[2]/span[2]/span[2]")))
        price = driver.find_elements(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')[0].text

    except:
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[1]/td[2]/span[1]/span[3]/span[2]')))

            price = driver.find_elements(By.XPATH,
                                     '//*[@id="corePrice_desktop"]/div/table/tbody/tr[1]/td[2]/span[1]/span[3]/span[2]')[0].text
        except:
            try:
                WebDriverWait(driver, 2).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[2]/span[2]/span[2]")))

                price = driver.find_elements(By.XPATH,
                                             "//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[2]/span[2]/span[2]")[0].text
            except:
                price = None

    try:
        print(f"Price : {price}")
    except:
        price = "None"
        print("None")
    try:
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='corePriceDisplay_desktop_feature_div']/div[2]/span/span[1]/span/span[2]")))
        mrp_price = driver.find_elements(By.XPATH, "//*[@id='corePriceDisplay_desktop_feature_div']/div[2]/span/span[1]/span/span[2]")[0].text

    except:
        mrp_price = "None"

    print(f"MRP RPice: {mrp_price}")
    sp=[]
    try:
        specs = driver.find_elements(By.XPATH, "//*[@id='feature-bullets']/ul/li")
        for s in specs:
            sp.append(s.text)
            print(s.text)
    except:
        sp.append("None")

    pName.append(name)
    pImage.append(i)
    pColor.append(color)
    pCategory.append(category)
    pSubcategory.append(subcat)
    pLink.append(pqr)
    pPrice.append(price)
    pMRP.append(mrp_price)
    pSpec.append(sp)

shoesDict={
        "Name": pName,
        "Image": pImage,
        "Link": pLink,
        "Price": pPrice,
        "MRP": pMRP,
        "Specification": pSpec,
        "Color": pColor,
        "Category": pCategory,
        "Subcategory": pSubcategory
    }
print(shoesDict["Name"], shoesDict["Image"], shoesDict["Link"], shoesDict["Price"], shoesDict["MRP"], shoesDict["Specification"])

with open("ShoesData", "ab") as f:
    pickle.dump(shoesDict, f)
print(len(shoes_link))

driver.close()
