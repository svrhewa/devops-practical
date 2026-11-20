import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevOps World! We are LIVE on Render!"

if __name__ == '__main__':
    # Get the port assigned by Render, or use 5000 locally
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)