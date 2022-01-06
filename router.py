from flask import Flask, request, jsonify
from flask_cors import CORS
import sys


from table import Topic_Table, Subtopic_Table, Content_Table, Quizz_Table

topic = Topic_Table()
subtopic=Subtopic_Table()
content = Content_Table()
quizz = Quizz_Table()

app = Flask(__name__)
CORS(app)

sys.setrecursionlimit(1500)
@app.route('/insert_topic',methods = ['POST'])  
def insert_topic():  
    param = request.get_json()
    print(param)
    result = topic.add_topic(**param)
    return result

@app.route('/select_topic',methods = ['POST'])  
def select_topic():  
    result = topic.get_topic()
    return result

@app.route('/update_topic',methods = ['POST'])  
def update_topic():  
    param = request.get_json()
    result = topic.update_topic(**param)
    return result


@app.route('/delete_topic',methods = ['POST'])  
def delete_topic():  
    param = request.get_json()
    result = topic.delete_topic(**param)
    return result

@app.route('/insert_subtopic',methods = ['POST'])  
def insert_subtopic():  
    param = request.get_json()
    result = subtopic.add_subtopic(**param)
    return result

@app.route('/select_subtopic',methods = ['POST'])  
def select_subtopic():  
    param = request.get_json()
    result = subtopic.get_subtopic(**param)
    return result

@app.route('/update_subtopic',methods = ['POST'])  
def update_subtopic():  
    param = request.get_json()
    result = subtopic.update_subtopic(**param)
    return result

@app.route('/delete_subtopic',methods = ['POST'])  
def delete_subtopic():  
    param = request.get_json()
    result = subtopic.delete_subtopic(**param)
    return result

@app.route('/insert_content',methods = ['POST']) 
def insert_content():  
    param = request.get_json()
    result = content.add_content(**param)
    return result

@app.route('/select_content',methods = ['POST'])  
def select_content():
    param = request.get_json()
    result = content.get_content(**param)
    return result

@app.route('/update_content',methods = ['POST'])  
def update_content():  
    param = request.get_json()
    result = content.update_content(**param)
    return result

@app.route('/delete_content',methods = ['POST'])  
def delete_content():  
    param = request.get_json()
    result = content.delete_content(**param)
    return result

@app.route('/get_content_desc',methods = ['POST'])  
def get_content_desc():
    param = request.get_json()
    result = content.get_desc(**param)
    return result

@app.route('/update_contentdesc',methods = ['POST'])  
def update_contentdesc():  
    param = request.get_json()
    result = content.update_content(**param)
    return result

@app.route('/get_question',methods=['POST'])
def get_question():
    param = request.get_json()
    result = quizz.get_question(**param)
    return result

@app.route('/add_question',methods=['POST'])
def add_question():
    param = request.get_json()
    result = quizz.add_question(**param)
    return result

@app.route('/delete_question',methods=['POST'])
def delete_question():
    param = request.get_json()
    result = quizz.delete_question(**param)
    return result



if __name__ == '__main__':  
   app.run(debug = True)