from dbconnector import create_engine,insert_data
from flask import jsonify,request


def insert_subtopic():
    params = request.get_json()
    subtopic_data = params["name"]
    topic_id = params["topic_id"]
    col_name = 'subtopic_name'
    col_name1 = 'topic_id'
    insert = insert_data(f"INSERT INTO education_db.sub_topic ({col_name},{col_name1}) VALUES ('{subtopic_data}','{topic_id}')")
    return jsonify({"msg":"inserted succesfully"}),200

def select_subtopic():
    params = request.get_json()
    topic_id = params["topic_id"]
    get_subtopics = create_engine(f'select * from education_db.sub_topic where topic_id = {topic_id};')
    data_form = {}
    for i in get_subtopics:
        data_form[f"S_{i[0]}"] = i[1]  
    return jsonify(data_form),200
    

def update_subtopic():
    params = request.get_json()
    name = params["name"]
    subtopic_id = params["id"]
    updated = insert_data(f"UPDATE education_db.sub_topic SET subtopic_name = '{name}' WHERE id = {subtopic_id}")
    return jsonify({"msg":"updated succesfully"}),200

def delete_subtopic():
    params = request.get_json()
    subtopic_id = params["id"]
    deleted = insert_data(f"DELETE FROM education_db.sub_topic WHERE id = '{subtopic_id}'")
    return jsonify({"msg":"deleted succesfully"}),200


