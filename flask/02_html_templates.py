from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('02_index.html', content = ['Tim', 'Joe', 'James'])




if __name__ == '__main__':
    app.run()
