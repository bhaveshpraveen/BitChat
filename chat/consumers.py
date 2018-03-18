import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_{}'.format(self.room_name) # name of the group
        
        # Adding the channel to the group
        async_to_sync(self.channel_layer.group_add)(self.room_group_name,
                                                    self.channel_name) 
        

        self.accept()

    def receive(self, text_data):
        text_data = json.loads(text_data)
        message = text_data['message']

        async_to_sync(self.channel_layer.group_send)(self.room_group_name, {
                                                        'type': 'chat_message',
                                                        'message': message
                                                        } 
                                                    )

    # Receive message from room group
    # The `message` that is passed above will be available as an event in
    # `chat_message`
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
   
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name,
                                                        self.channel_name)
