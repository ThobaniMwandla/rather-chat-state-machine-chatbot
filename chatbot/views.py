from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Step
from .api.serializers import UserSerializer, StepSerializer

# Create your views here.
class ChatBotView(APIView):
    def post(self, request):
        user_name = request.data.get('user_name','')
        message = request.data.get('message', '')

        # Retrieve or create the user session
        user_session, created = User.objects.get_or_create(user_name=user_name)
        user_session_serializer = UserSerializer(user_session)

        # Handle state transitions based on user input
        if user_session.current_state == 'greeting':
            response_message = 'Hello! How can I help you today?'
            user_session.current_state = 'question'
        elif user_session.current_state == 'question':
            response_message = f'You asked: {message}. How can I assist you further?'
            user_session.current_state = 'end'
        elif user_session.current_state == 'end':
            response_message = 'Thank you for chatting with me. Have a great day!'
            user_session.current_state = 'greeting'

        # Save the chat interaction
        chat_interaction = Step.objects.create(user_session=user_session, message=message)
        chat_interaction_serializer = StepSerializer(chat_interaction)

        # Save the updated user session
        user_session.save()

        return Response({
            'user_session': user_session_serializer.data,
            'chat_interaction': chat_interaction_serializer.data,
            'response_message': response_message
        }, status=status.HTTP_200_OK)
        