from server import app
#from models import Member

@app.route('/')
def index():
	return '<h1>You are on the index!</h1>'
