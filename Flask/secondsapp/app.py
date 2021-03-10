from flask import Flask
from flask import render_template
from flask import request

app=Flask("MyAPP")

@app.route("/")
def home():
	return "<center>Welcome to My home</center>"

@app.route("/path", methods=["GET"])
def path():
	name = request.args.get("x")
	company = request.args.get("y")
#	name = "Ankit"
	htmlcode = render_template("path.html", myname=name, cname=company)
	return htmlcode

@app.route("/form")
def form():
	return render_template("myform.html")


