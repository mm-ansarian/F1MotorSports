from django.db import models
from accounts.models import User


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.created_at})'

    class Meta:
        verbose_name_plural = 'News'
