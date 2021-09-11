from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 메모하기(POST) API
@app.route('/ToDoList', methods=['POST'])
def save_order():
    memo_receive = request.form['memo_give']


    doc = {
        'name': memo_receive,
    }

    db.memoList.insert_one(doc)
    return jsonify({'msg': '완료되었습니다!'})


# 목록보기(Read) API
@app.route('/ToDoList', methods=['GET'])
def view_orders():
    todo_list = list(db.memoList.find({}, {'_id': False}))
    return jsonify({'todo_list': todo_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)