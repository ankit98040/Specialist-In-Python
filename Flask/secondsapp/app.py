from flask import Flask
from flask import render_template

app=Flask("MyAPP")

@app.route("/")
def home():
	return "<center>Welcome to My home</center>"

@app.route("/path")
def path():
	name = "Ankit"
	htmlcode = render_template("path.html")
	return htmlcode