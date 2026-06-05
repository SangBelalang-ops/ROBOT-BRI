from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handleMessage(msg):
    print('Pesan diterima: ' + msg)
    send(msg, broadcast=True) # Kirim ke semua teman yang terhubung

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
