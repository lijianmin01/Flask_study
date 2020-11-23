from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        print(username,password)
        return render_template("xinix.html",username=username,password=password)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
