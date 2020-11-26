from flask import Flask,render_template,request,flash,get_flashed_messages

app = Flask(__name__)

app.secret_key="s51515ecretkey"
# app.session_cookie_name="121"
CSRF_ENABLED = True

@app.route("/",methods=['POST','GET'])
def index():
    message = None
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        # 3、判断参数是否填写 &  密码是否相同
        if not all([username,password,password2]):
            flash(u"参数不完整")
        elif password2!=password:
            flash(u"两次密码不一致")
        else:
            return "success"

    return render_template('index.html',get_flashed_messages=get_flashed_messages())

if __name__ == '__main__':
    app.run(debug=True)
