from django.db import models
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})


