from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('03_2_index.html')





if __name__ == '__main__':
    app.run(debug = True) # App muss nicht bei jeder Änderung neu gestartet werden
