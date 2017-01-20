import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!!!! (koen)"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='10.129.32.150', port=port)