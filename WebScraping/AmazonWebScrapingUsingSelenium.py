from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import csv
import time

url = "https://www.amazon.com/s?k=earrings"

service = Service("C:/Users/HP/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url)

time.sleep(3)  # allow page to load

products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
print("Products found:", len(products))

productList = []

for product in products:
    data = {}

    try:
        data['productTitle'] = product.find_element(By.XPATH, './/h2/span').text
    except:
        data['productTitle'] = None

    try:
        data['url'] = product.find_element(By.XPATH, './/h2/a').get_attribute('href')
    except:
        data['url'] = None

    try:
        data['img'] = product.find_element(By.XPATH, './/img').get_attribute('src')
    except:
        data['img'] = None

    try:
        data['price'] = product.find_element(By.XPATH, './/span[@class="a-price-whole"]').text
    except:
        data['price'] = None

    productList.append(data)

filename = "WebScraping/amazon_earrings.csv"

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['productTitle', 'url', 'img', 'price'])
    writer.writeheader()
    writer.writerows(productList)

    driver.quit()
