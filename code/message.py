from flask_restful import Resource, reqparse
import sqlite3

class Message(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('author',
    type=str,
    required=True)
    parser.add_argument('title',
    type=str,
    required=True)
    parser.add_argument('body',
    type=str,
    required=True)


    def get(self, message_id):
        message = self.find_message_by_id(message_id)

        if message:
            return message, 200
        else:
            return {'message': 'message doesn\'t exist'}, 404


    @classmethod
    def find_message_by_id(cls, message_id):
        connection = sqlite3.connect('message.db')
        cursor = connection.cursor()

        query = "SELECT * FROM messages WHERE id=?"
        result = cursor.execute(query,(message_id,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'message': {'id': row[0], 'author': row[1], 'title': row[2], 'message': row[3]}}


    def post(self):
        request_data = Message.parser.parse_args()
        message = {'author': request_data['author'], 'title': request_data['title'], 'body': request_data['body']}

        try:
            self.insert(message)
        except Exception as e:
            print(e)
            return {'message': 'An error occured while inserting message'}, 500


        return message, 201


    @classmethod
    def insert(cls, message):
        connection = sqlite3.connect('message.db')
        cursor = connection.cursor()

        query = "INSERT INTO messages VALUES (NULL, ?, ?, ?)"
        cursor.execute(query, (message['author'], message['title'], message['body']))

        connection.commit()
        connection.close()
