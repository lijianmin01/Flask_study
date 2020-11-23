from flask import Flask, app, jsonify
from flask_jwt_extended import JWTManager, jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from api.Blog.blog_model import Blog
from api.User.user_model import User
import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

"""
接下来，我们需要在我们的应用程序中注册这个蓝图，
所以在剩余的init剩余.py文件的create_app函数中，添加以下代码:
"""
from api.Blog.blog_routes import blogs

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URL']="sqlite:///flaskdatabase.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    CORS(app)

    db.init_app(app)
    app.register_blueprint(blogs)

    app.config['JWT_SECRET_KEY'] = 'YOUR_SECRET_KEY'
    jwt = JWTManager(app)
    return app

"""
上面的代码非常简单，我们创建了一个名为create_app()的函数，
它是我们的应用程序工厂，它初始化我们的应用程序和数据库。
"""

"""
因为我们将为应用程序创建一个管理用户，所以不需要为用户模型创建路由。
我们将在服务器启动之前创建一个自定义管理用户。
为此，我们将创建一个自定义命令，它将在运行flask run命令之前执行，
这个自定义命令将为我们创建一个管理用户。
"""

@click.command(name="create_admin")
@with_appcontext
def create_admin():
    admin = User(email="admin_email_address", password="admin_password")
    admin.password = generate_password_hash(admin.password, 'sha256', salt_length=12)
    db.session.add(admin)
    db.session.commit()

app.cli.add_command(create_admin)


@blogs.route('/delete_blog/<int:id>', methods=["DELETE"])
@jwt_required
def delete_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()

    return jsonify("Blog was deleted"), 200