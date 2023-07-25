from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def accept():
    if request.method == 'POST':
        result = request.data
        print(str(result, 'utf-8'))
        with open('result.txt', 'w') as f:
            f.write(str(result, 'utf-8'))
        return result
    else:
        return 'NO POST'

if __name__ == '__main__':
    app.run(port=25560, debug=True)