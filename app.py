from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>我的第一个网页后台</h1><p>来自 RackNerd 服务器</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
