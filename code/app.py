from flask import Flask
from flask_restful import Api
from message import Message, MessageList


app = Flask(__name__)
api  = Api(app)

api.add_resource(Message, '/message', '/message/<int:message_id>')
api.add_resource(MessageList, '/messages')

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
