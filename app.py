from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''<h1>Hello from Group 7! B9IS121 - Group CA</h1>
    <p>1. Khawaja Abdul Moiz - 20089410</p>
    <p>2. Arshman Noor - 20096163</p>
    <p>3. Hammad Malik - 20073974</p>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
