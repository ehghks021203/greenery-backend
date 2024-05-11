from flask import Blueprint, jsonify, request
from app import mysql

get_trash_data_routes = Blueprint("get_trash_data", __name__)

@get_trash_data_routes.route("/get_trash_data", methods=["POST"])
def get_trash_data():
    # request 값이 올바르지 않은 경우
    if not request.is_json:
        return jsonify({"result":"error", "msg":"missing json in request"}), 400

    # POST로 인자 값 받아오기
    lat = request.json.get("lat")
    lng = request.json.get("lng")
    radius = request.json.get("radius")

    cur = mysql.connection.cursor()

    sql = f"""
    SELECT * 
    FROM trash_place 
    WHERE ST_DISTANCE_SPHERE(POINT(lng, lat), POINT({lng}, {lat})) <= {radius}
    """
    cur.execute(sql)
    sql_res = cur.fetchall()
    cur.close()
    return jsonify({
        "result": "success", 
        "msg": "get trash data",
        "trash_data": sql_res,
        "count": len(sql_res)
    }), 200

@get_trash_data_routes.route("/get_nearest_trash_data", methods=["POST"])
def get_nearest_trash_data():
    # request 값이 올바르지 않은 경우
    if not request.is_json:
        return jsonify({"result":"error", "msg":"missing json in request"}), 400

    # POST로 인자 값 받아오기
    lat = request.json.get("lat")
    lng = request.json.get("lng")

    cur = mysql.connection.cursor()

    sql = f"""
    SELECT *, ST_DISTANCE_SPHERE(POINT(lng, lat), POINT({lng}, {lat})) as dist
    FROM trash_place 
    WHERE type LIKE "재활용쓰레기"
    ORDER BY dist
    LIMIT 1;
    """
    cur.execute(sql)
    sql_res = cur.fetchone()

    sql2 = f"""
    SELECT *, ST_DISTANCE_SPHERE(POINT(lng, lat), POINT({lng}, {lat})) as dist
    FROM trash_place 
    WHERE type LIKE "일반쓰레기"
    ORDER BY dist
    LIMIT 1;
    """
    cur.execute(sql2)
    sql_res2 = cur.fetchone()

    res = [sql_res, sql_res2]

    cur.close()
    return jsonify({
        "result": "success", 
        "msg": "get nearest trash data",
        "trash_data": res
    }), 200

@get_trash_data_routes.route("/get_specific_trash_data", methods=["POST"])
def get_specific_trash_data():
    # request 값이 올바르지 않은 경우
    if not request.is_json:
        return jsonify({"result":"error", "msg":"missing json in request"}), 400

    # POST로 인자 값 받아오기
    lat = request.json.get("lat")
    lng = request.json.get("lng")

    cur = mysql.connection.cursor()

    sql = f"""
    SELECT *, ST_DISTANCE_SPHERE(POINT(lng, lat), POINT({lng}, {lat})) as dist
    FROM trash_place 
    ORDER BY dist
    LIMIT 1;
    """
    cur.execute(sql)
    sql_res = cur.fetchone()
    cur.close()
    return jsonify({
        "result": "success", 
        "msg": "get specific trash data",
        "addr": sql_res["addr"],
        "lat": sql_res["lat"],
        "lng": sql_res["lng"],
        "place": sql_res["place"],
        "class": sql_res["class"],
        "type": sql_res["type"],
        "call_number": sql_res["call_number"]
    }), 200

