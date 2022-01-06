from flask import Flask
from flask_cors import CORS
import sys

from topic import insert_topic,select_topic,update_topic,delete_topic

from subtopic import insert_subtopic,select_subtopic,update_subtopic,delete_subtopic

from content import insert_content,select_content,update_content,delete_content,get_content_desc,update_contentdesc

app = Flask(__name__)
CORS(app)

sys.setrecursionlimit(1500)
@app.route('/insert_topic',methods = ['POST'])  
def insert_topic1():  
    return insert_topic()

@app.route('/select_topic',methods = ['POST'])  
def select_topic1():  
    return select_topic()

@app.route('/update_topic',methods = ['POST'])  
def update_topic1():  
    return update_topic()

@app.route('/delete_topic',methods = ['POST'])  
def delete_topic1():  
    return delete_topic()

@app.route('/insert_subtopic',methods = ['POST'])  
def insert_subtopic1():  
    return insert_subtopic()

@app.route('/select_subtopic',methods = ['POST'])  
def select_subtopic1():  
    return select_subtopic()

@app.route('/update_subtopic',methods = ['POST'])  
def update_subtopic1():  
    return update_subtopic()

@app.route('/delete_subtopic',methods = ['POST'])  
def delete_subtopic1():  
    return delete_subtopic()

@app.route('/insert_content',methods = ['POST']) 
def insert_content1():  
    return insert_content()

@app.route('/select_content',methods = ['POST'])  
def select_content1():  
    return select_content()

@app.route('/update_content',methods = ['POST'])  
def update_content1():  
    return update_content()

@app.route('/delete_content',methods = ['POST'])  
def delete_content1():  
    return delete_content()

@app.route('/get_content_desc',methods = ['POST'])  
def get_content_desc1():  
    return get_content_desc()

@app.route('/update_contentdesc',methods = ['POST'])  
def update_contentdesc1():  
    return update_contentdesc()   


if __name__ == '__main__':  
   app.run(debug = True)