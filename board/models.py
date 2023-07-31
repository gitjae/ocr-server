from django.db import models
from django.utils import timezone

class Board(models.Model):
    post_no = models.AutoField(primary_key=True, auto_created=1000)
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    username = models.ForeignKey(
        'users.User', 
        on_delete=models.SET_NULL, 
        null=True, 
        to_field='username'
    )
    file = models.FileField(upload_to='', storage=None, max_length=100, blank=True, null=True)
    image_link = models.URLField(default='')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

