from django.db import models
from django.utils import timezone
from customUser.models import CustomUserModel

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    detail = models.TextField()
    total_questions = models.PositiveIntegerField()
    body = models.TextField()
    result = models.TextField(blank=True, null=True)
    shuffle_q = models.BooleanField(default=False)
    shuffle_c = models.BooleanField(default=False)
    posted_at = models.DateTimeField(default=timezone.now)
    answer = models.PositiveIntegerField(default=0)
    like = models.PositiveIntegerField(default=0)
    image = models.ImageField(default='quiz/static/quiz/images/no_image_square.jpg', upload_to='images/quiz/')
    
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