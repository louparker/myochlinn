from django.db import models
from django.utils.safestring import mark_safe

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50, blank=True, null=True)
    preview = models.TextField()
    text_content = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    source_link = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
