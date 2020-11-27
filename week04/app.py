# flask 설치하기(API서버를 만들기 편리한 파이썬의 마이크로 웹 프레임워크)
# 플라스크가 만들어놓은 함수 render_template
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html') #html파일을 모아둔 폴더 templates안의 html파일 읽어줌
# @app.route('/mypage')
# def mypage():
#     return 'This is mypage!'

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give') #title_give값이 찾아지면 변수에 저장
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})
# 클라이언트 쪽 코드(웹페이지 검사 코드)
# $.ajax({
#     type: "GET",
#     url: "/test?title_give=봄날은간다", # 딕셔너리 형태로 데이터 값을 줌
#     data: {},
#     success: function(response){ #return인 딕셔너리를 json형식으로 바꿔서 보내줌 - reponse
#        console.log(response)
#     }
#   })

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give'] # title_give를 찾음
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
# $.ajax({
#     type: "POST",
#     url: "/test",
#     data: { title_give:'봄날은간다' }, # 데이터 title_give를 줌(데이터 가져갈땐 ''없음)
#     success: function(response){
#        console.log(response)
#     }
#   })

# 항상 가장 아래 있어야 함(서버 돌리는 코드)
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
