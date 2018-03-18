import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_{}'.format(self.room_name) # name of the group
        
        # Adding the channel to the group
        await self.channel_layer.group_add(self.room_group_name,
                                                    self.channel_name) 
        

        await self.accept()

    async def receive(self, text_data):
        text_data = json.loads(text_data)
        message = text_data['message']

        await self.channel_layer.group_send(self.room_group_name, {
                                                        'type': 'chat_message',
                                                        'message': message
                                                        } 
                                                    )

    # Receive message from room group
    # The `message` that is passed above will be available as an event in
    # `chat_message`
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
   
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name,
                                                        self.channel_name)
