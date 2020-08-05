from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)  #플라스크 만듦
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():      # 비어있으니 methods가 get이다.
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/review', methods=['POST'])            #보안을 지켜야할 때 포스트를 씀
def write_review():
    # 1. 클라이언트가 준 title, author, review 가져오기./ 받아서
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    # 2. DB에 정보 삽입하기 / 넣고
    document = {
        'title' : title_receive,
        'author' : author_receive,
        'review' : review_receive,
    }
    db.review.insert_one(document)    #db에 넣어주는 코드

    # 3. 성공 여부 & 성공 메시지 반환하기/ 가지고온다.
    return jsonify({'result': 'success'})


@app.route('/review', methods=['GET'])
def read_reviews():
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)