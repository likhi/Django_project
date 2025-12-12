
    
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

# already User IS Avaliable for US  by default

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    youtube_url = models.URLField(blank=True, null=True, help_text='Optional: YouTube video URL')
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # special methods / magic methods
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    visitor_name = models.CharField(max_length=100)
    visitor_email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Restore default to True (comments displayed immediately)
    is_approved = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        post_title = self.post.title if self.post else "General"
        return f"Comment by {self.visitor_name} on {post_title}"