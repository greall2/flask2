import flask as fl

app = fl.Flask(__name__)

#@app.route("/")
#def hello():
 #   return "Hello World!"
@app.route("/")
def route():
	return app.send_static_file('index.html')
	

@app.route('/name')
def fname():
	return 'Your name is'  + fl.request.values["name"]


#@app.route("/name/<name>")
#def name(name):
#	return "Your name is " + name


	

if __name__ == "__main__":
    app.run()