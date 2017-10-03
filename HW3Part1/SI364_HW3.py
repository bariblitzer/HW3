## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).
from flask import Flask, render_template, request
import requests
import json

from flask import Flask, request
app = Flask(__name__)
app.debug = True 


@app.route('/artistform')
def artist_form():
	return render_template('artistform.html')

@app.route('/artistinfo', methods = ['GET', 'POST'])
def artist_info():
	if request.method == 'GET':
		result = request.args
		term = result.get('artist')
		resp = requests.get('https://itunes.apple.com/search?term='+term+'&limit=')
		data = json.loads(resp.text)
	return render_template('artist_info.html', objects=data['results'])

@app.route('/artistlinks')
def artist_link():
	return render_template('artist_links.html')

@app.route('/specific/song/<artist_name>', methods = ['GET', 'POST'])
def artists(artist_name):
	d ={'media': 'music', 'format':'json', 'term':artist_name}
	url = requests.get('https://itunes.apple.com/search?', params=d)
	data = json.loads(url.text)
	return render_template('specific_artist.html', results=data['results'])


if __name__ == '__main__':
    app.run(debug=True)


