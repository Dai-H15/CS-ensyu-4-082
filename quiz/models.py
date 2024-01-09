from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    total_questions = models.PositiveIntegerField()
    body = models.TextField()
    result = models.TextField(blank=True, null=True)
    posted_at = models.DateField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    answer = models.PositiveIntegerField(default=0)
    like = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.text[:10]