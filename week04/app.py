# flask 설치하기
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<button>버튼</button>'


@app.route('/mypage')
def mypage():
    return 'This is mypage!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
