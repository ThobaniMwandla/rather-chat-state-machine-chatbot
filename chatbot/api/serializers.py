from rest_framework import serializers
from chatbot.models import User, Step

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'

# class LogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Log
#         fields = '__all__'
