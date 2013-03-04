import os,time,re,math

from flask import Flask,render_template,request,session,g,redirect, url_for,abort, flash

app = Flask(__name__)

# Static routing
# Please check the files ending in .html in the templates folder to understand about rendering template.
@app.route('/TheEngineer') # Replace TheEngineer with your nickname
def routeStaticTheEngineer():
    return render_template('TheEngineer.html')


"""
HitmanFoo # Static routing and return render_template



"""
"""
biscuit # Static routing and return render_template



"""
"""
aronLim # Static routing and return render_template



"""

# Dynamic routing
@app.route('/TheEngineer/<int:visitor>')
def routeDynamicTheEngineer(visitor):
	numOfVisitor = visitor
	return render_template('DynamicTheEngineer.html', numOfVisitor=numOfVisitor)
"""
HitmanFoo # Dynamic routing



"""
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
"""
HitmanFoo # Dynamic routing



"""
"""
biscuit # Dynamic routing



"""
"""
aronLim # Dynamic routing



"""



if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)





















