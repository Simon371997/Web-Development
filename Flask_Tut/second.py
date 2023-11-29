# good overview for Flask Structure: http://exploreflask.com/en/latest/blueprints.html

from flask import Blueprint, render_template


#name of the blueprtint should be the name of the file (here: '10_second')
second = Blueprint('second', __name__, static_folder='staic', template_folder='templates') 

@second.route('/home')
@second.route('/')
def home():
    return render_template('09_home.html')

@second.route('/test')
def test():
    return '<h1>test</h1>'