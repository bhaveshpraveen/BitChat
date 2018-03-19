import json

from django.core import serializers

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_{}'.format(self.room_name) # name of the group

        # Room instance
        self.room = await self.get_room()
        
        # Adding the channel to the group
        await self.channel_layer.group_add(self.room_group_name,
                                            self.channel_name)
        
        await self.accept()

    async def receive(self, text_data):
        text_data = json.loads(text_data)
        message = text_data['message']

        msg = await self.add_message(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': msg.text,
                'sent_by': msg.owner.username,
                'time': str(msg.created)
             })

    @database_sync_to_async
    def get_room(self):
        return Room.objects.get(slug=self.room_name)

    @database_sync_to_async
    def add_message(self, message):
        print(message)
        return Message.objects.create(room=self.room, owner=self.scope['user'], text=message)

    # Receive message from room group
    # The `message` that is passed above will be available as an event in
    # `chat_message`
    async def chat_message(self, event):
        print(event)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event,
            'user': self.scope['user'].username
        }))
   
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name,
                                               self.channel_name)

#todo Reset password not working