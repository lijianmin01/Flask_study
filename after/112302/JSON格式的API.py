from flask import Flask, url_for, jsonify
from flask_jwt_extended import get_current_user

app = Flask(__name__)

@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])

if __name__ == '__main__':
    app.run(debug=True)