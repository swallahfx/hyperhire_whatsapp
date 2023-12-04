# chat/repositories.py
from .entity import ChatRoom, Message, User

class ChatRepository:
    @staticmethod
    def create_chatroom(name, max_members):
        return ChatRoom.objects.create(name=name, max_members=max_members)
    
    @staticmethod
    def create_user(name):
        return User.objects.create(username=name)

    @staticmethod
    def list_users():
        return User.objects.all()

    @staticmethod
    def get_chatrooms():
        return ChatRoom.objects.all()

    @staticmethod
    def leave_chatroom(user, chat_room):
        # chat_room.members.remove(user)
        room = ChatRoom.objects.get(id=chat_room)
        user = User.objects.get(id=user)

        room.users.remove(user)

    @staticmethod
    def enter_chatroom(user, chat_room):
        room = ChatRoom.objects.get(id=chat_room)
        user = User.objects.get(id=user)

        room.users.add(user)
        # chat_room.members.add(user)

    @staticmethod
    def send_message(user, chat_room, content, attachment=None):
        user = User.objects.get(id=user)
        chat_room = ChatRoom.objects.get(id=chat_room)
        return Message.objects.create(user=user, chat_room=chat_room, content=content, attachment=attachment)

    @staticmethod
    def list_messages(chat_room):
        return Message.objects.filter(chat_room=chat_room)
