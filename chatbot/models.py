from django.db import models

# Create your models here.

class Step(models.Model):
    current_state = models.CharField(max_length=255, default='greeting')
    
    def __str__(self):
        return f'{self.current_state}'
    
    
class User(models.Model):
    user_name = models.CharField(max_length=255)
    user_session = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='user_session')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user_name} {self.user_session} {self.message} {self.timestamp}'
    

# class Log(models.Model):
#   timestamp = models.DateTimeField(auto_now_add=True)
    