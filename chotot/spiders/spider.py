import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logzero import logfile,logger
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
        desired_capabilities = options.to_capabilities()
        driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
        driver.get("https://nha.chotot.com/toan-quoc/mua-ban-can-ho-chung-cu")

        driver.implicitly_wait(30)

        wait = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,"_3fPtx0mYb_kcS1PSL3lwFA")))

        # button = driver.find_elements_by_class_name("sc-jlyJG jJyZjN")
        # button.click()
        # time.sleep(10)

        # urls = driver.find_elements_by_class_name("_3fPtx0mYb_kcS1PSL3lwFA")
        # for url in urls:
        #     link = url.get_atrribute("href")
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


        driver.quit()

