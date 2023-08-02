from urllib import parse
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
from  openpyxl import load_workbook
import re
city_list = ['lf','yanjiao', 'beijing', 'dongcheng', 'xicheng', 'chaoyang', 'haidian', 'fengtai', 'shijingshan', 'tongzhou', 'changping', 'daxing',
              'yizhuangkaifaqu', 'shunyi', 'fangshan', 'mentougou', 'pinggu', 'huairou', 'miyun', 'yanqing'  ]
beijing = 'https://bj.ke.com/ershoufang/'
langfang = 'https://lf.ke.com/ershoufang/'
yanjiao = 'https://lf.ke.com/ershoufang/yanjiao'


#Mysql所在的主机名ip
HOST = '123.56.173.220'
#Mysql的端口号，默认3306
PORT = 7581
#连接Mysql的用户名
USER = 'easondbroot'
#连接数据库的密码
PASSWORD = parse.quote('JIL4zgd3uUKv@2022')
# PWD = parse.quote_plus(PASSWORD)
#MySQL上创建数据库名称
DATABASE = 'ry-vue'

# SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4"

app = Flask(__name__)
# app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4"
db = SQLAlchemy()
db.init_app(app)

#创建表
class SailRoom(db.Model):
    __tablename__ = 'sailed_room'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    city_name = db.Column(db.String(20), nullable = False)
    sailed_amount = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)


# with app.app_context():
#     db.create_all()
#shuomign
cookies = {
    'SECKEY_ABVK': 'vzULQcz14GsPelFDE1y2DYOWY0E4jeAsAFWawpXQ1jU%3D',
    'BMAP_SECKEY': '3eh45l3qdxgTdUMGSpxI3uD-QPDWWRGfqcVFvG7l31yEC21ONzIYKmCnl8pFxP8xPiDVT5tS7q9oI_2p38rbg0fK_ThS7DjIDDP9yRqT3vct3ea6lRWzyz-b26LweE_Zgh_rUXhR_TgWAuViiSZPZdKxjar_1KRaJa6X4zXb22yZG8mmSiV3PRFwBxiBTL1q',
    'lianjia_uuid': '965c5236-371b-4d86-9b94-574b862fc3f4',
    'Hm_lvt_9152f8221cb6243a53c83b956842be8a': '1677053156,1678602080,1678677875',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218678285ee21aa-0a2bf521f4fd7e-26031951-1049088-18678285ee340c%22%2C%22%24device_id%22%3A%2218678285ee21aa-0a2bf521f4fd7e-26031951-1049088-18678285ee340c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wybeijing%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D',
    'select_city': '110000',
    'lianjia_ssid': '55cd37bd-80b7-442c-a7ad-2d345fed2f7b',
    'Hm_lpvt_9152f8221cb6243a53c83b956842be8a': '1678714285',
    'srcid': 'eyJ0Ijoie1wiZGF0YVwiOlwiNTNhZDgwMDQyMmJiMzViNmY3MzM5MjlmOTkyOWEwYWI5ZDI0MjkyYzRlNGIyMTE1ZWU3ODVkNjI4MDJlNmNjODllNDkxM2ViMTRlZjIwMThkOGE2ZTVhM2UxZWRmZTBjMDIwZTY4MmMyY2RjYzZiZGViOWJjM2IyNWM4Mjk0ZjBmOTkzMTNkMTQ5NDcxZGRhMWI3MTNmYTMyMzZkNjZhNGRlYWMyMzlmNWUyOGIxMDQxY2EyZDhhNDgzNWQxZTQ3ZWE0OWYwZmFiM2E1NzU4NjE5OTBmNzA5NjRkNjkxZDFjMmI2YWVlY2ZhOWY1YzlhY2MxNzc3MWMzYjA0MTJmZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIxMWU3MTU1OVwifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS9lcnNob3VmYW5nLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'SECKEY_ABVK=vzULQcz14GsPelFDE1y2DYOWY0E4jeAsAFWawpXQ1jU%3D; BMAP_SECKEY=3eh45l3qdxgTdUMGSpxI3uD-QPDWWRGfqcVFvG7l31yEC21ONzIYKmCnl8pFxP8xPiDVT5tS7q9oI_2p38rbg0fK_ThS7DjIDDP9yRqT3vct3ea6lRWzyz-b26LweE_Zgh_rUXhR_TgWAuViiSZPZdKxjar_1KRaJa6X4zXb22yZG8mmSiV3PRFwBxiBTL1q; lianjia_uuid=965c5236-371b-4d86-9b94-574b862fc3f4; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1677053156,1678602080,1678677875; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218678285ee21aa-0a2bf521f4fd7e-26031951-1049088-18678285ee340c%22%2C%22%24device_id%22%3A%2218678285ee21aa-0a2bf521f4fd7e-26031951-1049088-18678285ee340c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wybeijing%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; select_city=110000; lianjia_ssid=55cd37bd-80b7-442c-a7ad-2d345fed2f7b; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1678714285; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNTNhZDgwMDQyMmJiMzViNmY3MzM5MjlmOTkyOWEwYWI5ZDI0MjkyYzRlNGIyMTE1ZWU3ODVkNjI4MDJlNmNjODllNDkxM2ViMTRlZjIwMThkOGE2ZTVhM2UxZWRmZTBjMDIwZTY4MmMyY2RjYzZiZGViOWJjM2IyNWM4Mjk0ZjBmOTkzMTNkMTQ5NDcxZGRhMWI3MTNmYTMyMzZkNjZhNGRlYWMyMzlmNWUyOGIxMDQxY2EyZDhhNDgzNWQxZTQ3ZWE0OWYwZmFiM2E1NzU4NjE5OTBmNzA5NjRkNjkxZDFjMmI2YWVlY2ZhOWY1YzlhY2MxNzc3MWMzYjA0MTJmZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIxMWU3MTU1OVwifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS9lcnNob3VmYW5nLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
dated = datetime.now().strftime('%Y-%m-%d')
value_list = []
for city in city_list:
    if city == 'beijing':
        response = requests.get(url = beijing, cookies = cookies, headers = headers, verify = False)
    elif city == 'lf':
        response = requests.get(url = langfang, cookies = cookies, headers = headers, verify = False)
    elif city == 'yanjiao':
        response = requests.get(url = yanjiao, cookies = cookies, headers = headers, verify = False)
    else:
        response = requests.get(url=beijing + city, cookies=cookies, headers=headers, verify=False)

    response_all = response.content.decode()
    ad = re.findall('total fl">(.*?)"', response_all,  re.S)[0].replace('<br />','').replace(' ','')
    ad2 = re.findall('<span>(.*?)<', ad, re.S)
    user1 = SailRoom(city_name=city,sailed_amount=ad2[0] ,date = dated)

    data_tuple = (city, ad2[0], dated)
    value_list.append(data_tuple)
# user2 = Users(username='lisi', password='123456')
    with app.app_context():
        try:
            db.session.add(user1)
            # db.session.add(user2)
            db.session.commit()
            print("数据插入成功！")
        except:
            db.rollback()
            print("数据插入失败！")

try:
    file_name = 'D:\myflask\wqsl.xlsx'
    wb = load_workbook(file_name)
    print('打开excel成功')
except:
    print('打开excel失败')
ws = wb['Sheet2']


try:
    for row in tuple(value_list):
        # print(row)
        ws.append(row)
    wb.save(file_name)
    print('插入保存数据成功')
except:
    print('插入excel数据失败')




# if __name__ == '__main__':
#     app.run(debug = True, host = '0.0.0.0' ,port = '9999' )
#     # app.run()