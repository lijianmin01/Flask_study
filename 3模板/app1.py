from flask import Markup,Flask,render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    text = Markup("<h1>Hello,Flask!</h1>")
    return render_template("index.html")

@app.route("/")
def index():
    return render_template("index.html")
# 自定义过滤器
@app.template_filter()
def musical(s):
    return s+Markup("&#9835")


if __name__ == '__main__':
    app.run()