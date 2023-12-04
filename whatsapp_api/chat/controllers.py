# chat/controllers.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import ChatService
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


import json


@api_view(['POST'])
def create_chatroom(request):
    name = request.data.get('name')
    max_members = request.data.get('max_members')
    chat_room = ChatService.create_chatroom(name, max_members)
    return Response({'id': chat_room.id, 'name': chat_room.name, 'max_members': chat_room.max_members})

@api_view(['POST'])
def create_user(request):
    name = request.data.get('username')
    user = ChatService.create_user(name)
    return Response({'id': user.id, 'name': user.username})

@api_view(['GET'])
def list_chatrooms(request):
    chatrooms = ChatService.get_chatrooms()
    response_data = []

    for room in chatrooms:
        users_data = [{'id': user.id, 'username': user.username} for user in room.users.all()]

        response_data.append({
            'id': room.id,
            'name': room.name,
            'max_members': room.max_members,
            'users': users_data
        })
    return Response(response_data)

@api_view(['GET'])
def list_users(request):
    users = ChatService.list_users()
    response_data = [{'id': user.id, 'username': user.username} for user in users]
    return Response(response_data)

@api_view(['POST'])
def leave_chatroom(request):
    user_id = request.data.get('user_id')
    chatroom_id = request.data.get('chatroom_id')
    
    try:
        ChatService.leave_chatroom(user_id, chatroom_id)
        return Response({'message': 'User successfully left the chatroom'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def enter_chatroom(request):
    user_id = request.data.get('user_id')
    chatroom_id = request.data.get('chatroom_id')
    
    try:
        ChatService.enter_chatroom(user_id, chatroom_id)
        return Response({'message': 'User successfully entered the chatroom'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def send_message(request):
    user_id = request.data.get('user_id')
    chatroom_id = request.data.get('chatroom_id')
    content = request.data.get('content')
    
    try:
        attachment = request.FILES.get('attachment')
        ChatService.send_message(user_id, chatroom_id, content, attachment)
        return Response({'message': 'Message sent successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['POST'])
# def send_message(request):
#     user_id = request.data.get('user_id')
#     chatroom_id = request.data.get('chatroom_id')
#     content = request.data.get('content')
    
#     try:
#         attachment = request.FILES.get('attachment')

#         channel_layer = get_channel_layer()
#         print("hhhhhhhh", channel_layer)
#         async_to_sync(channel_layer.group_send)(
#             f"chat_{chatroom_id}",
#             {
#                 'type': 'chat.message',
#                 'user_id': user_id,
#                 'content': content,
#                 'attachment': attachment,
#             }
#         )

#         return Response({'message': 'Message sent successfully'}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_messages(request, chatroom_id):
    try:
        messages = ChatService.list_messages(chatroom_id)
        return Response([{'chat_room':message.chat_room.name ,'user': message.user.username, 'content': message.content, 'attachment': message.attachment.url if message.attachment else None} for message in messages], status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    