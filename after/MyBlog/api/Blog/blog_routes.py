from flask import Blueprint, request, jsonify
from api import db
from api.Blog.blog_model import Blog
from api.Tag.tag_model import Tag

blogs = Blueprint('blogs',__name__)

"""
让我们在应用程序中添加路由，以便对数据库执行CRUD操作
"""
@blogs.route("/add_blog",methods=['POST'])
def create_blog():
    data = request.get_json()

    new_blog = Blog(title=data["title"],content=data["content"],feature_image=data["feature_image"])

    for tag in data["tags"]:
        present_tag = Tag.query.filter_by(name=tag).first()
        if(present_tag):
            present_tag.blogs_associated.append(new_blog)
        else:
            new_tag = Tag(name=tag)
            new_tag.blogs_associated.append(new_blog)

    db.session.add(new_blog)
    db.session.commit()

    blog_id = getattr(new_blog,"id")
    return jsonify({"id":blog_id})

@blogs.route("/blogs",methods=['GET'])
def get_all_blogs():
    blogs = Blog.query.all()
    serialized_data = []
    for blog in blogs:
        serialized_data.append(blog.serialize)

    return jsonify({"all_blogs":serialized_data})

"""
在上面的代码中，我们查询数据库来检索所有的blog。
由于我们不能在返回函数中直接发送博客对象，
所以我们使用serialize函数将博客对象转换为JSON格式，然后返回所有的博客。

为了通过id检索一个博客，在blog_routing .py中添加以下代码:
"""
@blogs.route("/blog/<int:id>",methods=['GET'])
def get_single_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    serialized_blog = blog.serialize
    serialized_blog["tags"]=[]

    for tag in blog.tags:
        serialized_blog["tags"].append(tag.serialize)

    return jsonify({"single_blog": serialized_blog})

"""
在上述代码中，我们根据URL中提供的id查询数据库。
另外，因为我还想返回带有tags属性的blog对象，
所以我附加了blog中出现的所有标记。
标记到serialized_blog[" tags "]，然后返回serialized_blog。
"""
# 为了更新数据库，我使用了PUT方法。
@blogs.route("/update_blog/<int:id>",methods=['PUT'])
def update_blog(id):
    data = request.get_json()
    blog = Blog.query.filter_by(id=id).first_or_404()

    blog.title = data["title"]
    blog.content = data["content"]
    blog.feature_image = data["feature_image"]

    update_blog = blog.serialize

    db.session.commit()
    return jsonify({"blog_id":blog.id})

"""
在上面的代码中，在update_blog函数中，
我们根据url中提供的id查询数据库并查找记录。
然后，我们将记录中的信息替换为请求体中提供的数据。
"""

@blogs.route("/delete_blog/<int:id>",methods=['DELETE'])
def delete_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()

    return jsonify("Blog was deleted"),200


"""
保护线路

我们将为应用程序创建一个管理用户，只有管理用户才能访问所有路由，
因此，我们需要保护一些路由不被非管理用户访问。

在添加保护路由的功能之前，让我们先创建一个管理员用户。

"""




