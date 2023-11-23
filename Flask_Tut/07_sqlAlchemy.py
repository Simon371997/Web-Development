from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import timedelta
import sqlalchemy

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=2) # session data will be stored for 2 minutes


@app.route('/')
def home():
    return render_template('03_1_base.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        flash('Login was succesful!', category='info')
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            flash('Already logged in!')
            return redirect(url_for('user'))
        else:
            return render_template('04_login.html')

 
@app.route('/logout')
def logout():
    flash('You have been logged out!', category='info')
    session.pop('user', None)
    session.pop('emial', None)
    return redirect(url_for('login'))



@app.route('/user', methods = ['POST', 'GET'])
def user():
    email = None
    if 'user' in session:
        user = session['user']

        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email
        else:
            if 'email' in session:
                email = session['email']

        return render_template('06_user.html', email=email)
    else:
        flash('You are not logged in!', category='warning')
        return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)