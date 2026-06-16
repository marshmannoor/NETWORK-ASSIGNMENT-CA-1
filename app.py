from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello from Group 7! B9IS121 - Group CA</h1> ' \
    '<p> 1. Khawaja Abdul Moiz</p> ' \
    '<p> 2. Arshman Noor</p> ' \
    '<p> 3. Hammad Malik</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
