# chat/urls.py
from django.urls import path
from .controllers import create_chatroom, list_chatrooms, leave_chatroom, enter_chatroom, send_message, list_messages, create_user, list_users

urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('list_users/', list_users, name='list_users'),
    path('create_chatroom/', create_chatroom, name='create_chatroom'),
    path('list_chatrooms/', list_chatrooms, name='list_chatrooms'),
    path('leave_chatroom/', leave_chatroom, name='leave_chatroom'),
    path('enter_chatroom/', enter_chatroom, name='enter_chatroom'),
    path('send_message/', send_message, name='send_message'),
    path('list_messages/<int:chatroom_id>/', list_messages, name='list_messages'),
]
