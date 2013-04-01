import os,re,math 
from time import gmtime, strftime 

from flask import Flask, render_template, request, session,g,redirect, url_for, abort, flash 

app = Flask(__name__)

@app.route('/') 
def home(): 
	return render_template('home.html')a
	
@app.route('/BecomeaBaboon', methods =['GET','POST'])
def becomingababoon():
	if request.method = 'POST':
		x = request.form['I_want_to_be_A']
		cool = 'http://www.flickr.com/photos/wagner-machado-carlos-lemes/2095405319/lightbox/'
	return render_template('requestDatababoon.html', **locals()) 

if __name__ = '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 2001)
	app.run(host='127.0.0.1', port=port) 
		
	