from django.db import models

# Create your models here.
class Passwords(models.Model):
    user_id = models.IntegerField(null=False)
    label = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.label} - User ID: {self.user_id}"