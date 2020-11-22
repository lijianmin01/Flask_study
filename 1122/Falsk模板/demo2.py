# 模板变量
# 代码中传入字符串、列表、字典到模板中

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    # 往模板中传入的数据
    my_str = 'Hello Word'
    my_int = 10
    my_array = [3,4,2,1,7,9]
    my_dict = {
        "name":"xiaoming",
        "age":18
    }

    return render_template("hello1.html",
                           my_str=my_str,
                           my_int=my_int,
                           my_array=my_array,
                           my_dict=my_dict)

if __name__ == '__main__':
    app.run(debug=True)

