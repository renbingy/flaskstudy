from flask import Flask, request , render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

class User:
    def __init__(self,username, email):
        self.username = username
        self.email = email
#添加自定义过滤器
def datetime_format(value, format = '%Y-%d-%m %H:%M'):
    return value.strftime(format)
app.add_template_filter(datetime_format, "dformat")

@app.route('/filter')
def data_filter():
    user = User(username='xiaming', email='123456@qq.com')
    mytime = datetime.now()
    return render_template("filter.html", user=user, mytime = mytime)

@app.route('/hello/')
def hello_world():
    return 'Hello World！！！##!'

#请求链接中的参数，直接斜杠拼接
@app.route('/blog/<int:blog_id>')
def blog_data(blog_id):
    return "这是博客id {}".format(blog_id)

#请求连接中的参数？后的形式
@app.route('/book/list')
def book_list():
    page = request.args.get("page",default=1, type= int)
    username = request.args.get("username", default='amy', type= str )
    return f"您获取的是第{page}的图书列表书名{username}！"

#html中获取参数对象
@app.route('/')
def index():
    user = User(username= 'xiaming', email= '123456@qq.com')
    person = {
        "name":"zhangsan",
        "email":"renbingyi@163."
    }
    return render_template("index2.html", user = user, person = person)

#传递请求链接中的参数倒html中，如下blog_ids是html文件中的变量
@app.route('/blogs/<blogg_page>')
def blog_detail(blogg_page):
    return render_template("blog_detail.html", blog_ids = blogg_page)

#jinja2控制语句
@app.route('/control')
def control():
    age = 19
    books = [
        {'name':'水浒传',
         'author':'施耐庵'
         },{
        'name': '水浒传',
        'author': '施耐庵'
    }
    ]
    return render_template("control.html", age = age, books = books)

@app.route('/child1')
def child1():
    return render_template("child1.html")
#加载静态文件
@app.route('/static')
def static_demo():
    return render_template("static.html")


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0' ,port = '9999' )
