from flask import Blueprint, request, jsonify
from transformers import pipeline
from app.models.chat import Chat
from app import db

chatbot_bp = Blueprint('chatbot', __name__)

#load a model from Hugging Face
chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_id = data.get('user_id')
    user_message = data.get('message')

    if not user_id or not user_message:
        return jsonify({"error": "User ID and message are required"}), 400

    #generate a response using the open-source model
    response = chatbot(user_message, max_length=50, do_sample=True, temperature=0.7)
    bot_message = response[0]['generated_text']

    #save chat history
    chat = Chat(user_id, user_message, bot_message)
    chat.save(db)

    return jsonify({"message": bot_message})

#get a chat history
@chatbot_bp.route('/chat/history', methods=['GET'])
def chat_history():
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    chat_history = Chat.find_by_user_id(db, user_id)
    return jsonify({"chat_history": chat_history})