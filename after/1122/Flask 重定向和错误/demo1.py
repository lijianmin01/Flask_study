"""
Flask 重定向和错误
Flask类有一个redirect()函数。调用时，它返回一个响应对象，并将用户重定向到具有指定状态代码的另一个目标位置。

Flask.redirect(location, statuscode, response)
在上述函数中：

location参数是应该重定向响应的URL。

statuscode发送到浏览器标头，默认为302。

response参数用于实例化响应。

以下状态代码已标准化：

HTTP_300_MULTIPLE_CHOICES
HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND
HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY
HTTP_306_RESERVED
HTTP_307_TEMPORARY_REDIRECT
"""
from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("log_in.html")

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST' and request.form['username']=='admin':
        return redirect(url_for('success'))
    return redirect(url_for('index'))

@app.route("/success")
def success():
    return "logged in successfully"


if __name__ == '__main__':
    app.run(debug=True)


























