import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET', 'POST'])
def hello():
	print "does this run"
	return render_template('index.html')

app.run(debug=True)
