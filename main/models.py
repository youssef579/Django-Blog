from django.db import models
from datetime import datetime
from users.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datetime = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-datetime",)

    def __str__(self):
        return self.title