# hyperhire_whatsapp

# Django Chat App

## Overview

This Django Chat App is designed to provide basic chat functionality with features such as creating chatrooms, listing chatrooms, entering and leaving chatrooms, sending text messages, and sending attachments.

## Project Structure

The project follows a modular structure with the following components:

- **chat**: Django app containing the main chat functionality.
  - **controller**: Contains the views/controllers for handling HTTP requests.
  - **service**: Business logic layer for handling chat-related operations.
  - **repository**: Database interaction layer for handling data storage and retrieval.
  - **entity**: Defines Django models for User, ChatRoom, and Message.

- **root**: Directories for storing attachments (pictures and videos).

- **whatsapp_api**: Django project settings and configurations.

## Database Models

### User
- `id`: Auto-incremented primary key.
- `username`: Unique username for each user.

### ChatRoom
- `id`: Auto-incremented primary key.
- `name`: Name of the chatroom.
- `users`: Many-to-Many relationship with User model, representing chatroom members.
- `max_members`: Maximum number of members allowed in the chatroom.

### Message
- `id`: Auto-incremented primary key.
- `user`: Foreign key relationship with User model, representing the sender.
- `chat_room`: Foreign key relationship with ChatRoom model, representing the chatroom.
- `content`: Text content of the message.
- `attachment`: FileField for message attachments.

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/django-chat-app.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Apply migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the development server: `python manage.py runserver`

## API Endpoints

- **Create Chatroom**: POST `/api/create_chatroom/`
- **List Chatrooms**: GET `/api/list_chatrooms/`
- **Enter Chatroom**: POST `/api/enter_chatroom/<chatroom_id>/`
- **Leave Chatroom**: POST `/api/leave_chatroom/<chatroom_id>/`
- **Send Message**: POST `/api/send_message/<chatroom_id>/`
- **List Messages**: GET `/api/list_messages/<chatroom_id>/`

## WebSocket Integration

WebSocket functionality is integrated for real-time chat. WebSocket routing is defined in `chat/routing.py`, and consumers are implemented in `chat/consumers.py`.

## Swagger Integration

API documentation is available using Swagger. Visit `/swagger/` to explore and test the APIs.

## Testing

Run the development server and use tools like Postman or the Django Admin panel to test the APIs. Ensure WebSocket functionality is tested separately.
`https://documenter.getpostman.com/view/20949011/2s9YeK5qSi`
