from flask import Flask,render_template
from flask_socketio import SocketIO, send

app= Flask(__name__)
app.config['SECRET_KEY']= 'saleem'
socketio =SocketIO(app)



@app.route('/')
def form():
    return render_template('chat.html')

@socketio.on('message')
def handle_mess(mess):
    send(mess, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5000) 