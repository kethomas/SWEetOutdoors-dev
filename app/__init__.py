from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/states/texas")
def texas():
	return render_template('/stateInstances/Texas.html')

@app.route("/states/california")
def california():
	return render_template('/stateInstances/California.html')

@app.route("/states/florida")
def florida():
	return render_template('/stateInstances/Florida.html')

@app.route("/parks/BigBend")
def bigBend():
	return render_template('/parkInstances/BigBend.html')

@app.route("/parks/DeathValley")
def deathValley():
	return render_template('/parkInstances/DeathValley.html')

@app.route("/parks/Zilker")
def zilker():
	return render_template('/parkInstances/Zilker.html')

if __name__ == "__main__":
	app.run()