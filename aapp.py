from flask import Flask
app = Flask(__name__)
@app.route('/home')
def home():
	return "hi i am aadive!"
if __name__=='__main__':
	app.run()
