import requests
from lxml import html
import pymysql
from datetime import datetime,timedelta
from  openpyxl import load_workbook
from xml.etree import ElementTree
cookies = {
    'JSESSIONID': '3BE6F3209EF97D25DF8B3BC8FCB765E8',
    '_va_ref': '%5B%22%22%2C%22%22%2C1678777768%2C%22http%3A%2F%2Fzjw.beijing.gov.cn%2F%22%5D',
    '_va_ses': '*',
    '_va_id': '8461b937b56d2e7e.1676974011.8.1678778362.1678777768.',
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=3BE6F3209EF97D25DF8B3BC8FCB765E8; _va_ref=%5B%22%22%2C%22%22%2C1678777768%2C%22http%3A%2F%2Fzjw.beijing.gov.cn%2F%22%5D; _va_ses=*; _va_id=8461b937b56d2e7e.1676974011.8.1678778362.1678777768.',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

params = {
    'pageId': '307749',
}

response = requests.get('http://bjjs.zjw.beijing.gov.cn/eportal/ui', params=params, cookies=cookies, headers=headers, verify=False).content.decode(encoding='utf-8')
selector = html.fromstring(response)
#添加tbody标签，方便和chrome检查结果对照和使用xpath
for table in selector.xpath('//table'):
    tbody = html.Element('tbody')
    tbody.extend(table)
    table.append(tbody)
clzz_xpath = '//*[@id="daf461d430a34e6e877f5246ae33e36f"]/div[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/text()'
qfzz_xpath = '//*[@id="31a9e9d470ef4e1889001d6b3f82d072"]/div[2]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td[2]/text()'
xfzz_xpath = '//*[@id="31a9e9d470ef4e1889001d6b3f82d072"]/div[2]/table[2]/tbody/tr[2]/td[4]/table/tbody/tr[4]/td[2]/text()'

clzzd = selector.xpath(clzz_xpath)[0].replace('\r\n','').replace(' ','')
qfzzd = selector.xpath(qfzz_xpath)[0].replace('\r\n','').replace(' ','')
xfzzd = selector.xpath(xfzz_xpath)[0].replace('\r\n','').replace(' ','')
today = datetime.today()
yesterday = today - timedelta(days=1)
datetd = yesterday.strftime('%Y-%m-%d')
print('存量住宅网上签约数量{}'.format(clzzd))
print('期房住宅网签数量{}'.format(qfzzd))
print('现房住宅网签数量{}'.format(xfzzd))

# 打开数据库连接
db = pymysql.connect(host='123.56.173.220',
                     user='easondbroot',
                     password='JIL4zgd3uUKv@2022',
                     db='ry-vue',
                     port=7581)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL插入语句
sql = "INSERT INTO sailed_room_fgj (clzz, qfzz, xfzz, datet) VALUES (%s, %s, %s, %s)"
data = (clzzd,qfzzd,xfzzd,datetd)
try:
    # 执行SQL语句
    cursor.execute(sql,data)
    # 提交到数据库执行
    db.commit()
    print("数据插入成功！")
except:
    # 发生错误时回滚
    db.rollback()
    print("数据插入失败！")

#关闭数据库连接
db.close()
try:
    file_name = 'D:\myflask\wqsl.xlsx'
    wb = load_workbook(file_name)
except:
    print('打开excel失败')
ws = wb['Sheet1']

values = (
    data,
)
try:
    for row in values:
        ws.append(row)
except:
    print('插入excel数据失败')

# 保存工作簿
wb.save(file_name)