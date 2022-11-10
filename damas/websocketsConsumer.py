import json
from channels.generic.websocket import WebsocketConsumer


class Comsumidor(WebsocketConsumer):
    def connect(self):
        self.accept()


    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        datos = json.loads(text_data)
        

        self.send(text_data=json.dumps({}))