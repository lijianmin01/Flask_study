import os
import sys

from flask import Flask, flash, render_template, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired


# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_UR'] = os. getenv ('DATABASE URL','sqlite ／／／'+os.path.join(app.root_path, 'data.db' ))
# 关闭警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


# 创建表单视图
class NewNoteForm(FlaskForm):
    body = TextAreaField('Body',validators=[DataRequired()])
    submit = SubmitField('Save')


class EditNoteForm(FlaskForm):
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Update')


class DeleteNoteForm(FlaskForm):
    submit = SubmitField('Delete')

# 定义一个Note 来存储笔记
class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.Text)

    # 返回一些更有用的信息
    def __repr__(self):
        return "<Note %r>"% self.body

@app.route("/")
def index():
    # 在试图函数中查询数据库记录并传入模板
    form = DeleteNoteForm()
    notes = Note.query.all()
    return render_template("index.html",form=form,notes=notes)

# 增加一个新的内容
@app.route("/new",methods=['GET','POST'])
def new_note():
    form = NewNoteForm()
    # if  request.method==' post '  and  from.validate():
    if form.validate_on_submit():
        body = form.body.data
        note = Note(body=body)
        db.session.add(note)
        db.session.commit()
        flash("Your note is saved")
        return redirect(url_for('index'))
    return render_template("new_note.html",form=form)

# # 删除笔记
# @app.route('/delete/<int : note_id>')
# def delete_note(note_id):
#     note = Note.query.get(note_id)
#     db.session.delete(note)
#     db.session.commit()
#     flash("Your note is deleted.")
#     return redirect(render_template(url_for("index")))
"""
这种代码看起来逻辑很合理，但是回事程序数量CSRF攻击的风险中
防范CSRT 攻击的基本原理就是正确使用GET 和 POST 方法，想删除这类修改数据的
操作绝对不能通过GET 请求实现
正确的做法是为删除操作创建一个表单
"""
# 修改笔记
@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    form = EditNoteForm()
    note = Note.query.get(note_id)
    if form.validate_on_submit():
        note.body = form.body.data
        db.session.commit()
        flash('Your note is updated.')
        return redirect(url_for('index'))
    form.body.data = note.body  # preset form input's value
    return render_template('edit_note.html', form=form)

# 删除笔记
@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    form = DeleteNoteForm()
    if form.validate_on_submit():
        note = Note.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
        flash('Your note is deleted.')
    else:
        abort(400)
    return redirect(url_for('index'))

# 注册shell上下文处理函数
@app.shell_context_processor
def make_shell_context():
    return dict(db=db,Note=Note)

"""
一对多
   作者和文章来演示一对多的关系
   Author (Article1   Article2    Article3)  
"""
class Author(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(70),unique=True)
    phone = db.Column(db.String(20))

class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),index=True)
    body = db.Column(db.Text)
    time = db.Column(db.String(10))
    # 定义外键
    author_id = db.Column(db.Integer,db.ForeignKey("author.id"))

# 基于一对多关系的双向关系
class Writer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(70),unique=True)
    books = db.relationship('Book',back_populates='writer')

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),index=True)
    writer_id = db.Column(db.Integer,db.ForeignKey('writer.id'))
    writer = db.relationship('Writer',back_populates='books')

"""
多对一
    多个居民居住在同一座城市
    Citizen 类表示居民，City表示城市
"""
class Citizen(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(70),unique=True)
    city_id = db.Column(db.Integer,db.ForeignKey('city.id'))
    city = db.relationship('City')

class City(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30),unique=True)

"""
一对一
    Country    Capital(首都)
    建立双向关系的一对一实现的一对一的关系
"""
class Country(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30),unique=True)
    '''
    通过将uselist 设置为False,将返回对应的单个记录，而且无法再使用列表语义操作
    '''
    capital = db.relationship("Capital",uselist=False)

class Capital(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30),unique=True)
    country_id = db.Column(db.Integer,db.ForeignKey('country.id'))
    country = db.relationship('Country')

"""
多对多
    我们将使用学生和老师来演示多对多关系
    在SQLAlchemy 中，我们还需要创建一个关联表（association table）.
    关联表不存储数据，只用来存储关系两侧的外键的模型
"""
association_table = db.Table('association',
                             db.Column('student_id',db.Integer,db.ForeignKey('student.id')),
                             db.Column('teacher_id',db.Integer,db.ForeignKey('teacher.id')))

class Student(db.Model):
    id = db.Column(db.String,primary_key=True)
    name = db.Column(db.String(70),unique=True)
    grade = db.Column(db.String(20))
    teachers = db.relationship('Teacher',
                               secondary = association_table,
                               back_populates='students')

class Teacher(db.Model):
    id = db.Model(db.Integer,primary_key = True)
    name = db.Column(db.String(70),unique=True)
    office = db.Column(db.String(20))



if __name__ == '__main__':
    app.run(debug=True)






