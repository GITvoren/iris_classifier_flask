from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def basic():
    return jsonify("hello")


if __name__ == '__main__':
     app.run(debug=True)
