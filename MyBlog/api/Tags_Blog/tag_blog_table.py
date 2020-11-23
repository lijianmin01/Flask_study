from api import db

tag_blog = db.Table('tag_blog',
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True),
    db.Column('blog_id', db.Integer,db.ForeignKey('blog.id'),primary_key=True))

"""
从上面的代码可以看到，我们已经创建了一个表来分别存储tag_id和blog_id。
注意，我将列定义为主键，这样，每个博客只能提到标签一次。

现在我们已经定义了两个表，我们可以在Blog模型中添加标签属性:
"""