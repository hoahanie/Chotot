import psycopg2
from sshtunnel import SSHTunnelForwarder
import sys

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

# Create a database connection

try:
    conn = psycopg2.connect(
    database='postgres',
    user='vtttuong', 
    password='Tuongro26**',  
    host=tunnel.local_bind_host,
    port=tunnel.local_bind_port,
    )
    cur = conn.cursor()
    # cur.execute("""CREATE TABLE CHOTOT_MUBAN(
    #                 list_id VARCHAR(100) PRIMARY KEY NOT NULL,
    #                 list_time ,
    #                 account_name VARCHAR(50) NULL,
    #                 phone ,
    #                 body TEXT NULL,
    #                 category_name ,
    #                 images TEXT NULL,
    #                 price_string ,
    #                 price ,
    #                 type_name ,
    #                 ward ,
    #                 size ,
    #                 price_m2 ,
    #                 rooms ,
    #                 toilets ,
    #                 floors ,
    #                 property_legal_document ,
    #                 area ,
    #                 region ,
    #                 address VARCHAR(500) NULL,
    #                 house_type ,
    #                 furnishing_sell ,
    #                 width ,
    #                 length ,
    #                 living_size VARCHAR(100) NULL
    #                 );
    #             """)
    # conn.commit()

    # sql = """
    # INSERT INTO CHOTOT_MUBAN(list_id,
    #                 list_time ,
    #                 account_name ,
    #                 phone ,
    #                 body ,
    #                 category_name ,
    #                 images ,
    #                 price_string ,
    #                 price ,
    #                 type_name ,
    #                 ward ,
    #                 size ,
    #                 price_m2 ,
    #                 rooms ,
    #                 toilets ,
    #                 floors ,
    #                 property_legal_document ,
    #                 area ,
    #                 region ,
    #                 address ,
    #                 house_type ,
    #                 furnishing_sell ,
    #                 width ,
    #                 length ,
    #                 living_size)
    # VALUES ('79261975', 
    #         '1605254987841', 
    #         'Cô Sa', 
    #         '0933858509', 
    #         'Nhà 2 mặt tiền gốc Phú Thọ Hoà và Luỹ Bán Bích. Gồm 2 căn nhà liền kề 4 tấm và 3 kiot đang cho thuê ( thu nhập ổn định). Thích hợp làm ngân hàng và văn phòng.... . Gần UBND quận Tân Phú, bệnh viện Tân Phú.', 
    #         'Nhà ở', 
    #         array_to_string(ARRAY['https://cdn.chotot.com/R6_dzFSFR0vmzsoWWpD_IMxguhWt4meqktv7fU0noEM/preset:view/plain/0573d8d42977c4e38e33069f84281b38-2692585483040891025.jpg', 'https://cdn.chotot.com/CBducLiFhMo1R_wST3ShCVZBVxnQKPs5dVALJibCDes/preset:view/plain/3ffdeaf04cecb930ccb8954ba89b9479-2692585483027166753.jpg', 'https://cdn.chotot.com/tBEQuNhGGRoJoGxR3ZQm0OV_mM_02_UdAoxt1B5xPT4/preset:view/plain/33f964744a2ad2fae2b69472a1ea60f1-2692585482965976042.jpg', 'https://cdn.chotot.com/rIMYSE8yripcXygn39g33OleFBmhFQ31y-K3WuTt-N4/preset:view/plain/6699f244aa3fea428c2f7cc607cb35c7-2692585483041184360.jpg'], ',', '*'), 
    #         '50 tỷ', 
    #         '50000000000', 
    #         'Cần bán', 
    #         'Phường Phú Thọ Hòa', 
    #         '200 m2', 
    #         '250 triệu/m2', 
    #         '8 phòng', 
    #         'Nhiều hơn 6 phòng', 
    #         '4', 
    #         'Đã có sổ', 
    #         'Quận Tân Phú', 
    #         'Tp Hồ Chí Minh', 
    #         '729, Luỹ Bán Bích, Phường Phú Thọ Hòa, Quận Tân Phú, Tp Hồ Chí Minh', 
    #         'Nhà mặt phố, mặt tiền', 
    #         'Nội thất đầy đủ', 
    #         '10 m', 
    #         '20 m', 
    #         '200 m2');
    #         """
    sql = """
    INSERT INTO CHOTOT_MUBAN(list_id,
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
    VALUES ('79157304','1605363021571','Nguy\u1ec5n v\u0103n \u0111\u1ea1t','0376978065','Nh\u00e0 s\u1ed5 chung , 1 l\u1ea7u tr\u1ec7t , 1 l\u1ea7u , \u0111\u01b0\u1eddng tpk 30 , s\u00e1t \u0111\u01b0\u1eddng nh\u1ef1a , nh\u00e0 2 m\u1eb7t ti\u1ec1n \u0111\u01b0\u1eddng b\u00ea t\u00f4ng 5m, c\u00e1ch \u0111\u01b0\u1eddng nh\u1ef1a 20m, 2 p ng\u1ee7 , 2 wc, , \u0111\u01b0\u1eddng b\u00ea t\u00f4ng cao r\u00e1o s\u1ea1ch \u0111\u1eb9p,  dt 5,1x8, h\u00ecnh ch\u1ee5p th\u1ef1c t\u1ebf, gi\u00e1 m\u1ec1n nh\u1ea5t th\u1ecb tr\u01b0\u1eddng, lh e xem nh\u00e0','Nh\u00e0 \u1edf',array_to_string(ARRAY['https://cdn.chotot.com/o9N7rfsUJXz9Tu3qv3m1vCCDRkuzYy6jHmmLZY61hIQ/preset:view/plain/c7b014ea00c31dd78d99bc4da60cfcc8-2692155339679817929.jpg', 'https://cdn.chotot.com/ESUq0NhxUaAtOiabjpf1mUQa1WXlY_1Rmup1oUeZPL0/preset:view/plain/ea28ca227b0d515357d0fd55a240cc1c-2692155339836713815.jpg', 'https://cdn.chotot.com/0Gjci-9f1aBRmyP80bL1ecoPOgEfF0sDlB8ltsRAJE8/preset:view/plain/f5877b35a1c27fad498471e5d1caee2f-2692155340675520305.jpg', 'https://cdn.chotot.com/ZBMW-5KsfZ61ctK1XUrYIqkEsddOOT8F8lcA3E5o4o4/preset:view/plain/e5205e4e26facfaea27b621d4f890584-2692155340086211938.jpg', 'https://cdn.chotot.com/QRDcGKeVlim5yzsJti24spQizAVYQbYyS2dSkjsvCT4/preset:view/plain/5b27c3a37c2d3c82ab45c094a6205563-2692155339532693712.jpg', 'https://cdn.chotot.com/RsK73rQrJ55FTOKfcif0V6BL5CKlLrCmUALj2G-PT2g/preset:view/plain/6c36eb7d272b45837d83597961c5b595-2692155339065408361.jpg', 'https://cdn.chotot.com/HlfmCY_-J6l0oVfdgz8CCxyKawqEtRG_3bzfYgkhJRI/preset:view/plain/848f747367a166724dd4b11185584cb9-2692155338381789332.jpg', 'https://cdn.chotot.com/JWEF1l-BjIOKZDhnG25xrZ3T055FmhcVD5xkbQTFpIg/preset:view/plain/fefaa993795fbb6c8406a65abbe3f7e3-2692155340764219540.jpg'],',','*'),'770 tri\u1ec7u','770000000','C\u1ea7n b\u00e1n','Ph\u01b0\u1eddng T\u00e2n Ph\u01b0\u1edbc Kh\u00e1nh','40 m\u00b2','19,25 tri\u1ec7u/m\u00b2','2 ph\u00f2ng','B\u1eafc','2 ph\u00f2ng','Gi\u1ea5y t\u1edd kh\u00e1c','H\u1ebbm xe h\u01a1i','Th\u1ecb x\u00e3 T\u00e2n Uy\u00ean','B\u00ecnh D\u01b0\u01a1ng','\u0110\u01b0\u1eddng T\u00e2n Ph\u01b0\u1edbc Kh\u00e1nh 30, Ph\u01b0\u1eddng T\u00e2n Ph\u01b0\u1edbc Kh\u00e1nh, Th\u1ecb x\u00e3 T\u00e2n Uy\u00ean, B\u00ecnh D\u01b0\u01a1ng','Nh\u00e0 ng\u00f5, h\u1ebbm','75 m\u00b2');
            """
    cur.execute(sql)
    conn.commit()

    cur.execute("select * from information_schema.tables")
    db_version = cur.fetchone()
    print(db_version)
    # execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)
       
	# close the communication with the PostgreSQL
    cur.close()
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
# Get a database cursor


# Get the result
# result = cur.fetchall()
# print(result)
# Close connections

# Stop the tunnel

# Alternatively use contexts..
# with SSHTunnelForwarder(...) as tunnel:
#     with psycopg2.connect(...) as connect:
#         cur = conn.cursor()
#         ...