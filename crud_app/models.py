from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")

    # Este es un comentario para forzar la detección de cambios

    def __str__(self):
        return self.name

class ChangeLog(models.Model):
    ACTION_CHOICES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='change_logs')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action.capitalize()} by {self.user.username} on {self.timestamp}"
