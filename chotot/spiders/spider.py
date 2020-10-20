import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logzero import logfile,logger
from bs4 import BeautifulSoup
import json
import time

class muaBanCHCCSpider(scrapy.Spider):
    logfile("muaBanCHCCSpider.log",maxBytes=1e6, backupCount=3)
    name = 'muaBanCHCC_spiders'
    allowed_domains = ["toscrape.com"]

    def start_requests(self):
        url = "http://quotes.toscrape.com"
        yield scrapy.Request(url=url, callback=self.parse_muaban1)

    def parse_muaban1(self,response):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--start-maximized")
        desired_capabilities = options.to_capabilities()
        driver = webdriver.Chrome(desired_capabilities=desired_capabilities,executable_path="C:/Windows/chromedriver.exe")
        #driver = webdriver.Chrome(executable_path="C:/Windows/chromedriver.exe")
        driver.get("https://nha.chotot.com/toan-quoc/mua-ban-can-ho-chung-cu")

        #https://gateway.chotot.com/v1/public/ad-listing?cg=1000&limit=20&o=1000&st=s,k&page=51
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tooltip_btn_save_search"]/div[4]'))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="regionRef"]/div'))).click()
        
        driver.implicitly_wait(10)

        soup = BeautifulSoup(driver.page_source,"lxml")
        urls = soup.find_all("a", {"class": "sc-jDwBTQ hsqXiD"})
        base_url = ''
        for url in urls:
            print(url.get('href'))
            yield scrapy.Request(url=url, callback=self.parse_muaban1)

        # with open("source.html", "w", encoding='utf-8') as f:
        #     f.write(driver.page_source)
        # wait = WebDriverWait(driver, 5)
        # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sc-jDwBTQ hsqXiD")))
        # urls = driver.find_elements_by_class_name("sc-jDwBTQ hsqXiD")
        # urls_list = []
        # for url in urls:
        #     urls_list.append(url.get_atrribute("href"))
        #driver.quit()
        # Write countries_list to json file
        # with open("urls_list.json", "w") as f:
        #     json.dump(urls_list, f)

        #urls = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "sc-jDwBTQ hsqXiD")))

        # urls = driver.find_elements_by_class_name("_3qr34_XMQROJG0YnuXtt9c")
        # self.log(type(urls))
        # self.log(len(urls))

        #driver.implicitly_wait(30)
        
        
        #a = driver.find_element_by_xpath('//*[@id="regionRef"]/div[2]/div/ul/li/div/a')
        #urls = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sc-jDwBTQ hsqXiD")))
        #urls = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.CLASS_NAME,"sc-jDwBTQ hsqXiD"))
        #urls = driver.find_elements_by_class_name("sc-jDwBTQ hsqXiD")
        #self.log(type(a))
        #self.log(type(urls))
        #self.log(len(urls))
        #self.log(a.get_attribute('href'))
        # urls = driver.find_element_by_xpath('//*[@id="regionRef"]/div[2]/div/ul/li/div/a')
        #time.sleep(20)
        # button = driver.find_elements_by_class_name("sc-jlyJG jJyZjN")
        # button.click()
        # time.sleep(10)
        # btn = driver.find_element_by_xpath('//*[@id="app"]/header/div[1]/div[2]/div[5]/a/span')
        # btn.click()
        # 
        #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sc-jDwBTQ hsqXiD")))
        #urls = driver.find_elements_by_class_name("sc-jDwBTQ hsqXiD")
        #self.log(element)
        # for url in urls:
        #     link = url.get_atrribute("href")
        #     self.log(link)
        #     yield {
        #         "url": link,
        #     }

        # nhaban = driver.find_elements_by_class_name("ctAdListingBody")
        # nhaban_count = 0
        # for nha in nhaban:
        #     yield {
        #         "nha": nha.text,
        #     }
        #     nhaban_count +=1


        #driver.quit()

