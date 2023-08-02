import pymysql


HOST = '123.56.173.220'

PORT = 7581

USER = 'easondbroot'

PASSWORD = 'JIL4zgd3uUKv@2022'

DATABASE = 'ry-vue'

mydb = pymysql.connect(host=HOST,
                     user=USER,
                     password=PASSWORD,
                     #database='mysql',
                     port=PORT,
                     database='ry-vue',
                     charset='utf8mb4'
                    )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = mydb.cursor()
#SQL查询语句
sql = "select * from `ry-vue`.eas_area where id= 1 "
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
print(results)
for row in results:
    fname = row[0]

    print ("fname={}".format(fname))

# 关闭数据库连接
mydb.close()