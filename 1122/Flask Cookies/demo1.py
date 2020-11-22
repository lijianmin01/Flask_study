"""
Flask Cookies
Cookie以文本文件的形式存储在客户端的计算机上。
其目的是记住和跟踪与客户使用相关的数据，以获得更好的访问者体验和网站统计信息。

Request对象包含Cookie的属性。它是所有cookie变量及其对应值的字典对象，
客户端已传输。除此之外，cookie还存储其网站的到期时间，路径和域名。

在Flask中，对cookie的处理步骤为：
"""
# Flask Cookies的简单示例

from flask import Flask,make_response,request

app = Flask(__name__)

@app.route("/set_cookies")
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("w3cshool","w3csholl",max_age=3600)
    return resp

@app.route("/get_cookies")
def get_cookie():
    resp = make_response("del success")
    resp.delete_cookie("w3cshool")

    return resp

if __name__ == '__main__':
    app.run(debug=True)

