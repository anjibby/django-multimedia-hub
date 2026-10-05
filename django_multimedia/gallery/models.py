from django.db import models
from django.contrib.auth.models import User

class MediaItem(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='multimedia/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media_items')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_media_type_display()})"

    class Meta:
        ordering = ['-uploaded_at']