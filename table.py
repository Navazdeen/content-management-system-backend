from database import Topic, Quizz, SubTopic, Content
from database import SessionMaker
import json


class Quizz_Table():
    def get_question(self, id):
        session = SessionMaker()
        results = session.query(Quizz).filter_by(topic_id=id).all()
        session.close()
        temp = []
        for result in results:
            id = result.question_id
            temp.append({'id': result.question_id, 'question': result.question, 'options': [
                result.option1, result.option2, result.option3, result.option4, result.Anwers]})
        return(json.dumps(dict(question = temp)))

    def delete_question(self, topic_id, id):
        session = SessionMaker()
        result = session.query(Quizz).filter_by(question_id=id, topic_id=topic_id).first()
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
            temp['T_'+str(id)] = result.topic_name
        return(json.dumps(temp)), 200

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


class Subtopic_Table():
    def get_subtopic(self, topic_id):
        session = SessionMaker()
        results = session.query(SubTopic).filter_by(topic_id=topic_id).all()
        session.close()
        temp = {}
        for result in results:
            temp['S_'+str(result.id)] = result.subtopic_name
        return (json.dumps(temp))

    def add_subtopic(self, name, topic_id):
        session = SessionMaker()
        subtopic = SubTopic(subtopic_name=name, topic_id=topic_id)
        session.add(subtopic)
        session.commit()
        session.close()
        return(json.dumps(dict(response='added successfully', status=200)))

    def update_subtopic(self, name, id, topic_id):
        session = SessionMaker()
        result = session.query(SubTopic).filter_by(
            id=id, topic_id=topic_id).first()
        if result:
            result.subtopic_name = name
            session.commit()
            return(json.dumps(dict(response='updated successfully', status=200)))
        return(json.dumps(dict(response='Not found', status=404)))

    def delete_subtopic(self, id, topic_id):
        session = SessionMaker()
        result = session.query(SubTopic).filter_by(
            id=id, topic_id=topic_id).first()
        if result:
            session.delete(result)
            session.commit()
            return(json.dumps(dict(response='deleted successfully', status=200)))
        return(json.dumps(dict(response='Not found', status=404)))


class Content_Table():
    def get_content(self, topic_id, subtopic_id):
        session = SessionMaker()
        results = session.query(Content).filter_by(
            topic_id=topic_id, subtopic_id=subtopic_id).all()
        session.close()
        temp = {}
        for result in results:
            temp['C_'+str(result.id)] = result.content_name
        return(json.dumps(temp))

    def get_desc(self, topic_id, subtopic_id, id):
        session = SessionMaker()
        results = session.query(Content).filter_by(
            topic_id=topic_id, subtopic_id=subtopic_id, id=id).all()
        session.close()
        temp = {}
        for result in results:
            temp['desc'] = result.content_desc
        return(json.dumps(temp))

    def add_content(self, topic_id, subtopic_id, content_name, content_desc=''):
        session = SessionMaker()
        content = Content(topic_id=topic_id, subtopic_id=subtopic_id,
                          content_name=content_name, content_desc=content_desc)
        session.add(content)
        session.commit()
        return(json.dumps(dict(response='added successfully', status=200)))

    def update_content(self, topic_id, subtopic_id, id, content_name=None, content_desc=None):
        session = SessionMaker()
        result = session.query(Content).filter_by(
            topic_id=topic_id, subtopic_id=subtopic_id, id=id).first()
        if result:
            if content_name:
                result.content_name = content_name
            else:
                result.content_desc = content_desc
            session.commit()
            return(json.dumps(dict(response='updateed successfully', status=200)))
        return(json.dumps(dict(response='Not found', status=404)))

    def delete_content(self, topic_id, subtopic_id, id):
        session = SessionMaker()
        result = session.query(Content).filter_by(
            topic_id=topic_id, subtopic_id=subtopic_id, id=id).first()
        if result:
            session.delete(result)
            session.commit()
            return(json.dumps(dict(response='deleted successfully', status=200)))
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
    # topic_.delete_topic(3)
    # print(topic_.get_topic(), '----')
    # topic_.add_topic('ML')
    # print(topic_.get_topic(), '----')
    # print(quizz.get_question(1))
    subtopic = Subtopic_Table()
    # print(subtopic.add_subtopic('TensorFlow', topic_id=3))
    # print(subtopic.get_subtopic(topic_id=3), '----')
    # print(subtopic.delete_subtopic(id=9))
    # print(subtopic.update_subtopic('Scikit_learn', id=9,topic_id=3))
    # print(subtopic.get_subtopic(5))
    content = Content_Table()
    # print(content.add_content(topic_id=3,subtopic_id=10, content_name='Introduction'))
    # print(content.get_content(topic_id=3, subtopic_id=10))
    # print(content.update_content(topic_id=3, subtopic_id=9, id=1,content_desc='This is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the introThis is the intro'))
    # print(content.delete_content(topic_id=3,subtopic_id=9, id=1))
