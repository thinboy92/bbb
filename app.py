import os,re,math
from time import gmtime, strftime

from flask import Flask,render_template,request,session,g,redirect, url_for,abort, flash

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


# Static routing
# Please check the files ending in .html in the templates folder to understand about rendering template.
@app.route('/TheEngineer') # Replace TheEngineer with your nickname
def routeStaticTheEngineer():
	imageURL = 'http://placehold.it/350x150&text=imageOne'
	return render_template('TheEngineer.html', imageURL=imageURL)


HitmanFoo # Static routing, static files and return render_template
@app.route('/HitmanFoo') 
def routeStaticHitmanFoo():
	imageURL = 'http://placehold.it/350x150&text=imageOne'
	return render_template('HitmanFoo.html', imageURL=imageURL)


"""
"""
biscuit # Static routing, static files and return render_template



"""
"""
aronLim # Static routing, static files and return render_template



"""

# Dynamic routing
@app.route('/TheEngineer/<int:visitor>')
def routeDynamicTheEngineer(visitor):
	numOfVisitor = visitor
	return render_template('DynamicTheEngineer.html', numOfVisitor=numOfVisitor)
"""

@app.route('/HitmanFoo/<init:visitor>')
def routeDynamicHitmanFoo(visitor):
	numofVisitor = visitor
	return render_template('DynamicHitmanFoo.html', numOfVisitor=numOfVisitor)


"""
biscuit # Dynamic routing



"""
"""
aronLim # Dynamic routing



"""


# HTTP methods
# N.B: The default method is GET. If no method is defined, Flask will think that it should execute GET.
@app.route('/TheEngineer/HTTPmethods',methods=['GET', 'POST'])
def httpMethodsTheEngineer():
	if request.method == 'POST':
		# if client/browser is requesting a POST method then execute this.
		varTheEngineer = 1 + 2
		return render_template('HTTPmethodsTheEngineer.html', varTheEngineer = varTheEngineer)
	if request.method == 'GET':
		varTheEngineer = 1 + 1
		return render_template('HTTPmethodsTheEngineer.html', varTheEngineer = varTheEngineer)


@app.route('/HitmanFoo/HTTPmethods',methods=['GET', 'POST']
def httpMethodsHitmanFoo():
	if request.method == 'POST':
	# if client/browser is requesting a POST method then execute this. 
		varHitmanFoo = 1 + 2 
		return render_template('HTTPmethodsHitmanFoo.html', varHitmanFoo = varHitmanFoo)
	if request.method == 'GET':
		varHitmanFoo = "You are so smart man" 
		return render_template('HTTPmethodsHitmanFoo.html', varHitmanFoo = varHitmanFoo) 
	



"""
biscuit # Dynamic routing



"""
"""
aronLim # Dynamic routing



"""

# RequestData
@app.route('/TheEngineer/requestData',methods=['GET', 'POST'])
def requestDataTheEngineer():
	if request.method == 'POST':
		name = request.form['name']
		location = request.form['location']
		return render_template('requestDataTheEngineer.html', **locals())
	return render_template('requestDataTheEngineer.html')

@app.route('/HitmanFoo/requestData', methods=['GET', 'POST'])
def requestDataHitmanFoo():
	if request.method == 'POST':
		name = request.form['name']
		location = request.form['location']
		return render_template('requestDataHitmanFoo.html, **locals()) 
	return render_template('requestDataHitmanFoo.html')



"""
biscuit # Request Data



"""
"""
aronLim # Request Data



"""

# Session & url_for & flash
# App secret should be stored in the configuration section
app.secret_key = 'ultimate/123Aron/345Killed/456Hitman/987Foo/432By/543Eating/435Biscuit'

@app.route('/TheEngineer/storeSession')
def storeSessionTheEngineer():
	session['timeEntered'] = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	flash('Data stored in session & you have been redirected to index page')
	return redirect(url_for('index'))

@app.route('/TheEngineer/checkSession')
def checkSessionTheEngineer():
	checkSession = session['timeEntered']
	return render_template('checkSessionTheEngineer.html', checkSession=checkSession)

@app.route('/TheEngineer/popSession')
def popSessionTheEngineer():
	session.pop('timeEntered', None)
	flash('Data removed from session & you have been redirected to index page')
	return redirect(url_for('index'))

@app.route('/TheHitmanFoo/storeSession')
def storeSessionHitmanFoo():
	session['timeEntered'] = strftime("%a, %d %b %Y %H:%M:%S +000", gmtime())
	flash('Data stored in session & you have been redirected to index page')
	return redirect(url_for('index'))

@app.route('/HitmanFoo/checkSession')
def checkSessionHitmanFoo():
	checksession = session['timeEntered']
	return render_template('checkSessionHitmanFoo.html', checkSession=checkSession)
	
@app.route('/HitmanFoo/popSession')
def popSessionHitmanFoo():
	session.pop('timeEntered', None) 
	flash('Data removed from session & you have been redirected to index page')
	return redirect(url_for('index))
	
"""
biscuit # Session



"""
"""
aronLim # Session



"""



if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='127.0.0.1', port=port)





