from urllib import parse
#Mysql所在的主机名ip
HOST = '123.56.173.220'
#Mysql觐见厅的端口号，默认3306
PORT = 7581
#连接Mysql的用户名
USER = 'easondbroot'
#连接数据库的密码
PASSWORD = parse.quote('JIL4zgd3uUKv@2022')
# PWD = parse.quote_plus(PASSWORD)
#MySQL上创建数据库名称
DATABASE = 'ry-vue'

# HOST = '10.200.146.41'
# #Mysql觐见厅的端口号，默认3306
# PORT = 3306
# #连接Mysql的用户名
# USER = 'root'
# #连接数据库的密码
# PASSWORD = '0y7jnQzdtqBkfHjr'
# #MySQL上创建数据库名称
# DATABASE = 'pplive_ad'



SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4"
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=uf8mb4".format(USER,PASSWORD,HOST,PORT,DATABASE)

print(SQLALCHEMY_DATABASE_URI)