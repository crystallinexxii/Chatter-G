from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Room(models.Model):
    room_code = models.CharField(max_length=100)
    room_name = models.CharField(max_length=100)

    def __str__(self):
        return self.room_name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message