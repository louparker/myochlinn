from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50, blank=True, null=True)
    preview = models.TextField()
    section_one = models.TextField(blank=False, null=False)
    section_two = models.TextField(blank=True, null=True)
    section_three = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    source_link = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title
