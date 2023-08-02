from flask import Flask, request , render_template
from flask_sqlalchemy import SQLAlchemy
import config



app = Flask(__name__)

app.config.from_object(config)
db = SQLAlchemy()
#再app.config中设置好的数据库连接信息
#然后使用SQLAlchemy(app)创建一个db对象
#SQLAlchemy会自动读取app.config中连接的数据库信息

db.init_app(app)
# sql = "select * from `pptv_ad`.ad_channel where id= 1 "
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(sql)
#         print(rs.fetchone())
#创建表
class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    username = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable=False)

#添加作者的外键
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author =db.relationship('Users', backref = 'articles')

with app.app_context():
    db.create_all()

@app.route('/query_article')
def query_article():
    user = Users.query.get(2)
    for article in user.articles:
        print(article.title)
    return '文章查询成功'

@app.route('/article/add/<string:title>/<string:content>')
def add_article(title, content):
    article1 = Article(title=title,content=content)
    article1.author = Users.query.get(2)
    # user2 = Users(username='lisi', password='123456')
    db.session.add(article1)
    # db.session.add(user2)
    db.session.commit()
    return "文章标题{},文章内容{}插入成功".format(title,content)

@app.route('/article/query')
def query_articles():
    user = Users.query.get(2)
    for article in user.articles:
        print(article.title)
    return '文章查找成功'

@app.route('/user/add/<string:usn>/<string:pwd>')
def add_user(usn, pwd):
    user1 = Users(username=usn,password=pwd)
    # user2 = Users(username='lisi', password='123456')
    db.session.add(user1)
    # db.session.add(user2)
    db.session.commit()
    return "用户{},密码{}插入成功".format(usn,pwd)

@app.route('/user/get')
def get_user():

    user = Users.query.get(1)
    result = "{0}:{1}--{2}".format(user.id,user.username,user.password)
    return result
@app.route('/user/query')
def query_user():

    users = Users.query.filter_by(password = '123456')
    for user in users:
        print(user.username)
        print(type(user.username))
    return user.username

@app.route('/user/update')
def update():
    user = Users.query.filter_by(username = 'zhangsan').first()
    user.password = '222222'
    db.session.commit()
    return '修改成功'

@app.route('/user/delete')
def delete():
    user = Users.query.filter_by(username = 'zhangsan').first()
    try:
        db.session.delete(user)
        db.session.commit()
    except:
        return '数据不存在'

@app.route('/')
def hello():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0' ,port = '9999' )
    # app.run()