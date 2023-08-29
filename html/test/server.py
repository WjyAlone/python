
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Propist'

if __name__ == '__main__':
    app.run(debug= True, port=80)