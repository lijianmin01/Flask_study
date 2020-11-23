"""
Flask 静态文件
Web应用程序通常需要静态文件，例如javascript文件或支持网页显示的CSS文件。
通常，配置Web服务器并为您提供这些服务，但在开发过程中，
这些文件是从您的包或模块旁边的static文件夹中提供，
它将在应用程序的/static中提供。

特殊端点'static'用于生成静态文件的URL。

在下面的示例中，在index.html中的HTML按钮的OnClick事件上
调用hello.js中定义的javascript函数，
该函数在Flask应用程序的“/”URL上呈现。
"""
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)



