from dbconnector import create_engine,insert_data
from flask import jsonify,request

def insert_content():
    params = request.get_json()
    content_name = params["name"]
    content_desc = params["desc"]
    topic_id = params["topic_id"]
    subtopic_id = params["subtopic_id"]
    col_name = 'content_name'
    col_name1 = 'content_desc'
    col_name2 = 'topic_id'
    col_name3 = 'subtopic_id'
    insert = insert_data(f"INSERT INTO education_db.content ({col_name},{col_name1},{col_name2},{col_name3}) VALUES ('{content_name}','{content_desc}','{topic_id}','{subtopic_id}')")
    return jsonify({"message":"inserted succesfully"}),200

def select_content():
    params = request.get_json()
    subtopic_id = params["subtopic_id"]
    topic_id = params["topic_id"]
    get_content = create_engine(f'select * from education_db.content where subtopic_id = {subtopic_id} and topic_id = {topic_id};')
    data_form = {}
    for i in get_content:
        data_form[f"c_{i[0]}"] = i[1]
    print(data_form)
    return jsonify(data_form),200

def update_content():
    params = request.get_json()
    name = params["name"]
    content_id = params["id"]
    updated = insert_data(f"UPDATE education_db.content SET content_name = '{name}'  WHERE id = {content_id}")
    return jsonify({"message":"updated succesfully"}),200

def delete_content():
    params = request.get_json()
    content_id = params["id"]
    deleted = insert_data(f"DELETE FROM education_db.content WHERE id = '{content_id}'")
    return jsonify({"message":"deleted succesfully"}),200


def get_content_desc():
    params = request.get_json()
    subtopic_id = params["subtopic_id"]
    topic_id = params["topic_id"]
    content_id = params["content_id"]
    get_content = create_engine(f'select * from education_db.content where subtopic_id = {subtopic_id} and topic_id = {topic_id} and id = {content_id};')
    data_form = {}
    print(get_content)
    for i in get_content:
        data_form["desc"] = i[2]  
    print(data_form)
    return jsonify(data_form),200



def update_contentdesc():
    params = request.get_json()
    name = params["desc"]
    content_id = params["id"]
    updated = insert_data(f"UPDATE education_db.content SET content_desc = '{name}'  WHERE id = {content_id}")
    return jsonify({"message":"updated succesfully"}),200

