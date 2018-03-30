from flask import Flask
import demo
import json
app = Flask(__name__)

@app.route('/data/')
def my_link():
    # res = demo.main()
    return 'click'

if __name__ == '__main__':
    app.run(debug=True)
