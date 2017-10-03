from flask import Flask, render_template, request
import requests
import json

from flask import Flask, request
app = Flask(__name__)
app.debug = True 

@app.route('/colorform')
def artist_form():
	return render_template('color_form.html')

@app.route('/colorinfo', methods = ['GET', 'POST'])
def count_color():
	if request.method == 'GET':
		result = request.args
		number = str(result['color'])
		col = len(number)
		return 'There are' + " " + str(col) + " " + 'letters in your favorite color!'

@app.route('/second')
def second_form():
	return render_template('second_blank.html')

@app.route('/ageinfo', methods = ['GET', 'POST'])
def age_count():
	if request.method == 'GET':
		result = request.args
		age_num = 17 + int(result['age'])
		return 'You are' + " " + str(age_num) + " " + 'years old!'