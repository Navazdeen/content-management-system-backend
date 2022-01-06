from dbconnector import create_engine,insert_data
from flask import jsonify,request


def create_db():
    db = create_engine("show databases")
    print((db[0][0]))
    isexist = False
    for i in db:
        if i[0] == 'education_db':
            isexist = True
    if not isexist:
        db = create_engine("create database education_db;")
        return {'message':'Database succesfully created'}


def create_tables():
    tables_list = create_engine("show tables in education_db")
    print(tables_list)
    topic_exist = False
    subtopic_exist = False
    content_exist = False
    userinfo_exist = False
    for i in tables_list:
        print(i)
        if i[0] == 'topic':
            topic_exist = True
        if i[0] == 'sub_topic':
            subtopic_exist = True
        if i[0] == 'content':
            content_exist = True
        if i[0] == "user_info":
            print(userinfo_exist)
            userinfo_exist = True
    if topic_exist and subtopic_exist and content_exist and userinfo_exist:
        pass 
    else:
        if not topic_exist:
                topic_table = create_engine("create table education_db.topic (id int auto_increment primary key,topic_name varchar(50));")
        if not subtopic_exist:
                subtopic_table = create_engine("create table education_db.sub_topic (id int auto_increment primary key,subtopic_name varchar(50),topic_id int,foreign key (topic_id) references topic(id));")
        if not content_exist:
                content_table = create_engine("create table education_db.content(id int auto_increment primary key,content_name varchar(50),content_desc varchar(50),topic_id int,subtopic_id int, foreign key (topic_id) references topic(id),foreign key (subtopic_id) references sub_topic(id));")
        if not userinfo_exist:
                print("user_table_created")
                userinfo_table = create_engine("create table education_db.user_info(id int auto_increment primary key,user_name varchar(50),name  varchar(50),email varchar(50),password varchar(50));")
        return {"message":'tables created succesfully'}



def insert_topic():
    create_db()
    create_tables()
    params = request.get_json()
    topic_data = params["name"]
    print(topic_data)
    col_name = 'topic_name'
    insert = insert_data(f"INSERT INTO education_db.topic ({col_name}) VALUES ('{topic_data}')")
    return jsonify({"msg":"inserted succesfully"}),200

def select_topic():
    get_topics = create_engine(f'select * from education_db.topic;')
    data_form = {}
    for i in get_topics:
        val = f't_{i[0]}'
        data_form[val] = i[1]
    print(data_form)
    return jsonify(data_form),200
    return data_form

def update_topic():
    params = request.get_json()
    name = params["name"]
    topic_id = params["id"]
    updated = insert_data(f"UPDATE education_db.topic SET topic_name = '{name}' WHERE id = {topic_id}")
    print(updated)
    return jsonify({"msg":"updated succesfully"}),200

def delete_topic():
    params = request.get_json()
    topic_id = params["id"]
    deleted = insert_data(f"DELETE FROM education_db.topic WHERE id = '{topic_id}'")
    return jsonify({"msg":"deleted succesfully"}),200





