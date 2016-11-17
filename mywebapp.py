from flask import Flask
app = Flask(__name__)

#@app.route("/")
#def hello():
 #   return "Hello World!"
@app.route("/")
def route():
	return app.send_static_file('index.html')
	

@app.route("/name")
def name():
	return "Hello Riona!"

if __name__ == "__main__":
    app.run()