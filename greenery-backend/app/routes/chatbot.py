from flask import Blueprint, jsonify, request
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath('')))
from src import chatbot


chatbot_routes = Blueprint("chatbot", __name__)

@chatbot_routes.route("/chat", methods=["POST"])
def chat():
    """챗봇 기억력 테스트 함수

    ** 현재 아이디만 안다면 데이터를 수정할 수 있는 상태로, 수정이 필요

    Params:
        msg `str`:
            사용자가 보낸 채팅 내용
        history `list`:
            대화 기록
    
    Returns:
        result `str`:
            응답 성공 여부 (success, error)
        msg `str`:
            응답 메시지
        history `list`:
            대화 히스토리
    """
    # Error: 데이터 형식이 JSON이 아님
    if not request.is_json:
        return jsonify({
            "result": "error", 
            "msg": "missing json in request"
        }), 400
        
    # 파라미터 받아오기
    user_msg = request.json["msg"] if "msg" in request.json else ""
    history = request.json["history"] if "history" in request.json != None else []
    
    bot_msg, history = chatbot.chat(user_msg, history)
    
    return jsonify({
        "result": "success", 
        "msg": bot_msg,
        "history": history
    }), 200
