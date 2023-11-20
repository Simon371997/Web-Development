from flask import Flask, redirect, url_for


# definieren der App
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello! This is the main page <h1>HELLO</h1> '

@app.route('/<name>')
def user(name):
    return f'Hello {name}!'


# mit redirect können routen auf andere routen umgeleitet werden
# mit url_for muss nicht die url übergeben werden, sondern nur der name der Funktion!
@app.route('/admin')
def admin():
    return redirect(url_for('home'))





if __name__ == '__main__':
    app.run()
