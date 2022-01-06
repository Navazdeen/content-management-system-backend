from sqlalchemy.orm import session
from database import Topic, Quizz
from database import SessionMaker
import json


class Quizz_Table():
    def get_question(self, id):
        session = SessionMaker()
        results = session.query(Quizz).filter_by(topic_id=id).all()
        session.close()
        temp = {}
        for result in results:
            id = result.question_id
            temp[id] = {'id': result.question_id, 'question': result.question, 'options': [
                result.option1, result.option2, result.option3, result.option4]}
        return(json.dumps(temp))

    def delete_question(self, id, commit=True):
        session = SessionMaker()
        result = session.query(Quizz).filter_by(question_id=id).first()
        if result:
            session.delete(result)
            session.commit()
            return(json.dumps(dict(response='deleted successfully', status=200)))
        session.close()
        return(json.dumps(dict(response='Not found', status=404)))

    def add_question(self, topic_id, question, option1, option2, option3, option4, answer):
        session = SessionMaker()
        result = Quizz(topic_id=topic_id, question=question, option1=option1,
                       option2=option2, option3=option3, option4=option4, Anwers=answer)
        session.add(result)
        session.commit()
        session.close()
        return(json.dumps(dict(response='added successfully', status=200)))


class Topic_Table():
    def get_topic(self):
        session = SessionMaker()
        results = session.query(Topic).all()
        session.close()
        temp = {}
        for result in results:
            id = result.id
            temp[id] = {'id': result.id, 'name': result.topic_name}
        return(json.dumps(temp))

    def update_topic(self, id, name):
        session = SessionMaker()
        results = session.query(Topic).filter_by(id=id).first()
        if results:
            results.topic_name = name
            session.commit()
            return(json.dumps(dict(response='updated successfully', status=200)))
        session.close()
        return(json.dumps(dict(response='Not found', status=404)))

    def add_topic(self, name):
        session = SessionMaker()
        topic = Topic(topic_name=name)
        session.add(topic)
        session.commit()
        session.close()
        return(json.dumps(dict(response='added successfully', status=200)))

    def delete_topic(self, id):
        session = SessionMaker()
        results = session.query(Topic).filter_by(id=id).first()
        if results:
            session.delete(results)
            session.commit()
            return(json.dumps(dict(response='deleted successfully', status=200)))
        session.close()
        return(json.dumps(dict(response='Not found', status=404)))








if __name__ == '__main__':
    quizz = Quizz_Table()
    # quizz.add_question(1,'This is the question2', 'a','b', 'c', 'd', 'A')
    # print(quizz.get_question(17))
    # quizz.delete_question(5)
    topic_ = Topic_Table()
    # print(topic_.get_topic(), '----')
    # topic_.update_topic(14, 'AI')
    # print(topic_.get_topic(), '----')
    topic_.delete_topic(1)
    # print(topic_.get_topic(), '----')
    # topic_.add_topic('DL')
    print(topic_.get_topic(), '----')
    print(quizz.get_question(1))
