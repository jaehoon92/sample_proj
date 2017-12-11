from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'abcdefg'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('../ChatAppPage.html')

@socketio.on('my event')
def handle_my_custom_event(json):
	print('received something: ' + str(json))
	socketio.emit('my response', json)
if __name__ == '__main__':

	# Bind the PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	socketio.run(app, host='0.0.0.0', port=port)
