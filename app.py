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


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    phone_receive = request.form['phone_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    address2_receive = request.form['address2_give']
    post_receive = request.form['post_give']

    doc = {
        'name': name_receive,
        'phone': phone_receive,
        'amount': amount_receive,
        'address': address_receive,
        'address2': address2_receive,
        'post': post_receive,
    }

    db.onlineMall.insert_one(doc)
    return jsonify({'msg': '완료되었습니다!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    order_list = list(db.onlineMall.find({}, {'_id': False}))
    return jsonify({'order_list': order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)