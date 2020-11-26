from flask import Flask,render_template,flash,url_for

app = Flask(__name__)
app.secret_key = "Secret string"

@app.route("/flash")
def just_flash():
    flash("I am flash, who is looking for me .")
    return render_template(url_for("index"))

if __name__ == '__main__':
    app.run()