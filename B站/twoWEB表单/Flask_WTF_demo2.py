from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
    message = None
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        # 3、判断参数是否填写 &  密码是否相同
        if not all([username,password,password2]):
            print("参数不完成")
            message = "参数不完整"
        elif password2!=password:
            message = "两次密码不一致"
        else:
            message = "success"

    return render_template('index.html',message=message)

if __name__ == '__main__':
    app.run(debug=True)
