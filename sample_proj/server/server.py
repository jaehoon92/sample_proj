from flask import Flask
import os
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config.from_pyfile('config.py')
#db = SQLAlchemy(app)


#from views import *

@app.route('/')
def hello():
	return 'Hello Jaehoon'

if __name__ == '__main__':
	# Bind the PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(port=port)
