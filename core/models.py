from django.db import models
from django.contrib.auth import get_user_model
import uuid, base64

# Create your models here.

class Tag(models.Model):
    tag_id = models.CharField(max_length=15, primary_key=True, editable=False)
    tag_name = models.CharField(max_length=25)
    
    def save(self, *args, **kwargs):
        if not self.tag_id:
            # Generate a shorter base64-encoded UUID
            hex_string = uuid.uuid4().hex
            bytes_data = bytes.fromhex(hex_string)
            data = base64.urlsafe_b64encode(bytes_data).decode('ascii')[:12]
            self.tag_id = data.replace("-","").replace("_", "")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.tag_name}"
    

class NewsItem(models.Model):
    id = models.CharField(max_length=15, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False, null=False, max_length=35000)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name='news_items')
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            # Generate a shorter base64-encoded UUID
            hex_string = uuid.uuid4().hex
            bytes_data = bytes.fromhex(hex_string)
            data = base64.urlsafe_b64encode(bytes_data).decode('ascii')[:12]
            self.id = data.replace("-","").replace("_", "")
        super().save(*args, **kwargs)
    