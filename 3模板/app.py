from flask import Flask,render_template

user = {
    'username':'Grey Li',
    'bio':'A boy who loves movies and music',
}

movies = [
    {'name':'A','year':'1988'},
    {'name':'b','year':'1989'},
    {'name':'c','year':'1288'},
    {'name':'d','year':'1888'},
    {'name':'e','year':'2988'},
]

app = Flask(__name__)

@app.route("/")
def watchlist():
    return render_template("watchlist.html",user=user,movies=movies)

if __name__ == '__main__':
    app.run(debug=True)