# chat/services.py
from .repositories import ChatRepository

class ChatService:
    @staticmethod
    def create_chatroom(name, max_members):
        return ChatRepository.create_chatroom(name, max_members)

    @staticmethod
    def get_chatrooms():
        return ChatRepository.get_chatrooms()
    
    @staticmethod
    def list_users():
        return ChatRepository.list_users()

    @staticmethod
    def leave_chatroom(user, chat_room):
        ChatRepository.leave_chatroom(user, chat_room)

    @staticmethod
    def create_user(user):
        return ChatRepository.create_user(user)

    @staticmethod
    def enter_chatroom(user, chat_room):
        ChatRepository.enter_chatroom(user, chat_room)

    @staticmethod
    def send_message(user, chat_room, content, attachment=None):
        return ChatRepository.send_message(user, chat_room, content, attachment)

    @staticmethod
    def list_messages(chat_room):
        return ChatRepository.list_messages(chat_room)
    

    # @staticmethod
    # def list_messages(chatroom_id):
    #     chatroom = ChatRoom.objects.get(id=chatroom_id)
    #     return ChatRepository.list_messages(chatroom)
