from flask import Flask ,render_template
import subprocess

app = Flask("Ankit")

@app.route("/search")
def mysearch():
	data = subprocess.getoutput('date')
	#return("<center><h1>Search</h1></center>")
	return(data)

@app.route("/home")
def email():
	return render_template("a.html")
