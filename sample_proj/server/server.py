from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config.from_pyfile('config.py')
#db = SQLAlchemy(app)


#from views import *

@app.route('/')
def hello():
	return 'Hello Jaehoon'

if __name__ == '__main__':
	app.run(port=33507)
