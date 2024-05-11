from flask import Blueprint, jsonify, request
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath('')))
from src import chatbot

chatbot_routes = Blueprint("chatbot", __name__)

@chatbot_routes.route("/chat", methods=["POST"])
def chat():
    # Error: 데이터 형식이 JSON이 아님
    if not request.is_json:
        return jsonify({
            "result": "error", 
            "msg": "missing json in request"
        }), 400
    # 파라미터 받아오기
    user_msg = request.json["msg"] if "msg" in request.json else ""
    history = request.json["history"] if "history" in request.json != None else []

    if user_msg == "undefined":
        bot_msg = "물체가 인식되지 않았습니다. 사진을 다시 찍어주세요."
        return jsonify({
            "result": "success", 
            "msg": bot_msg,
            "history": history
        }), 200

    if len(history) == 0:
        bot_msg, history = chatbot.rag(user_msg)
    
    else:
        bot_msg, history = chatbot.chat(user_msg, history)
    
    return jsonify({
        "result": "success", 
        "msg": bot_msg.strip("'"),
        "history": history
    }), 200
