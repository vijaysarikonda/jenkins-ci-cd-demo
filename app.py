from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask CI/CD pipeline!"

@app.route('/health')
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

