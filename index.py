from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello():
    name = request.form.get('name', 'Guest')

    return f"Hello cloud-engine labs!!"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)


