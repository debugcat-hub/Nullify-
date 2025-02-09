from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Spotify OAuth Server Running!"

@app.route("/callback")
def callback():
    code = request.args.get("code")
    return f"Authorization Code: {code}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
