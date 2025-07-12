from flask import Flask
app = Flask(__name__)
@app.route('/home')
def home():
	return "hello from Flask in juypter Notepad!"
if __name__=='__main__':
	app.run()
