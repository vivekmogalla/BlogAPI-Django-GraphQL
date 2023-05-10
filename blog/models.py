from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    publish_date = models.DateField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text