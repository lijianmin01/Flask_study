from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    my_list = [1,3,4,5,6,7]
    my_str = "www.baidu.com"
    return render_template("index.html",my_list=my_list,my_str=my_str)

app.run(debug=True)