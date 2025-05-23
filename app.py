from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <form method="POST" action="/login">
            Kullanıcı Adı: <input name="username"><br>
            Şifre: <input name="password"><br>
            <input type="submit" value="Giriş Yap">
        </form>
    '''

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    return f"Giriş Yapıldı! Kullanıcı: {username}, Şifre: {password}"

if __name__ == "__main__":
    app.run(port=5000)
