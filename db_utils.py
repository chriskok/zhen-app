# Load Database Pkg
from os import name
import sqlite3
from datetime import datetime

conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_page_visited_table():
	c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT,timeOfvisit TIMESTAMP)')

def add_page_visited_details(pagename,timeOfvisit):
	c.execute('INSERT INTO pageTrackTable(pagename,timeOfvisit) VALUES(?,?)',(pagename,timeOfvisit))
	conn.commit()

def view_all_page_visited_details():
	c.execute('SELECT * FROM pageTrackTable')
	data = c.fetchall()
	return data


# # Fxn To Track Input & Prediction
# def create_emotionclf_table():
# 	c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT,prediction TEXT,probability NUMBER,timeOfvisit TIMESTAMP)')

# def add_prediction_details(rawtext,prediction,probability,timeOfvisit):
# 	c.execute('INSERT INTO emotionclfTable(rawtext,prediction,probability,timeOfvisit) VALUES(?,?,?,?)',(rawtext,prediction,probability,timeOfvisit))
# 	conn.commit()

# def view_all_prediction_details():
# 	c.execute('SELECT * FROM emotionclfTable')
# 	data = c.fetchall()
# 	return data

def create_question_answer_table():
	c.execute('CREATE TABLE IF NOT EXISTS qnaTable(quizID TEXT, userID TEXT, questionID TEXT, questionText TEXT, answerText TEXT, timeOfAnswer TIMESTAMP)')

def add_question_answer_details(quizID, userID, questionID, questionText, answerText, timeOfAnswer):
	c.execute('INSERT INTO qnaTable(quizID, userID, questionID, questionText, answerText, timeOfAnswer) VALUES(?,?,?,?,?,?)',\
        (quizID, userID, questionID, questionText, answerText, timeOfAnswer))
	conn.commit()

def view_all_question_answer_details():
	c.execute('SELECT * FROM qnaTable')
	data = c.fetchall()
	return data

def delete_qna_by_quizID(quizID):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the q&a
    :return:
    """
    sql = 'DELETE FROM qnaTable WHERE quizID=?'
    c.execute(sql, (quizID,))
    conn.commit()

if __name__ == '__main__':
    create_question_answer_table()

    add_question_answer_details('akosdk', 'robot1', '01', 'Name?', 'Robo 1', datetime.now())
    add_question_answer_details('akosdk', 'robot1', '02', 'Purpose?', 'Spread Butter', datetime.now())
    add_question_answer_details('akosdk', 'robot2', '01', 'Name?', 'Robo 2', datetime.now())
    add_question_answer_details('akosdk', 'robot2', '02', 'Purpose?', 'Spread Jam', datetime.now())

    print(len(view_all_question_answer_details()))

    delete_qna_by_quizID('akosdk')

    print(view_all_question_answer_details())


