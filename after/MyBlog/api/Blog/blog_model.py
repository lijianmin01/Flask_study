"""
创建表

我们将创建一个博客表，在其中存储博客的所有属性。
我为这个特别的博客考虑的属性/专栏如下:

id(这将是我们的博客id)
标题(博客标题)
内容(博客内容)
created_at(博客创建日期)
feature_image(我们博客的封面图片)
标签(与博客相关的标签)
    id ( This will be our blog-id)
    title (Title of the blog)
    content (Content of the blog)
    created_at (Date at which the blog was created)
    feature_image (Cover image for our blog)
    tags (Tags related to the blog)

一个人可以添加更多的属性/列到博客根据他们的便利性。

让我们开始为表构建模型。
"""

from api import db
from datetime import datetime
from api.Tags_Blog.tag_blog_table import tag_blog
# from api.Tags_Blog.tag_blog_table import tag_blog

class Blog(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text,nullable=False)
    feature_image = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            "id":self.id,
            "title":self.title,
            "content":self.content,
            "feature_image":self.feature_image,
            "create_at":self.created_at,
        }

    tags = db.relationship('Tag',secondary=tag_blog,backref=db.backref('blogs_associated',lazy="dynamic"))
















