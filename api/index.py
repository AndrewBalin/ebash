
from flask import Flask
#a
app = Flask(__name__)


@app.route('/')
def mission():
    return "EBASH"


if __name__ == '__main__':
    main()
    app.run(port=5000, host='0.0.0.0')

