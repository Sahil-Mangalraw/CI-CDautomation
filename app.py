from flask import Flask
app=Flask(__name__)
@app.route("/info")
def info():
	return "Sahil is Problem solver"

app.run(host="0.0.0.0")