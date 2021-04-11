from flask import Flask, request, render_template

app = Flask("NewApp")

@app.route('/form')
def myform():
	return render_template('basic.html')

@app.route('/data', methods=['POST'])
def mydata():
	if request.method == 'POST':
		data = request.form.get('x')
	else:
		pass

	return data + " is Awesome"

#dynamic route
@app.route('/name/<y>')
def name(y):
	return y.upper()

app.run(port=5555, debug=True)