from flask       import (
    Flask,
    jsonify,
    render_template
    )
from flask_ngrok import run_with_ngrok
import json

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/',methods=['GET'])
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()