from flask_socketio import emit
from app import socketio, db
from app.models.chat import Chat

#webSocket is used for sending and receiving messages
@socketio.on('send_message')
def handle_send_message(data):
    user_id = data.get('user_id')
    message = data.get('message')

    if not user_id or not message:
        emit('error', {'message': 'User ID and message are required'})
        return

    #save the message to the database
    chat = Chat(user_id, message, "")
    chat.save(db)

    #emitting the message to all connected clients
    emit('receive_message', {
        'user_id': user_id,
        'message': message,
        'timestamp': chat.timestamp.isoformat()
    }, broadcast=True)