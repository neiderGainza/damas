import json
from channels.generic.websocket import WebsocketConsumer
from login import models as login_models



class OnLine(WebsocketConsumer):
    def connect(self):
        self.accept()


    def disconnect(self, close_code):
        self.usuario.online = False
        self.usuario.save()
        pass

    def receive(self, text_data):
        datos = json.loads(text_data)

        usuario = login_models.User.objects.get( name = datos['userName'])
        usuario.online = datos['value']
        usuario.save()

        self.usuario = usuario
        
        