from __future__ import absolute_import
import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import urllib
import json
import datetime

import psycopg2
from sshtunnel import SSHTunnelForwarder
import sys


class muaBanBdsSpider(scrapy.Spider):
    name = 'muabanbds'
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://nha.chotot.com",
        "pragma": "no-cache",
        "referer": "https://nha.chotot.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }

    base_url = 'https://gateway.chotot.com/v1/public/ad-listing'
    def __init__(self, conn):
        self.filename ='./output/muaban_' + datetime.datetime.today().strftime('%Y-%m-%d-%H-%M') + '.jsonl'
        self.conn = conn
    
    def start_requests(self):
        query_string_params = '?cg=1000&st=s,k&limit=50&key_param_included=true'
        yield scrapy.Request(
            url=self.base_url + query_string_params,
            method='GET',
            headers=self.headers,
            callback=self.parse_page
        ) 

    def parse_page(self, response):
        data = json.loads(response.body)
        total_ads = 0
        if ('total' in data.keys()):
            if(int(data['total'])>0):
                total_ads = data['total']
            else:
                return
        number_page = round(total_ads/50)
        number_page = 1
        for page in range(1,number_page+1):
            query_string_params ='?cg=1000&st=s,k&o={}&page={}&limit=50&key_param_included=true'.format((page-1)*50,page)
            yield response.follow(
                    url=self.base_url + query_string_params,
                    method='GET',
                    headers=self.headers,
                    callback=self.parse_ads
                )
    def parse_ads(self, response):
        data = json.loads(response.body)
        for ad in data['ads']:
            yield response.follow(
                url=self.base_url+ "/" + str(ad['list_id']),
                method='GET',
                headers=self.headers,
                callback=self.parse_ad_detail,
                )

    def parse_ad_detail(self, response):
        data = json.loads(response.body)
        ad_data = {
            'list_id' :'Null',
            'list_time' :'Null',
            'account_name' :'Null',
            'phone' :'Null',
            'body' :'Null',
            'category_name' :'Null',
            'images' :'Null',
            'price_string' :'Null',
            'price' :'Null',
            'type_name' :'Null',
            'ward' :'Null',
            'size' :'Null',
            'price_m2' :'Null',
            'rooms' :'Null',
            'toilets' :'Null',
            'floors' :'Null',
            'property_legal_document' :'Null',
            'area' :'Null',
            'region' :'Null',
            'address' :'Null',
            'house_type' :'Null',
            'furnishing_sell' :'Null',
            'width' :'Null',
            'length' :'Null',
            'living_size':'Null'
        }
        
        ad_data1 = { 'list_id': str(data['ad']['list_id']),
            'list_time': str(data['ad']['list_time']),
           'account_name':data['ad']['account_name'],
           'phone' :str(data['ad']['phone']),
           'body':data['ad']['body'],
           'category_name':data['ad']['category_name'],
           'images': json.dumps(data['ad']['images']),
           'price_string':data['ad']['price_string'],
           'price':str(data['ad']['price']),
           'type_name': data['ad']['type_name'],
          }
        

        for e in data['parameters']:
            if e['id'] != None and e['value']!=None:
                ad_data1[e['id']] = str(e['value'])

        for e in ad_data1.keys():
            if e in ad_data.keys():
                ad_data[e] = ad_data1[e]
        value =()

        for e in ad_data.keys():
            if e=='images':
                value += ('day la images',)
            else:
                value += (ad_data[e],)
        # print(len(value))
        cur = self.conn.cursor()
        sql = """INSERT INTO CHOTOT_MUBAN(list_id,
                                list_time ,
                                account_name ,
                                phone ,
                                body ,
                                category_name ,
                                images ,
                                price_string ,
                                price ,
                                type_name ,
                                ward ,
                                size ,
                                price_m2 ,
                                rooms ,
                                toilets ,
                                floors ,
                                property_legal_document ,
                                area ,
                                region ,
                                address ,
                                house_type ,
                                furnishing_sell ,
                                width ,
                                length ,
                                living_size) 
                                VALUES (%s,%s,%s,%s,%s,
                                        %s,%s,%s,%s,%s,
                                        %s,%s,%s,%s,%s,
                                        %s,%s,%s,%s,%s,
                                        %s,%s,%s,%s,%s);"""

        cur.execute(sql,value)
        self.conn.commit()
        cur.execute("rollback")
        self.conn.commit()
        cur.close()
        # with open("abc.json" ,"a") as f:
        #     f.write(json.dumps(ad_data) + '\n')

if __name__ == '__main__':
    # For interactive work (on ipython) it's easier to work with explicit objects
    # instead of contexts.

    # Create an SSH tunnel
    tunnel = SSHTunnelForwarder(
        ('45.119.81.84', 22),
        ssh_username='root',
        #ssh_private_key='</path/to/private/key>',
        ssh_password='qW7iO2Tgt1Tw',
        remote_bind_address=('localhost', 5432),
        local_bind_address=('localhost', 6543), # could be any available port
    )
    # Start the tunnel
    tunnel.start()

    try:
        # Create a database connection
        conn = psycopg2.connect(
        database='postgres',
        user='vtttuong', 
        password='Tuongro26**',  
        host=tunnel.local_bind_host,
        port=tunnel.local_bind_port,
        )

        process = CrawlerProcess()
        process.crawl(muaBanBdsSpider, conn)
        process.start()

    except (psycopg2.OperationalError, Exception, psycopg2.DatabaseError) as e:
        print('Unable to connect!\n{0}'.format(e))
        sys.exit(1)
    else:
        print('Connected!')
    finally:
        if conn is not None:
            print('Closed !!!')
            conn.close()
        tunnel.stop()

        
