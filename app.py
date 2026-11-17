from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Python application deployed using GitHub Actions and Argo CD."

@app.route("/healthz")
def health():
    return {"status": "healthy"}, 200