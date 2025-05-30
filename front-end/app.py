from flask import Flask,render_template,request
from datetime import datetime
import requests

BACKEND_URL = 'http://0.0.0.0:9000'

app = Flask(__name__)

@app.route('/')

def hello():
    day_of_week_str = datetime.today().strftime("%A")

    print(day_of_week_str)
    return render_template('index.html', day_of_week_str=day_of_week_str)


@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit', json=form_data)
    return "Data received"

if __name__== '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)